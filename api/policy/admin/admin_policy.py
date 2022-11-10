from api.policy.policy import Policy

class AdminPolicy(Policy):

    def admin_policy(func):
        def policy(user, record):
            if user.role != 2: return False
            func()
        return policy
