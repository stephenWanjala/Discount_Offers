from django import forms
from .models import DiscountOffer
import re

class DiscountOfferForm(forms.ModelForm):
    class Meta:
        model = DiscountOffer
        fields = '__all__'
        widgets = {
            'date_processed': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_account_number(self):
        account_number = self.cleaned_data.get('account_number')

        # Ensure the account number starts with 'AfriQ'
        if not account_number.startswith("AfriQ"):
            raise forms.ValidationError("Account number must start with 'AfriQ'.")

        # Ensure the remaining part contains only integers
        remaining_part = account_number[5:]
        if not remaining_part.isdigit():
            raise forms.ValidationError("The part after 'AfriQ' must contain integers only.")
        
        return account_number
