class User:
    """Modelo de usuario para la base de datos."""

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"

    def save(self):
        """Método para guardar el usuario en la base de datos."""
        # Implementar la lógica para guardar el usuario en la base de datos
        pass

    @classmethod
    def find_by_username(cls, username):
        """Método para encontrar un usuario por su nombre de usuario."""
        # Implementar la lógica para buscar un usuario en la base de datos
        pass

    @classmethod
    def find_by_email(cls, email):
        """Método para encontrar un usuario por su correo electrónico."""
        # Implementar la lógica para buscar un usuario en la base de datos
        pass

    def update(self, **kwargs):
        """Método para actualizar los atributos del usuario."""
        for key, value in kwargs.items():
            setattr(self, key, value)
        # Implementar la lógica para guardar los cambios en la base de datos
        pass

    def delete(self):
        """Método para eliminar el usuario de la base de datos."""
        # Implementar la lógica para eliminar el usuario de la base de datos
        pass