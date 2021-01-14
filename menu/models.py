from django.db import models


# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.CharField(max_length=50, unique=True, null=True, default=True)

    def get_url(self):
        ...

class Item(models.Model):
    name = models.CharField(max_length=50, null=False)
    url = models.CharField(max_length=50, null=True)

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    item_previous = models.ForeignKey("Item", on_delete=models.CASCADE, null=True)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['name', 'menu', 'item_previous'],
            name='menu_item_unique')]

    def get_url(self):
        return
