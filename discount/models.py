from django.db import models

class DiscountOffer(models.Model):
    account_number = models.CharField(max_length=255)
    discount_offer = models.CharField(max_length=10)
    ticket_number = models.CharField(max_length=10)
    region = models.CharField(max_length=50)
    date_processed = models.DateField()

    def __str__(self):
        return f"{self.account_number} - {self.discount_offer}"
