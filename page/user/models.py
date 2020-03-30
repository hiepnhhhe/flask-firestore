from passlib.hash import pbkdf2_sha256 as sha256 

class User(object):
    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name
        
    def __repr__(self):
        return(
            u'User(username={}, name={})'
            .format(self.username, self.name)
        )

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

class RevokedTokenModel(object):
    def __init__(self, id, jti):
        self.id = id
        self.jti = jti

        