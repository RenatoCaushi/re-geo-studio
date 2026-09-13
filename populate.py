import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 're_geo_studio.settings') # vendos emrin e projektit tënd nëse është ndryshe
django.setup()

from core.models import Projekti, Sherbimi # ndrysho core sipas emrit të app-it tënd

# 1. Plotëso Shërbimet
sherbimet_data = [
    {
        "titulli": "Studime Gjeoteknike",
        "pershkrimi_i_shkurtër": "Vlerësim i kapacitetit mbajtës të trojeve për çdo lloj strukture ndërtimore.",
        "ikona_bootstrap": "bi-geo-alt"
    },
    {
        "titulli": "Hidrogjeologji",
        "pershkrimi_i_shkurtër": "Diagnostikim i akuiferëve, teste pompimi dhe vlerësim i ujërave nëntokësore.",
        "ikona_bootstrap": "bi-droplet"
    },
    {
        "titulli": "Testime Laboratorike",
        "pershkrimi_i_shkurtër": "Prova fiziko-mekanike mbi kampione dheu dhe gurësh sipas Eurokodit.",
        "ikona_bootstrap": "bi-layers"
    }
]

for s in sherbimet_data:
    Sherbimi.objects.update_or_create(
        titulli=s["titulli"],
        defaults=s
    )

# 2. Plotëso Projektet me emrat e imazheve te media/
projektet_data = [
    {
        "titulli": "Analizë Gjeoteknike Terreni",
        "vendi": "Tiranë",
        "pershkrimi": "Kryerja e provave të ngjeshjes dhe testimit të dheut sipas standardeve më të larta për ndërtim.",
        "imazhi_kryesor": "projektet/analiza.JPG"
    },
    {
        "titulli": "Shpime Hidrogjeologjike",
        "vendi": "Durrës",
        "pershkrimi": "Studim i thelluar i shtresave ujëmbajtëse dhe vlerësimi i burimeve nëntokësore.",
        "imazhi_kryesor": "projektet/drill.JPG"
    },
    {
        "titulli": "Testime Terreni & Laboratori",
        "vendi": "Elbasan",
        "pershkrimi": "Ekzekutim i provave CBR dhe Proctor për përgatitjen e infrastrukturës rrugore.",
        "imazhi_kryesor": "projektet/Construction-soil-testing-scaled.jpg"
    }
]

for p in projektet_data:
    Projekti.objects.update_or_create(
        titulli=p["titulli"],
        defaults=p
    )

print("Baza e të dhënave u popullua me sukses!")