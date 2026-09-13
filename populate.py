import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from services.models import Sherbimi
from projects.models import Projekti

# 1. Popullo Shërbimet
sherbimet_data = [
    {
        "titulli": "Studime Gjeoteknike",
        "pershkrimi_i_shkurtër": "Vlerësim i trojeve të ndërtimit, analizë e aftësisë mbajtëse dhe teste dinamike sipas Eurokodit 7.",
        "ikona_bootstrap": "bi-layers-fill"
    },
    {
        "titulli": "Studime Hidrogjeologjike",
        "pershkrimi_i_shkurtër": "Kërkim i ujërave nëntokësore, shpime puseve, teste pompimi dhe vlerësim i akuiferëve.",
        "ikona_bootstrap": "bi-droplet-half"
    },
    {
        "titulli": "Laborator Gjeoteknik",
        "pershkrimi_i_shkurtër": "Testime fiziko-mekanike të dheut dhe gurit, provat Proctor, CBR dhe analiza granulometrike.",
        "ikona_bootstrap": "bi-diagram-3-fill"
    }
]

for s in sherbimet_data:
    Sherbimi.objects.get_or_create(
        titulli=s["titulli"],
        defaults=s
    )

# 2. Popullo Projektet
projektet_data = [
    {
        "titulli": "Analizë Gjeoteknike Terreni",
        "vendi": "Tiranë",
        "pershkrimi": "Kryerja e provave të ngjeshjes dhe testimit të dheut sipas standardeve më të larta për ndërtim.",
        "imazhi_kryesor": "images/analiza.JPG"
    },
    {
        "titulli": "Shpime Hidrogjeologjike",
        "vendi": "Durrës",
        "pershkrimi": "Studim i thelluar i shtresave ujëmbajtëse dhe vlerësimi i burimeve nëntokësore.",
        "imazhi_kryesor": "images/drill.JPG"
    },
    {
        "titulli": "Testime Terreni & Laboratori",
        "vendi": "Elbasan",
        "pershkrimi": "Ekzekutim i provave CBR dhe Proctor për përgatitjen e infrastrukturës rrugore.",
        "imazhi_kryesor": "images/Construction-soil-testing-scaled.jpg"
    }
]

for p in projektet_data:
    Projekti.objects.get_or_create(
        titulli=p["titulli"],
        defaults=p
    )

print("Popullimi përfundoi me sukses!")