class UserState:
    """Class to manage user-specific state, including authentication and profile data."""

    def __init__(self):
        self.user_id = None
        self.username = None
        self.is_authenticated = False
        self.profile_data = {}

    def login(self, user_id, username):
        """Authenticate the user and set user details."""
        self.user_id = user_id
        self.username = username
        self.is_authenticated = True

    def logout(self):
        """Log out the user and clear user details."""
        self.user_id = None
        self.username = None
        self.is_authenticated = False
        self.profile_data = {}

    def update_profile(self, profile_data):
        """Update the user's profile data."""
        self.profile_data.update(profile_data)

    def get_profile(self):
        """Return the user's profile data."""
        return self.profile_data

    def is_user_authenticated(self):
        """Check if the user is authenticated."""
        return self.is_authenticated