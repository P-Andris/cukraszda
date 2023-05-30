from django.db import models

class Kategoria(models.Model):
    kategoria_azon = models.AutoField(primary_key = True, editable = False)
    nev = models.CharField(max_length = 25, unique = True, verbose_name = 'Kategória neve')

    def __str__(self):
        return self.nev
    
class Edesseg(models.Model):
    edesseg_azon = models.AutoField(primary_key = True, editable = False)
    kategoria_azon = models.ForeignKey(Kategoria, on_delete = models.CASCADE, verbose_name = 'Kategória')
    nev = models.CharField(max_length = 60, verbose_name = 'Édesség neve')
    leiras = models.TextField(verbose_name = 'Leírás')
    ar = models.IntegerField(verbose_name = 'Ár (Ft)')
    kep_utvonal = models.CharField(max_length = 255, null = True, blank = True, verbose_name = 'Kép elérési útvonala')

    def __str__(self):
        return f'{self.edesseg_azon} | {self.nev}'