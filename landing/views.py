from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *

# Create your views here.
def landing(request):
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        new_form = form.save()
    return render(request, 'landing/landing.html', locals())


def home(request):
    products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_phone = products.filter(product__category__id=1)
    products_laptop = products.filter(product__category__id=2)
    return render(request, 'landing/home.html', locals())