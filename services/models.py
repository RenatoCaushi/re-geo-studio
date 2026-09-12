from django.db import models

class Sherbimi(models.Model):
    titulli = models.CharField(max_length=150, verbose_name="Titulli i Shërbimit")
    slug = models.SlugField(unique=True)
    ikona_bootstrap = models.CharField(max_length=50, default="bi-layers", help_text="Emri i ikonës nga Bootstrap Icons (p.sh. bi-geo-alt, bi-layers)")
    pershkrimi_i_shkurtër = models.TextField(max_length=300, verbose_name="Përshkrimi i Shkurtër")
    permbajtja_detajuar = models.TextField(verbose_name="Përmbajtja e Detajuar")
    imazhi = models.ImageField(upload_to='sherbimet/', blank=True, null=True)
    renditja = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Shërbim"
        verbose_name_plural = "Shërbimet"
        ordering = ['renditja']

    def __str__(self):
        return self.titulli
