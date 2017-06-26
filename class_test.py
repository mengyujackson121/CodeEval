import hashlib
class Account(object):
    hash_algorithm = hashlib.sha512
    def __init__(self, username, password):
        if not Account.is_password_strong(password):
            raise AssertionError("Password is not strong!")
        self.username = username
        m = Account.hash_algorithm()
        m.update(password)
        self.hashed_password = m.digest()

    def matches_password(self, attempt):
        m = Account.hash_algorithm()
        m.update(attempt)
        hashed_attempt = m.digest()
        return hashed_attempt == self.hashed_password

    @classmethod
    def is_password_strong(cls, password):
        if password == password.lower():
            return False
        if password == password.upper():
            return False
        if password.isalpha():
            return False
        if len(password) < 6:
            return False
        return True

    def __str__(self):
        return "username: " + self.username + "\tpassword: NOT TELLING YOU"



def main():
    x = Account("mengyu", "secret_Dassword")
    y = Account("steven", "Fo123345")
    print x
    print type(x)
    print x.username
    print x.hashed_password
    print x.matches_password("secret_Dassword")
    print x.matches_password("foo")
    print y.hashed_password
    print y.matches_password("secret_Dassword")
    print y.matches_password("foo")

main()
