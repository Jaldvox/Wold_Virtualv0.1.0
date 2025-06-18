def validate_email(email: str) -> bool:
    """Validate the format of an email address."""
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def validate_username(username: str) -> bool:
    """Validate the format of a username."""
    return len(username) >= 3 and len(username) <= 20 and username.isalnum()

def validate_password(password: str) -> bool:
    """Validate the strength of a password."""
    return (
        len(password) >= 8 and
        any(char.isdigit() for char in password) and
        any(char.isalpha() for char in password) and
        any(char in "!@#$%^&*()-_=+" for char in password)
    )

def validate_scene_data(scene_data: dict) -> bool:
    """Validate the structure of scene data."""
    required_keys = {'objects', 'camera_position', 'selected_object'}
    return required_keys.issubset(scene_data.keys()) and isinstance(scene_data['camera_position'], dict)