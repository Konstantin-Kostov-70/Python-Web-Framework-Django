import uuid
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from DynamicWebsite.buyers.models import Buyer
from DynamicWebsite.cars.models import Car


# @receiver(pre_save, sender=Car)
# def pre_save_modify_buyer_and_create_code(sender, instance, **kwargs):
#     if instance.code == '':
#         instance.code = str(uuid.uuid4()).replace('-', '').upper()[:10]
#
#     obj = Buyer.objects.get(user=instance.buyer.user)
#     obj.from_signal = True
#     obj.save()


@receiver(post_save, sender=Car)
def post_save_modify_buyer_and_create_code(sender, instance, created, **kwargs):
    if instance.code == '':
        instance.code = str(uuid.uuid4()).replace('-', '').upper()[:10]
        instance.save()

    obj = Buyer.objects.get(user=instance.buyer.user)
    obj.from_signal = True
    obj.save()