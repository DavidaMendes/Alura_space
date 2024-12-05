from django.contrib import admin
from galeria.models import Fotografia

#Usando poder de admin para mostrar mais coisas no admin

class ListandoFotografias(admin.ModelAdmin):
    # Essa é listagem de fotografias, os metodos abaixo todos trabalham com a iinterface do admin
    list_display = ("id", "nome", "legenda", "publicada") # Esse Metodo mostra no dispaly
    list_display_links = ("id","nome") # Esse Metodo faz o acesso de link
    search_fields = ("nome",) # Esse Metodo pesquisa por nome
    list_filter = ("categoria","usuario") # Esse Metodo filtra por categoria
    list_editable =("publicada",) # Esse Metodo edita no dispaly
    list_per_page = 10 # Esse Metodo é o numero maximo de instancias na pagina do admin para criar outra

admin.site.register(Fotografia, ListandoFotografias)
# Regristo do banco de dados no nosso admin
