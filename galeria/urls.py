from django.urls import path
from galeria.views import index, imagem, buscar

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'), # essa instancia vai fazer assim: toda vez que a rota imagem/ for chamda ela vai renderizar tal coisa
    path("buscar", buscar, name="buscar"), # Rota para busca
]