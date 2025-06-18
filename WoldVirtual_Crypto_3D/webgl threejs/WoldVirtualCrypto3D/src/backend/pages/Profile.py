from reflex import rx

class Profile(rx.Page):
    """Página de perfil del usuario."""

    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.user_data = self.fetch_user_data()

    def fetch_user_data(self):
        """Simula la recuperación de datos del usuario."""
        # Aquí se puede implementar la lógica para obtener datos del usuario desde la base de datos
        return {
            "username": "UsuarioEjemplo",
            "email": "usuario@ejemplo.com",
            "avatar": "ruta/a/avatar.png"
        }

    def render(self):
        """Renderiza la página de perfil."""
        return rx.vstack(
            rx.heading(f"Perfil de {self.user_data['username']}"),
            rx.text(f"Email: {self.user_data['email']}"),
            rx.image(src=self.user_data['avatar'], alt="Avatar", width="100px"),
            spacing="1rem",
            padding="2rem"
        )