from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """
    AppConfig for the 'authentication' app.

    This AppConfig is used to configure settings specific to the 'authentication' app.

    Attributes:
        default_auto_field (str): The default primary key field type for models in this app.
        name (str): The name of the app ('authentication').
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'
