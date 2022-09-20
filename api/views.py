import os
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from django.http import Http404
from api.models import Item
from dotenv import load_dotenv
import stripe


load_dotenv()

stripe.api_key = os.getenv('STRIPE_KEY')
URL = os.getenv('URL')


@api_view(['GET'])
def get_info_item(request, *args, **kwargs):
    """Method for getting information about Item"""
    try:
        item = Item.objects.get(id=kwargs.get('id'))
        context = {'item': item}
        return render(request, 'info_item.html', context)
    except Item.DoesNotExist:
        raise Http404('Object not found')


@api_view(['GET', 'POST'])
def get_buy_id(request, *args, **kwargs):
    """Method for getting Stripe Session id for to pay for the selected Item"""
    item = Item.objects.get(id=kwargs['id'])
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                    'description': item.description
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=URL + '/success/',
        cancel_url=URL + '/cancel/',
    )
    return redirect(session.url, code=303)


@api_view(['GET', 'POST'])
def get_buy_order(request, *args, **kwargs):
    """Method for getting Stripe Session id for to pay for the selected Order"""
    items = Item.objects.filter(items__id=kwargs['id'])
    line_items = []
    for item in items:
        line_items.append({
            'price_data': {
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price,
                'currency': 'usd',
            },
            'quantity': 1,
        })
    session = stripe.checkout.Session.create(
        mode='payment',
        success_url=URL + '/success/',
        cancel_url=URL + '/cancel/',
        line_items=line_items,
    )
    return redirect(session.url, code=303)


class SuccessView(TemplateView):
    """The class to represent the template success.html"""
    template_name = 'success.html'


class CancelView(TemplateView):
    """The class to represent the template cancel.html"""
    template_name = 'cancel.html'
