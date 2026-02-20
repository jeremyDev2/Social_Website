from django.apps import AppConfig


class ImagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'images'
    
    #called when the app is initialized
    def ready(self):
        import signal handlers
        import images.signals
