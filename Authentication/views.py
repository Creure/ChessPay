from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import View
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView


def logout_view(request):
    logout(request)
    return redirect('/')

def disabled(request):
    return render(request, 'disabled.html')
class Authentication(View):

    def get(self,request):
        if not request.user.is_authenticated:
            print(request.path)
            return render(request, 'login.html')
        else:
            return redirect('/')
    

    def post(self,request):

        auth = authenticate(username=request.POST['id_username'], password=request.POST['id_password'])

        if auth is not None:
            login(request, auth)
            request.session['auth'] = {}
            request.session['user'] = request.POST['id_username']
            return redirect('/')       
        else:
            return render(request, 'login.html', {'auth':request.user.is_authenticated})




