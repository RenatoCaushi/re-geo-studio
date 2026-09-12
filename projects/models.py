from django.db import models

class Projekti(models.Model):
    titulli = models.CharField(max_length=200, verbose_name="Titulli i Projektit")
    slug = models.SlugField(unique=True)
    klienti = models.CharField(max_length=150, blank=True, verbose_name="Klienti")
    vendi = models.CharField(max_length=100, verbose_name="Vendndodhja (Qyteti/Zona)")
    
    # Koordinatat për hartën interaktive
    latitude = models.FloatField(blank=True, null=True, verbose_name="Gjerësia Gjeografike (Latitude)")
    longitude = models.FloatField(blank=True, null=True, verbose_name="Gjatësia Gjeografike (Longitude)")
    
    pershkrimi = models.TextField(verbose_name="Përshkrimi i Projektit")
    imazhi_kryesor = models.ImageField(upload_to='projektet/', verbose_name="Imazhi Kryesor")
    data_perfundimit = models.DateField(verbose_name="Data e Përfundimit")

    class Meta:
        verbose_name = "Projekt"
        verbose_name_plural = "Projektet"

    def __str__(self):
        return self.titulli
