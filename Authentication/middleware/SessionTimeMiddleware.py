from Authentication.models import AuthenticationTokenTime
from django.utils import timezone
from django.contrib.auth import logout

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware) are called.
        if request.user.is_authenticated and 'rT7gM2sP5qW8jN4' in request.session:
            try:
                data = AuthenticationTokenTime.objects.get(pk=request.session['rT7gM2sP5qW8jN4'])
                if data.valid_session:
                    if  timezone.now() > data.session_time :
                        data.valid_session = False
                        data.save()
                        logout(request)
                else:
                    request.session.pop('rT7gM2sP5qW8jN4'),
            except:
                logout(request)
            
        response = self.get_response(request)
        # Code to be executed for each request/response after the view is called.
        return response