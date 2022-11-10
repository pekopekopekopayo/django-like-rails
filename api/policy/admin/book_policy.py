import pdb
from api.policy.admin.admin_policy import AdminPolicy
from lib.policy.admin_base import is_admin

class BookPolicy(AdminPolicy):

    def get(self):
        return is_admin(self.user)

    def post(self): return self.get()

    def put(self): return self.get()

    def delete(self): return self.put()
