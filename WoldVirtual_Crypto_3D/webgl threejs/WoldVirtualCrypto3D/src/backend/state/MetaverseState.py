class MetaverseState:
    """Class to manage the overall state of the metaverse, including user and scene data."""

    def __init__(self):
        self.users = {}
        self.scenes = {}
        self.current_scene_id = None

    def add_user(self, user_id, user_data):
        """Add a user to the metaverse state."""
        self.users[user_id] = user_data

    def remove_user(self, user_id):
        """Remove a user from the metaverse state."""
        if user_id in self.users:
            del self.users[user_id]

    def set_current_scene(self, scene_id):
        """Set the current active scene."""
        self.current_scene_id = scene_id

    def add_scene(self, scene_id, scene_data):
        """Add a scene to the metaverse state."""
        self.scenes[scene_id] = scene_data

    def remove_scene(self, scene_id):
        """Remove a scene from the metaverse state."""
        if scene_id in self.scenes:
            del self.scenes[scene_id]

    def get_user_data(self, user_id):
        """Get data for a specific user."""
        return self.users.get(user_id)

    def get_scene_data(self, scene_id):
        """Get data for a specific scene."""
        return self.scenes.get(scene_id)

    def get_all_users(self):
        """Get all users in the metaverse."""
        return self.users

    def get_all_scenes(self):
        """Get all scenes in the metaverse."""
        return self.scenes