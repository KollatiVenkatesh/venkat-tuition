from django.apps import AppConfig
from django.db.models.signals import post_migrate
import os


def create_render_superuser(sender, **kwargs):
    if os.environ.get("RENDER_SUPERUSER") != "true":
        return

    from django.contrib.auth import get_user_model

    User = get_user_model()

    username = os.environ.get("RENDER_ADMIN_USERNAME", "admin")
    password = os.environ.get("RENDER_ADMIN_PASSWORD", "admin123")
    email = os.environ.get("RENDER_ADMIN_EMAIL", "admin@example.com")

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )


class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'

    def ready(self):
        post_migrate.connect(create_render_superuser, sender=self)
