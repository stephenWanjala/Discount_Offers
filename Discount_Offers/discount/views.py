from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DiscountOfferForm
from .models import DiscountOffer

def discount_form_view(request):
    if request.method == 'POST':
        form = DiscountOfferForm(request.POST)
        if form.is_valid():
            account_number = form.cleaned_data['account_number']
            selected_discount = form.cleaned_data['discount_offer']

            # Fetch all discounts already applied for this account
            applied_discounts = list(DiscountOffer.objects.filter(
                account_number=account_number
            ).values_list('discount_offer', flat=True))
            
            # Define the required sequence of discounts
            required_sequence = ['50%', '25%', '10%']
            
            # Check if the sequence is violated
            for idx, discount in enumerate(applied_discounts):
                if discount != required_sequence[idx]:
                    messages.error(
                        request,
                        "Invalid discount application sequence. Please apply for the discounts in the order: 50%, then 25%, then 10%."
                    )
                    return redirect('discount_form')

            # Check if the selected discount matches the next in sequence
            next_discount = required_sequence[len(applied_discounts)] if len(applied_discounts) < 3 else None
            if selected_discount != next_discount:
                messages.error(
                    request,
                    f"Apply for the {next_discount} discount."
                )
                return redirect('discount_form')

            # Save the discount if the sequence is valid
            form.save()
            messages.success(request, f"{selected_discount} discount applied successfully!")
            return redirect('success', message=f"{selected_discount} discount applied successfully!")
    else:
        form = DiscountOfferForm()
    
    return render(request, 'discount_form.html', {'form': form})

def success_view(request, message):
    return render(request, 'success.html', {'message': message})
