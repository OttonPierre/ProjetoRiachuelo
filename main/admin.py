from django.contrib import admin
from .models import Animal, Desaparecido, Adocao

# Registro simples dos modelos
admin.site.register(Animal)
admin.site.register(Desaparecido)
admin.site.register(Adocao)
