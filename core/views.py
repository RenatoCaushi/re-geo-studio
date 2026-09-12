from django.shortcuts import render
from services.models import Sherbimi
from projects.models import Projekti

def home(request):
    sherbimet = Sherbimi.objects.all()[:6]
    projektet = Projekti.objects.all().order_by('-data_perfundimit')[:6]
    
    context = {
        'sherbimet': sherbimet,
        'projektet': projektet,
    }
    return render(request, 'core/index.html', context)
