from django.shortcuts import render

# Create your views here.


def home(request):
    
    data = {
        'nom': "Soro",
        'prenom': "nbe"
    }
    
    return render(request, 'index.html', data)


def about(request):
    
    return render(request, 'about.html')