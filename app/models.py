from django.db import models

class CartItem(models.Model):
    item_id = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"Item ID: {self.item_id}, Quantity: {self.quantity}"
