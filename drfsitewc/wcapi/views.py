import requests
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import WcapiSerializer

class WcapiAPIViewStatistics(APIView):
    def get(self, request):
        lst = Statistics.objects.all().values()
        return Response({'statistics': list(lst)})

    def post(self,request):
        post_new = Statistics.objects.create(
            user_id=request.data['user_id'],
            total_received=request.data['total_received'],
            number_of_transactions=request.data['number_of_transactions'],
        )
        return Response({'statistics_post': model_to_dict(post_new)})

    def put(self,request):
        data = Statistics.objects.get(user_id=request.data['user_id'])
        data.user_id, data.total_received, data.number_of_transactions = \
            request.data['user_id'],request.data['total_received'], request.data['number_of_transactions'],
        data.save()
        return Response({request.data['user_id']: 'edit'})

class WcapiAPIViewSettings(APIView):
    def get(self, request):
        lst = Settings.objects.all().values()
        return Response({'settings': list(lst)})

    def post(self,request):
        post_new = Settings.objects.create(
            user_id=request.data['user_id'],
            language=request.data['language'],
            main_currency=request.data['main_currency'],
        )
        return Response({'settings_post': model_to_dict(post_new)})

    def put(self,request):
        data = Settings.objects.get(user_id=request.data['user_id'])
        data.user_id, data.language, data.main_currency = \
            request.data['user_id'],request.data['language'], request.data['main_currency'],
        data.save()
        return Response({request.data['user_id']: 'edit'})

class WcapiAPIViewHistory(APIView):
    def get(self, request):
        lst = History.objects.all().values()
        return Response({'history': list(lst)})

    def post(self, request):
        post_new = History.objects.create(
            user_id=request.data['user_id'],
            payment_id=request.data['payment_id'],
            date_tranz=request.data['date_tranz'],
            value_tranz=request.data['value_tranz'],
        )
        return Response({'history_post': model_to_dict(post_new)})

    def put(self,request):
        data = History.objects.get(user_id=request.data['user_id'])
        data.payment_id, data.date_tranz, data.value_tranz = \
            request.data['payment_id'],request.data['date_tranz'], request.data['value_tranz'],
        data.save()
        return Response({request.data['user_id']: 'edit'})

class WcapiAPIViewQR(APIView):
    def post(self,request):
        tokens = "Uizbpp4RXQsfmuCk2zYSI4RFkD70SwftKfgyNhEjWyWr1YCv3wSd0pwdqQZ05yAz"
        post_data = {
                     "frame_name": "no-frame",
                     "qr_code_text": request.data['qr_code_text'],
                     "image_format": "SVG",
                     "qr_code_logo": "scan-me-square"
                    }
        response = requests.post(f'https://api.qr-code-generator.com/v1/create?access-token={tokens}', data=post_data)
        content = response.content
        return Response(content)

class WcapiAPIViewCheckLogin(APIView):
    def get(self, request):
        lst = Logins.objects.all().values()
        return Response({'logins': list(lst)})

    def post(self, request):
        post_new = Logins.objects.create(
            user_id=request.data['user_id'],
            login=request.data['login'],
            password=request.data['password'],
        )
        return Response({'login_post': model_to_dict(post_new)})

    def put(self,request):
        data = Logins.objects.get(user_id=request.data['user_id'])
        data.login, data.password = \
            request.data['login'],request.data['password']
        data.save()
        return Response({request.data['user_id']: 'edit'})


class WcapiAPIViewCheckAuth(APIView):
    def post(self, request):
        try:
            data = Logins.objects.get(user_id=request.data['user_id'],login=request.data['login'],password=request.data['password'])
            if data:
                return Response({'login': True})
            else:
                return Response({'login': False})
        except:
            return Response({'login': False})

class WcapiAPIViewCheckOrder(APIView):
    def post(self, request):
        ADDRESS = request.data['ADDRESS']
        COIN = request.data['COIN']
        url = f'https://api.blockchair.com/{COIN}/dashboards/address/{ADDRESS}'
        response = requests.get(url)

        if response.status_code == 200:
            try:
                data = response.json()
                received_value = data['data'][ADDRESS]['address']['received_usd']
                return Response({'ADDRESS': ADDRESS,
                                 'received_value': received_value,
                                 'COIN': COIN})
            except Exception as E:
                return Response({'error_p': f"{E}"})
        else:
            return Response({'error': response.status_code})

class WcapiAPIViewConvectorValut(APIView):
    def post(self, request):
        api_key = "A___nBsJDbXc1imJ45CjYox9BBTHbaZ8"
        COIN = request.data['COIN']
        usd_amount  = request.data['usd_amount']
        response = requests.get(f"https://api.blockchair.com/{COIN}/stats?apikey={api_key}")
        if response.status_code == 200:
            data = response.json()
            btc_price = data["data"]["market_price_usd"]

            # ?????????????????????????? 100 ???????????????? ?? BTC

            btc_amount = float(usd_amount) / btc_price

            return Response({COIN: btc_amount,
                             'usd_amount': usd_amount,
                             'COIN': COIN})
        else:
            return Response({'error': response.status_code})



