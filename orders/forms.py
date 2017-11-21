from django import forms


class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)