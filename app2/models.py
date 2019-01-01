from django.db import models

class Pessoal(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    bio = models.TextField(max_length=400)
    creation = models.TimeField(auto_now=True)
    photo = models.ImageField(upload_to='clientes_photos', null = True, blank=True) # o upload_to é onde a foto será salva
                                                                                    # ja o null e o blank permitem o campo em branco
    class Meta:
        verbose_name_plural = "Novas Pessoinhas"

    def __str__(self):
        return str(self.id) +" "+ self.first_name

