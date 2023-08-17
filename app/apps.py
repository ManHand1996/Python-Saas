from django.apps import AppConfig

from tracker import settings


class AppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"


if __name__ == "__main__":
    print(settings)
