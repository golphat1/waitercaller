class User:
    def __init__(self, email):
        self.email = email

    def is_authenticated(self):
        return True  # Simplified for this example

    def is_active(self):
        return True  # Adjust based on your logic

    def is_anonymous(self):
        return False  # Adjust based on your logic

    def get_id(self):
        return self.email  # Returns the email as the user ID
