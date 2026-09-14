import os
from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_default_superuser(sender, **kwargs):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'Geologyrenni')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'otanerstudio')
    
    u, created = User.objects.get_or_create(username=username)
    u.set_password(password)
    u.is_superuser = True
    u.is_staff = True
    u.is_active = True
    u.save()
    print(f"--> SUPERUSER {username} U PËRDITËSUA ME SUKSES!")

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        post_migrate.connect(create_default_superuser)
