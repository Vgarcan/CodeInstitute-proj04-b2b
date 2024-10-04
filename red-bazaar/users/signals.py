from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser, Profile

# crea la signal para el modelo CUSTOMUSER


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Crearte a new user profile
    """
    if created and not instance.is_superuser:
        Profile.objects.create(user=instance)
        print('Created user profile')
    elif not instance.is_superuser:
        instance.profile.save()
