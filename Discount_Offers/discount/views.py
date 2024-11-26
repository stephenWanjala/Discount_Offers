from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DiscountOfferForm
from .models import DiscountOffer
from django.http import FileResponse, HttpResponseNotFound
import os
from .utils import export_db_to_excel

from django.http import FileResponse, HttpResponseNotFound
import os
from .utils import export_db_to_excel

def download_db_as_excel(request):
    """Export the SQLite database to an Excel file and serve it for download."""
    db_path = r"C:\Users\HomePC\Desktop\Discount\Discount_Offers\db.sqlite3"  # Path to your SQLite database
    excel_path = r"C:\Users\HomePC\Desktop\Discount\Discount_Offers\database_export.xlsx"  # Temporary Excel file

    # Ensure the database exists
    if not os.path.exists(db_path):
        return HttpResponseNotFound('<h1>Database not found</h1>')

    # Export the database to Excel
    export_db_to_excel(db_path, excel_path)

    # Serve the Excel file as a download
    return FileResponse(open(excel_path, 'rb'), as_attachment=True, filename='database_export.xlsx')

def discount_form_view(request):
    if request.method == 'POST':
        form = DiscountOfferForm(request.POST)
        if form.is_valid():
            account_number = form.cleaned_data['account_number']
            discount_offer = form.cleaned_data['discount_offer']
            ticket_number = form.cleaned_data['ticket_number']
            region = form.cleaned_data['region']
            date_processed = form.cleaned_data['date_processed']

            # Save the validated data to the database
            DiscountOffer.objects.create(
                account_number=account_number,
                discount_offer=discount_offer,
                ticket_number=ticket_number,
                region=region,
                date_processed=date_processed
            )

            # Show success message
            messages.success(request, f"Discount {discount_offer} applied successfully!")
            return redirect('success')
    else:
        form = DiscountOfferForm()

    return render(request, 'discount_form.html', {'form': form})

def success_view(request):
    """Renders the success page."""
    return render(request, 'success.html')