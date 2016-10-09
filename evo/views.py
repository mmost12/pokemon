from django.shortcuts import render
from django.http import HttpResponseRedirect

app_name = 'evo'
# Create your views here.
def index(request):
    if request.method == 'POST':
        return HttpResponseRedirect('evo/')
    else:
        return render(request, 'evo/index.html', {})

def evo(request):
    return render(request, 'evo/evo.html', {})
