import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geo_studio.settings')
django.setup()

from services.models import Service, Project

def run():
    print("Po pastrohen të dhënat e vjetra...")
    Project.objects.all().delete()
    Service.objects.all().delete()

    print("Po krijohen 3 shërbimet dhe projektet kryesore...")

    # 1. Shërbimi 1
    s1 = Service.objects.create(
        title="Studime Hidrogjeologjike",
        description="Vlerësime profesionale të burimeve ujore dhe hidrogjeologjisë."
    )
    Project.objects.create(
        service=s1,
        title="Studim Hidrogjeologjik",
        description="Detaje dhe vlerësim për burimet ujore underground.",
        image="images/Construction-soil-testing-scaled.jpg"
    )

    # 2. Shërbimi 2
    s2 = Service.objects.create(
        title="Laborator Gjeoteknik",
        description="Analiza fiziko-mekanike të dherave dhe shkëmbinjve."
    )
    Project.objects.create(
        service=s2,
        title="Analiza Laboratorike",
        description="Testime të detajuara gjeoteknike për dherat.",
        image="images/analiza.JPG"
    )

    # 3. Shërbimi 3
    s3 = Service.objects.create(
        title="Shpime Gjeologo-Inxhinierike",
        description="Shpime karkotazhi dhe sondazhe me pajisje moderne."
    )
    Project.objects.create(
        service=s3,
        title="Shpime Gjeologjike",
        description="Sondazhe terreni dhe marrje kampionesh shkëmbore.",
        image="images/drill.JPG"
    )

    print("--> 3 Shërbimet dhe Projektet u krijuan me sukses!")

if __name__ == '__main__':
    run()