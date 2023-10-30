from django.shortcuts import render

# Create your views here.
def white(request):
    return render(request, 'white.html')

def black(request):
    return render(request, 'black.html')