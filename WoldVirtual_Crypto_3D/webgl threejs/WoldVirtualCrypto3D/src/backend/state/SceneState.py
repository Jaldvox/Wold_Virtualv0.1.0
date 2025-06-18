class SceneState:
    """Class to manage the state of the 3D scene, including objects and their properties."""

    def __init__(self):
        self.objects = []  # List to hold 3D objects in the scene
        self.camera_position = {"x": 0, "y": 0, "z": 5}  # Default camera position
        self.selected_object = None  # Currently selected object in the scene

    def add_object(self, obj):
        """Add a new object to the scene."""
        self.objects.append(obj)

    def remove_object(self, obj):
        """Remove an object from the scene."""
        if obj in self.objects:
            self.objects.remove(obj)

    def update_camera_position(self, x, y, z):
        """Update the camera position."""
        self.camera_position = {"x": x, "y": y, "z": z}

    def select_object(self, obj):
        """Select an object in the scene."""
        self.selected_object = obj

    def deselect_object(self):
        """Deselect the currently selected object."""
        self.selected_object = None

    def get_scene_data(self):
        """Return the current state of the scene."""
        return {
            "objects": self.objects,
            "camera_position": self.camera_position,
            "selected_object": self.selected_object,
        }