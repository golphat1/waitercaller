import hashlib
from os
import base64

class PasswordHelper:
    
    def get_hash(self, plain):
        hashed = hashlib.sha512(plain.encode()).hexdigest()
        return hashed
    
    def get_salt(self):
        salt = os.urandom(20)
        return base64.b64encode(salt).decode()
    
    def validate_password(self, plain, salt, expected):
        hashed_plain = self.get_hash(plain + salt)
        return hashed_plain == expected
    
    def generate_password(self, plain):
        salt = self.get_salt()
        hashed_plain = self.get_hash(plain + salt)
        return hashed_plain, salt
    
    def verify_password(self, plain, salt, hashed):
        return self.validate_password(plain, salt, hashed)
    
    def change_password(self, plain, old_salt, old_hashed):
        new_salt = self.get_salt()
        new_hashed = self.get_hash(plain + new_salt)
        return new_hashed, new_salt
    
    def forgot_password(self, username):
        # Implement forgot password functionality here