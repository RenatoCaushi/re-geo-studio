from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
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

def fix_admin(request):
    User = get_user_model()
    user, created = User.objects.get_or_create(username='Geologyrenni')
    user.set_password('otanerstudio')
    user.is_superuser = True
    user.is_staff = True
    user.is_active = True
    user.save()
    return HttpResponse("Superuser Geologyrenni u rregullua me sukses! Tani mund te kyçesh te /admin/.")
