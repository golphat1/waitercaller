MOCK_USERS = [{"email": "test@example.com", "salt":
    "8Fb23mMNHD5Zb8pr2qWA3PE9bH0=", "hashed":
        "e10adc3949ba59abbe56e057f20f883e"
        f0aa6a31f780e576578f791b5555b50df46303f0c3a7f2d21f91aa1429ac22e"}]

class MockDBHelper:

    def get_user(self, email):
        if email in MOCK_USERS:
            return email
        return None
        
    def get_user(self, email):
    user = {x for x in MOCK_USERS if x.get("email") == email}
    if user:
        return user[0]
    return None
    
    def add_user(self, email, salt, hashed):
        MOCK_USERS.append({"email": email, "salt": salt, "hashed": hashed})
        return True
        