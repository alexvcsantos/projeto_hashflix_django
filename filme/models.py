from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
LISTA_CATEGORIAS = (
    ("ANALISES", "Análises"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
)


# criar o filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.BigIntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    # função para exibir no banco o titulo do filme ao inves do filme object (1)
    # função padrão do python para informar o que vai aparecer de der um print
    def __str__(self):
        return self.titulo


# criar os episodios
class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.filme.titulo + " - " + self.titulo
    

# sub classe do AbstractUser - já tem informações padroes do usuario
# obs: tem que adicionar no settings AUTH_USER_MODEL = "filme.Usuario"
class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")