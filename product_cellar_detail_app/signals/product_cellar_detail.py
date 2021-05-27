from django.db import transaction
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from product_in_cellar_app.models import ProductInCellar
from product_in_cellar_detail_app.models import ProductInCellarDetail


@receiver(post_save, sender=ProductInCellarDetail)
def post_save_product_in_cellar_detail(sender, instance, created, update_fields, **kwargs):
    def doit():
        product_in_cellar_instance = ProductInCellar.objects.get(uuid=instance.product_in_cellar_id)
        if created:
            product_in_cellar_instance.free_quantity = product_in_cellar_instance.free_quantity + 1
            product_in_cellar_instance.save(update_fields=('free_quantity',))
        elif (instance.deletecd_at != None):
            product_in_cellar_instance.free_quantity = product_in_cellar_instance.free_quantity - 1
            product_in_cellar_instance.save(update_fields=('free_quantity',))
        else:
            update_fields

    transaction.on_commit(doit)
