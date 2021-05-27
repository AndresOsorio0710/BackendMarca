from django.db import transaction
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from cellar_app.models import Cellar
from product_cellar_app.models import ProductCellar


@receiver(post_save, sender=ProductCellar)
def post_save_product_cellar(sender, instance, created, update_fields, **kwargs):
    def doit():
        if created:
            cellar_instance = Cellar.objects.get(uuid=instance.cellar_id)
            cellar_instance.free_capacity = cellar_instance.free_capacity - instance.quantity_entered
            cellar_instance.save(update_fields=('free_capacity',))
        elif (instance.deleted_at != None):
            cellar_instance = Cellar.objects.get(uuid=instance.cellar_id)
            cellar_instance.free_capacity = cellar_instance.free_capacity + instance.free_quantity
            cellar_instance.save(update_fields=('free_capacity',))
        else:
            update_fields

    transaction.on_commit(doit)
