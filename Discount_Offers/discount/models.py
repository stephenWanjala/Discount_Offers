from django.db import models

class DiscountOffer(models.Model):
    account_number = models.CharField(max_length=100)
    discount_offer = models.CharField(
        max_length=20,
        choices=[
            ('50%', '50% discount'),
            ('25%', '25% discount'),
            ('10%', '10% discount')
        ]
    )
    ticket_number = models.CharField(max_length=100)
    region = models.CharField(
        max_length=20,
        choices=[
            ('Nairobi', 'Nairobi'),
            ('Garissa', 'Garissa'),
            ('Wajir', 'Wajir')
        ]
    )
    date_processed = models.DateField()

    def __str__(self):
        return f"{self.account_number} - {self.discount_offer}"
