from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import View
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from Authentication.models import AuthenticationTokenTime
from django.utils import timezone
import secrets

def logout_view(request):
    logout(request)
    return redirect('/')

def disabled(request):
    return render(request, 'disabled.html')

class Authentication(View):

    def get(self,request):
        if not request.user.is_authenticated:
            return render(request, 'login.html')
        else:
            return redirect('/')
    

    def post(self,request):

        auth = authenticate(username=request.POST['id_username'], password=request.POST['id_password'])

        if auth is not None:
            login(request, auth)
            token = secrets.token_hex(256)
            request.session['auth'] = {}
            request.session['user'] = request.POST['id_username']
            request.session['rT7gM2sP5qW8jN4'] = token
            data = AuthenticationTokenTime(token_auth=token, username=request.POST['id_username'], last_login=timezone.now(), session_time=timezone.now() + timezone.timedelta(hours=2), valid_session=True, ip_address=request.META['REMOTE_ADDR']).save()
            return redirect('/')       
        else:
            return render(request, 'login.html', {'auth':request.user.is_authenticated})




