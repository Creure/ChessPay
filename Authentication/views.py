from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import View
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from Authentication.models import AuthenticationTokenTime
from django.utils import timezone
from Authentication.models import User 
from UserInformationManager.models import UserProfile
from django.db import IntegrityError
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
                data.valid_session = False
                data.save()
                token = request.COOKIES.get('csrftoken', '')
                request.session['rT7gM2sP5qW8jN4'] = token
                AuthenticationTokenTime.objects.create(token_auth=token, username=request.POST['id_username'], last_login=timezone.now(), session_time=timezone.now() + timezone.timedelta(hours=24), valid_session=True, ip_address=request.META['REMOTE_ADDR'])

            except AuthenticationTokenTime.DoesNotExist:
                token = request.COOKIES.get('csrftoken', '')
                request.session['rT7gM2sP5qW8jN4'] = token
                AuthenticationTokenTime.objects.create(token_auth=token, username=request.POST['id_username'], last_login=timezone.now(), session_time=timezone.now() + timezone.timedelta(hours=24), valid_session=True, ip_address=request.META['REMOTE_ADDR'])
            
            request.session['username'] = request.POST['id_username']
            return redirect('/wallet/')
        else:
            return render(request, 'login.html', {'auth': request.user.is_authenticated})







class Registration(View):

    def get(self,request):
        if not request.user.is_authenticated:
            return render(request, 'register.html')
        else:
            return redirect('/')
    
    def post(self, request):
        try:
            user = User(
            username=request.POST['username'],
            identification_number=request.POST['cedula'],
            wallet=0.00,
            email=request.POST['email'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            
            phone_number='+123456789',
            id_history=[{"event": "registered", "date": "2024-09-01"}]
            )
            user.set_password(request.POST['password'])

            user.save()
            User_Profile = UserProfile(user=user).save()

            
            return redirect('/login/')
        except IntegrityError as e:
            if 'duplicate key value violates unique constraint' in str(e):
                return render(request, 'Register.html', {'error': "Error: Clave primaria duplicada."})
            else:
                print("Error de integridad:", e)
            

