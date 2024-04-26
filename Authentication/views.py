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
    return redirect('/login/')

def disabled(request):
    return render(request, 'disabled.html')

class Authentication(View):

    def get(self,request):
        if not request.user.is_authenticated:
            return render(request, 'login.html')
        else:
            return redirect('/')
    
    def post(self, request):
        auth = authenticate(username=request.POST['id_username'], password=request.POST['id_password'])

        if auth is not None:
            login(request, auth)

            try:
                data = AuthenticationTokenTime.objects.get(username=request.POST['id_username'], valid_session=True)
                token = data.token_auth
            except AuthenticationTokenTime.DoesNotExist:
                token = secrets.token_hex(256)
                AuthenticationTokenTime.objects.create(token_auth=token, username=request.POST['id_username'], last_login=timezone.now(), session_time=timezone.now() + timezone.timedelta(hours=24), valid_session=True, ip_address=request.META['REMOTE_ADDR'])

            request.session['rT7gM2sP5qW8jN4'] = token
            request.session['username'] = request.POST['id_username']
            return redirect('/')
        else:
            return render(request, 'login.html', {'auth': request.user.is_authenticated})



