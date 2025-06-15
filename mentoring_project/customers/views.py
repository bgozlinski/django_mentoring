from django.contrib import messages
from django.shortcuts import redirect, render

from .models import Customer


def produce_consumer(request):
    if request.method == 'POST':
        customer = Customer.objects.create(name=f"Customer {Customer.objects.count() + 1}")
        messages.success(request, f'New customers "{customer.name}" created with basket!')
        return redirect('produce_customer')

    customers = Customer.objects.all()
    return render(request, 'customers/produce_customer.html', {'customers': customers})