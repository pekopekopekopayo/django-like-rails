from api.policy.policy import Policy
from lib.policy.admin_base import is_admin

class AdminPolicy(Policy):

    def get(self):
        return is_admin(self.user)

    def post(self): return self.get()

    def put(self): return self.get()

    def delete(self): return self.put()
