import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
from services.models import Sherbimi
from projects.models import Projekti

User = get_user_model()

def populate():
   # 1. Krijimi ose Ndryshimi i Fjalëkalimit për Superuser
    username = "Geologyrenni"
    email = "ren.caushi22@gmail.com"
    password = "renatoing"  # Vendos fjalëkalimin tënd të ri këtu

    user, created = User.objects.get_or_create(username=username, defaults={'email': email})
    user.set_password(password)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    print(f"Fjalekalimi per '{username}' u perditesua me sukses!")

    # 2. Sherbimet
    sherbimet = [
        {
            "titulli": "Studime Gjeoteknike",
            "slug": "studime-gjeoteknike",
            "ikona_bootstrap": "bi-layers-half",
            "pershkrimi_i_shkurtër": "Vlerësim i kapacitetit mbajtës të trojeve, shpime inxhinierike dhe analiza laboratorike për ndërtim.",
            "permbajtja_detajuar": "Shërbimi ynë i studimeve gjeoteknike përfshin punime të plota në terren dhe laborator."
        },
        {
            "titulli": "Kërkime Hidrogjeologjike",
            "slug": "kerkime-hidrogjeologjike",
            "ikona_bootstrap": "bi-droplet-half",
            "pershkrimi_i_shkurtër": "Zbulim dhe vlerësim i burimeve ujore nëntokësore, shpime pusesh dhe teste pompimi.",
            "permbajtja_detajuar": "Realizojmë studime të detajuara hidrogjeologjike për gjetjen e ujit nëntokësor."
        },
        {
            "titulli": "Konsulencë & Monitorim Gjeoteknik",
            "slug": "konsulence-monitorim-gjeoteknik",
            "ikona_bootstrap": "bi-shield-check",
            "pershkrimi_i_shkurtër": "Monitorim stabiliteti i shpateve, skratave dhe asistencë teknike gjatë punimeve gërmuese.",
            "permbajtja_detajuar": "Ofrojmë asistencë teknike dhe monitorim të vazhdueshëm inxhinierik."
        }
    ]

    for item in sherbimet:
        Sherbimi.objects.get_or_create(slug=item["slug"], defaults=item)

    # 3. Projektet
    projektet = [
        {
            "titulli": "Studim Gjeoteknik për Rezidencë Banimi",
            "slug": "studim-gjeoteknik-per-rezidence-banimi",
            "klienti": "Ndërtimi SHPK",
            "vendi": "Tiranë",
            "pershkrimi": "Studim i plotë terreni për bazamentin e një godine 10-katëshe.",
            "imazhi_kryesor": "projektet/Construction-soil-testing-scaled.jpg",
            "data_perfundimit": "2026-09-12"
        },
        {
            "titulli": "Shpim Pusi dhe Vlerësim Akuiferi",
            "slug": "shpim-pusi-dhe-vleresim-akuiferi",
            "klienti": "Kompleksi Agro-Turistik",
            "vendi": "Durrës",
            "pershkrimi": "Realizim shpimi hidrogjeologjik në thellësi 120m, teste pompimi.",
            "imazhi_kryesor": "projektet/drill.JPG",
            "data_perfundimit": "2026-09-12"
        },
        {
            "titulli": "Testime Laboratorike të Avancuara për Infrastrukturë Rrugore",
            "slug": "testime-laboratorike-te-avancuara-per-infrastruktu",
            "klienti": "Lab-Geo & Construction",
            "vendi": "Elbasan",
            "pershkrimi": "Testime të detajuara laboratorike për kampionë guri dhe dheu.",
            "imazhi_kryesor": "projektet/analiza.JPG",
            "data_perfundimit": "2026-09-12"
        }
    ]

    for item in projektet:
        Projekti.objects.get_or_create(slug=item["slug"], defaults=item)

if __name__ == '__main__':
    populate()