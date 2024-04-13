from django.shortcuts import render

# Create your views here.
def white(request):
    return render(request, 'white.html', {'id': 'dc724af18fbdd4e59189f5fe768a5f8311527050d9b8a52c989f6e7f085e8b90'})

def black(request):
    return render(request, 'black.html', {'id': '32523caacfbc25d536b7e7ccbc7e3e97baf4b9e38fc43d229de3da54c36e7a4b'})