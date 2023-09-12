from django.apps import AppConfig


class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'

"""
    # roda depois do filme carregado
    def ready(self):
        from .models import Usuario
        import os

        # pegar os campos do ambiente virtual servidor
        email = os.getenv("EMAIL_ADMIN")
        senha = os.getenv("SENHA_ADMIN")

        usuarios = Usuario.objects.filter(email=email)
        if not usuarios:
            Usuario.objects.create_superuser(username="admin", email=email, password=senha,
                                             is_active=True, is_staff=True)
"""