import base64
import raritan.rpc

# JSON module
#
# alternatively for python < 2.6, use jsonrpc.json
# from http://json-rpc.org/wiki/python-json-rpc
import json

try:
    # Python 3
    import urllib.request
    urllib_request = urllib.request
except ImportError:
    # Python 2
    import urllib
    urllib_request = urllib

class Agent(object):
    """Provides transport to one RPC service, e.g. one PX2 device - holds host,
       user name, and password."""
    id = 1

    def __init__(self, proto, host, user = None, passwd = None, token = None, debug = False):
        self.url = "%s://%s" % (proto, host)
        self.user = user
        self.passwd = passwd
        self.token = token # authentication token
        self.debug = debug

        Agent.defaultInst = self

    def set_auth_basic(self, user, passwd):
        self.user = user
        self.passwd = passwd
        self.token = None

    def set_auth_token(self, token):
        self.user = None
        self.passwd = None
        self.token = token

    def handle_http_redirect(self, rid, headers):
        location = headers.getheader('Location')
        baselen = len(location) - len(rid)
        if baselen <= 0:
            return False
        elif location[baselen:] != rid:
            return False
        else:
            self.url = location[:baselen]
            if self.debug:
                print("Redirected to: " + self.url)
            return True

    def json_rpc(self, target, method, params = [], redirected = False):
        request_json = json.dumps({"method": method, "params": params, "id": Agent.id})
        if (self.debug):
            print("json_rpc: %s() - %s: , request = %s" % (method, target, request_json))
        Agent.id += 1

        import ssl
        context = ssl._create_unverified_context()
        opener = urllib_request.URLopener(context=context)
        if self.token != None:
            opener.addheader("X-SessionToken", self.token)
        elif self.user != None and self.passwd != None:
            basic = base64.b64encode(str.encode('%s:%s' % (self.user, self.passwd)))
            opener.addheader('Authorization', 'Basic:' + bytes.decode(basic))

        target_url = "%s/%s" % (self.url, target)

        try:
            fd = opener.open(target_url, request_json)
        except IOError as e:
            if hasattr(e, 'code') and e.code == 302 and not redirected:
                # handle HTTP-to-HTTPS redirect and try again
                if self.handle_http_redirect(target, e.args[3]):
                    return self.json_rpc(target, method, params, True)
            raise raritan.rpc.HttpException("Opening URL %s failed: %s" % (target_url, e))

        # get and process response
        resp_code = fd.getcode()
        try:
            resp = bytes.decode(fd.read())
        except:
            raise raritan.rpc.HttpException("Reading response failed.")

        if resp_code != 200:
            raise raritan.rpc.HttpException("HTTP Error %d\nResponse:\n%s" % (resp_code, resp))

        if (self.debug):
            print("json_rpc: Response:\n%s" % resp)

        try:
            resp_json = json.loads(resp)
        except ValueError as e:
            raise raritan.rpc.JsonRpcSyntaxException(
                    "Decoding response to JSON failed: %s" % e)

        if "error" in resp_json:
            try:
                code = resp_json["error"]["code"]
                msg = resp_json["error"]["message"]
            except KeyError:
                raise raritan.rpc.JsonRpcSyntaxException(
                        "JSON RPC returned malformed error: %s" % resp_json)
            raise raritan.rpc.JsonRpcErrorException(
                    "JSON RPC returned error: code = %d, msg = %s" % (code, msg))

        try:
            res = resp_json["result"]
        except KeyError:
            raise raritan.rpc.JsonRpcSyntaxException(
                    "Result is missing in JSON RPC response: %s" % resp_json)
            
        return res
