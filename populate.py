import os
import django
from django.core.files import File
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from services.models import Service, Project

def run():
    print("--> Po pastrohen të dhënat e vjetra...")
    Project.objects.all().delete()
    Service.objects.all().delete()

    print("--> Po krijohen 3 shërbimet dhe projektet kryesore...")

    base_img_path = os.path.join(settings.BASE_DIR, 'services', 'static', 'images')

    # 1. Shërbimi & Projekti 1
    s1 = Service.objects.create(
        titulli="Studime Hidrogjeologjike",
        pershkrimi_i_shkurter="Vlerësime profesionale të burimeve ujore dhe hidrogjeologjisë.",
        ikona_bootstrap="bi-droplet-half"
    )
    p1 = Project(
        service=s1,
        titulli="Studim Hidrogjeologjik",
        vendi="Tiranë",
        pershkrimi="Detaje dhe vlerësim për burimet ujore nëntokësore sipas standardeve inxhinierike."
    )
    path1 = os.path.join(base_img_path, 'Construction-soil-testing-scaled.jpg')
    if os.path.exists(path1):
        with open(path1, 'rb') as f:
            p1.imazhi_kryesor.save('Construction-soil-testing-scaled.jpg', File(f), save=False)
    p1.save()

    # 2. Shërbimi & Projekti 2
    s2 = Service.objects.create(
        titulli="Laborator Gjeoteknik",
        pershkrimi_i_shkurter="Analiza fiziko-mekanike të dherave dhe shkëmbinjve.",
        ikona_bootstrap="bi-diagram-3-fill"
    )
    p2 = Project(
        service=s2,
        titulli="Analiza Laboratorike",
        vendi="Durrës",
        pershkrimi="Testime të detajuara gjeoteknike për dherat, provat Proctor dhe CBR."
    )
    path2 = os.path.join(base_img_path, 'analiza.JPG')
    if os.path.exists(path2):
        with open(path2, 'rb') as f:
            p2.imazhi_kryesor.save('analiza.JPG', File(f), save=False)
    p2.save()

    # 3. Shërbimi & Projekti 3
    s3 = Service.objects.create(
        titulli="Shpime Gjeologo-Inxhinierike",
        pershkrimi_i_shkurter="Shpime karkotazhi dhe sondazhe me pajisje moderne.",
        ikona_bootstrap="bi-layers-fill"
    )
    p3 = Project(
        service=s3,
        titulli="Shpime Gjeologjike",
        vendi="Elbasan",
        pershkrimi="Sondazhe terreni dhe marrje kampionesh shkëmbore për vlerësim bazamenti."
    )
    path3 = os.path.join(base_img_path, 'drill.JPG')
    if os.path.exists(path3):
        with open(path3, 'rb') as f:
            p3.imazhi_kryesor.save('drill.JPG', File(f), save=False)
    p3.save()

    print("--> 3 Shërbimet dhe Projektet u krijuan me sukses!")

if __name__ == '__main__':
    run()