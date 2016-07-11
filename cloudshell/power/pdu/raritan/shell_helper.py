

def get_outlets_by_address(outlets, ports):
    # ports: ['192.168.30.128/4', '192.168.30.128/6']

    def socket(port):
        n = int(port.split('/')[-1])
        return outlets[n-1]

    return [socket(x) for x in ports]