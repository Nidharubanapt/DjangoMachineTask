from django.apps import AppConfig


# class UserPortalConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'user_portal'

class UserPortalConfig(AppConfig):
    name = 'user_portal'

    def ready(self):
        import user_portal.models  
