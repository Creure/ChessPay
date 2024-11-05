from django.shortcuts import render
from .models import UserProfile
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
import json


@login_required
def gui_update(request):
    if request.method == 'POST':
        # Obtener el perfil del usuario autenticado
        try:
            data = json.loads(request.body)
            state = data.get('state', 'default_value')
            user_profile = UserProfile.objects.get(user=request.user) 
        
            
            user_profile.gui = True if state == 'on' else False

            user_profile.save()
            return JsonResponse({'status': 'success'})

        except UserProfile.DoesNotExist:
            user_profile = UserProfile(user=request.user)
            user_profile.gui = True if state == 'on' else False

            user_profile.save()
            return JsonResponse({'status': 'success'}) 
            
        # Responder con éxito
    else:
        return JsonResponse({'status': '404'})   