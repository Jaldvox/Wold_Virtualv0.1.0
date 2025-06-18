class Scene:
    """Modelo de escena para la base de datos."""

    def __init__(self, id, name, objects, camera_position, selected_object):
        self.id = id  # Identificador único de la escena
        self.name = name  # Nombre de la escena
        self.objects = objects  # Lista de objetos en la escena
        self.camera_position = camera_position  # Posición de la cámara
        self.selected_object = selected_object  # Objeto seleccionado en la escena

    def to_dict(self):
        """Convierte el modelo de escena a un diccionario para la serialización."""
        return {
            "id": self.id,
            "name": self.name,
            "objects": self.objects,
            "camera_position": self.camera_position,
            "selected_object": self.selected_object,
        }