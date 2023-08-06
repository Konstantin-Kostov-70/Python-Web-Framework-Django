from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from DynamicWebsite.buyers.models import Buyer


@receiver(post_save, sender=User)
def post_save_create_buyer(sender, instance, created, **kwargs):

    print('sender:', sender)
    print('instance:', instance)
    print('created:', created)
    print(kwargs)

    if created:
        Buyer.objects.create(user=instance)

"""
This is printing information....
sender: <class 'django.contrib.auth.models.User'>
instance: Rado
created: True
{'signal': <django.db.models.signals.ModelSignal
object at 0x0000025B840F5D50>
'update_fields': None, 'raw': False, 'using': 'default'}
"""