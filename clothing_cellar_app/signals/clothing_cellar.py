from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from product_cellar_app.models import ProductCellar
from clothing_cellar_app.models import ClothingCellar


@receiver(post_save, sender=ClothingCellar)
def post_save_clothing_cellar(sender, instance, created, update_fields, **kwargs):
    def doit():
        product_cellar_instance = ProductCellar.objects.get(uuid=instance.product_cellar_id)
        if created:
            product_cellar_instance.free_quantity = product_cellar_instance.free_quantity + 1
            product_cellar_instance.save(update_fields=('free_quantity',))
        elif (instance.deleted_at != None):
            product_cellar_instance.free_quantity = product_cellar_instance.free_quantity - 1
            product_cellar_instance.save(update_fields=('free_quantity',))
        else:
            update_fields

    transaction.on_commit(doit)
