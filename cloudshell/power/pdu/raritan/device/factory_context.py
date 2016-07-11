from cloudshell.shell.core.context_utils import get_attribute_by_name
import inject


class FactoryContext:
    def __init__(self, context):
        api = inject.instance('api')
        password = get_attribute_by_name('Password', context)
        self._password = api.DecryptPassword(password).Value
        self._user = get_attribute_by_name('User', context)
        self._host = context.resource.address

    @property
    def user(self):
        return self._user

    @property
    def password(self):
        return self._password

    @property
    def host(self):
        return self._host