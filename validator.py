class Validator:
    def username_is_valid(self, username):
        if len(username) < 3 or len(username) > 20:
            return False
        if ' ' in username:
            return False
        if username.islower():
            return False
        return True
