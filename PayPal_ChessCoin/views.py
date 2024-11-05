from django.shortcuts import redirect
import paypalrestsdk
from paypalrestsdk import Payment, configure
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import PayPalTransaction
from .Nush_ChessCoin import NushChessCoin
from .NushCoders import ChessCoinEncription
from Authentication.models import User
import uuid, json
import hashlib
import pdb
from decimal import Decimal

paypalrestsdk.configure({
  "mode": settings.PAYPAL_MODE,  # "sandbox" o "live"
  "client_id": settings.PAYPAL_CLIENT_ID,
  "client_secret": settings.PAYPAL_CLIENT_SECRET
})



@login_required
def create_payment(request):    
    # 5,4% amount + 0,30 
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": request.build_absolute_uri('/paypal/execute/'),
            "cancel_url": request.build_absolute_uri('/paypal/cancel/')
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "Criptomoneda ChessCoin",
                    "sku": f"sku_{uuid.uuid4()}_{uuid.uuid4()}",
                    "price": f'{request.GET.get('quantity')}',
                    "currency": "USD",
                    "quantity": 1
                }]
            },
            "amount": {
                "total":  f'{request.GET.get('quantity')}' ,
                "currency": "USD"
            },
            "description": "Adquisición de Criptomoneda ChessCoin a Través del Sitio Web de ChessPay"
        }]
    })



    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                approval_url = str(link.href)
                return redirect(approval_url)
    else:
        return HttpResponse("Error al crear el pago")


@login_required
def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        transaction_data = payment.transactions[0]
        item_list = transaction_data.item_list

        
        amount = transaction_data.amount['total']
        currency = transaction_data.amount['currency']
        merchant_id = transaction_data.payee.merchant_id if transaction_data.payee else 'N/A'
        state = payment.state
        create_time = payment.create_time
        update_time = payment.update_time   
        data = f"{payment_id}{payer_id}{state}{amount}{currency}{merchant_id}"
        hash = hashlib.sha256(data.encode('utf-8')).hexdigest()
        __nush__ = NushChessCoin(hash, amount, payment_id, payer_id, merchant_id, transaction_data['item_list']['items'][0]['sku'], create_time, update_time)
        __encrypt__ = ChessCoinEncription(password=hash)
        user_profile = User.objects.get(pk=request.user.identification_number) 

        transacción_info = PayPalTransaction.objects.create(
            payment_id=payment_id,
            payer_id=payer_id,
            state=state,
            amount=amount,
            currency=currency,
            merchant_id=merchant_id,
            create_time=create_time,
            update_time=update_time,
            hash=hash,
            description=transaction_data['description'],
            ChessCoin_SKU=transaction_data['item_list']['items'][0]['sku'],
            Nush_ChessCoin = __encrypt__.encryption(f'{__nush__.split_ChessCoin()}'),
            identification_number = user_profile.identification_number
        )   
        
        
        user_profile.wallet += Decimal(__nush__.amount)
        user_profile.save()


        return redirect('/wallet/')
    else:
        return HttpResponse("Error en la ejecución del pago")


@login_required
def cancel_payment(request):
    return HttpResponse("El pago ha sido cancelado.")
