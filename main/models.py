from django.db import models

class Animal(models.Model):
    SEXO_CHOICES = {
        "M": "Masculino",
        "F": "Feminino",
    }
    PORTE_CHOICES = {
        "MP": "Muito Pequeno",
        "P": "Pequeno",
        "M": "Médio",
        "G": "Grande",
        "MG": "Muito Grande",
    }

    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    especie = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    porte= models.CharField(max_length=2, choices=PORTE_CHOICES)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    descricao_animal = models.TextField(max_length=200, default="Sem Descrição.")

    def __str__(self):
        return f"{self.nome} ({self.especie})"

class Desaparecido(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    contato = models.CharField(max_length=50)
    data_desaparecimento = models.DateField()
    descricao_desaparecido = models.TextField()

    def __str__(self):
        return f"{self.animal}"
 
class Adocao(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    data_publicacao = models.DateField()
    @property
    def descricao_animal(self):
        return self.animal.descricao_animal
    
    def __str__(self):
        return f"{self.animal}"