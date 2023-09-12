from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

# adicionar o campo novo da classe Usuario pra exibir no UserAdmin
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ('filmes_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Filme)
admin.site.register(Episodio)
# 1 parametro classe Usuario, 2 parametro UserAdmin do django que vai gerenciar o usuario
admin.site.register(Usuario, UserAdmin)