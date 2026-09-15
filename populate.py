import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.apps import apps

# Gjen modelet automatikisht nga çdo aplikacion i regjistruar
all_models = {m.__name__.lower(): m for m in apps.get_models()}

# Kërkon për Service/Sherbimi dhe Project/Projekt
Service = all_models.get('service') or all_models.get('sherbimi')
Project = all_models.get('project') or all_models.get('projekt')

if not Service or not Project:
    print(f"Modelet e gjetura në sistem: {list(all_models.keys())}")
    raise Exception("Nuk u gjetën dot modelet e Service ose Project!")

def run():
    print("--> Po pastrohen të dhënat e vjetra...")
    Project.objects.all().delete()
    Service.objects.all().delete()

    print("--> Po krijohen 3 shërbimet dhe projektet kryesore...")

    # 1. Shërbimi & Projekti 1
    s1 = Service.objects.create(
        titulli="Studime Hidrogjeologjike",
        pershkrimi_i_shkurter="Vlerësime profesionale të burimeve ujore dhe hidrogjeologjisë.",
        ikona_bootstrap="bi-droplet-half"
    )
    Project.objects.create(
        service=s1,
        titulli="Studim Hidrogjeologjik",
        vendi="Tiranë",
        pershkrimi="Detaje dhe vlerësim për burimet ujore nëntokësore sipas standardeve inxhinierike.",
        imazhi_kryesor="images/Construction-soil-testing-scaled.jpg"
    )

    # 2. Shërbimi & Projekti 2
    s2 = Service.objects.create(
        titulli="Laborator Gjeoteknik",
        pershkrimi_i_shkurter="Analiza fiziko-mekanike të dherave dhe shkëmbinjve.",
        ikona_bootstrap="bi-diagram-3-fill"
    )
    Project.objects.create(
        service=s2,
        titulli="Analiza Laboratorike",
        vendi="Durrës",
        pershkrimi="Testime të detajuara gjeoteknike për dherat, provat Proctor dhe CBR.",
        imazhi_kryesor="images/analiza.JPG"
    )

    # 3. Shërbimi & Projekti 3
    s3 = Service.objects.create(
        titulli="Shpime Gjeologo-Inxhinierike",
        pershkrimi_i_shkurter="Shpime karkotazhi dhe sondazhe me pajisje moderne.",
        ikona_bootstrap="bi-layers-fill"
    )
    Project.objects.create(
        service=s3,
        titulli="Shpime Gjeologjike",
        vendi="Elbasan",
        pershkrimi="Sondazhe terreni dhe marrje kampionesh shkëmbore për vlerësim bazamenti.",
        imazhi_kryesor="images/drill.JPG"
    )

    print("--> 3 Shërbimet dhe Projektet u krijuan me sukses!")

if __name__ == '__main__':
    run()