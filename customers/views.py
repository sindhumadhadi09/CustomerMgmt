from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Customer

class IndexView(generic.ListView):
    template_name = 'customers/index.html'
    context_object_name = 'customers_list'

    def get_queryset(self):
        return Customer.objects.all()

class CustomerView(generic.TemplateView):
    template_name = 'customers/detail.html'

def add_customer(request):
    customer = Customer()
    customer.customer_firstname = request.POST['fname']
    customer.customer_lastname = request.POST['lname']
    customer.customer_address = request.POST['address']
    customer.customer_city = request.POST['city']
    customer.customer_zipcode = request.POST['zip']
    customer.customer_state = request.POST['state']
    customer.save()
    return HttpResponseRedirect(reverse('customers:index'))
    
def delete_customer(request, customer_id):
    p = Customer.objects.get(pk=customer_id)
    p.delete()
    return HttpResponseRedirect(reverse('customers:index'))