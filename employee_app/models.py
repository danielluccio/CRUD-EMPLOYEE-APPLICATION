from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name="Titulo")

    class Meta:
        verbose_name_plural = 'Positions'

    def __str__(self):
        return self.title
    
class Employee(models.Model):
    full_name = models.CharField(max_length=150, blank=False, null=False, verbose_name='Nome Completo')
    emp_code = models.CharField(max_length=3, blank=False, null=False, verbose_name="Código do Funcionário")
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.full_name