import hashlib as hash
class toHash:
    def get_Hash(self,password):
        hash_object = hash.sha256(password.encode('utf-8'))
        return  hash_object.hexdigest()
    