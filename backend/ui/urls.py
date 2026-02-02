from django.urls import path

from .views import (
    cadastro_dados_aventureiro,
    cadastro_ficha_medica,
    cadastro_lista_aventureiros,
    cadastro_revisao,
    cadastro_responsavel,
    cadastro_termo_imagem,
    cadastro_tipo,
    dashboard_generic,
    dashboard_responsavel,
    login_page,
)


urlpatterns = [
    path('', login_page, name='login'),
    path('cadastro-aventureiro/', cadastro_tipo, name='cadastro-aventureiro-tipo'),
    path('cadastro-aventureiro/responsavel/', cadastro_responsavel, name='cadastro-aventureiro-responsavel'),
    path('cadastro-aventureiro/aventureiros/', cadastro_lista_aventureiros, name='cadastro-aventureiro-lista'),
    path('cadastro-aventureiro/aventureiro/novo/', cadastro_dados_aventureiro, name='cadastro-aventureiro-dados-novo'),
    path('cadastro-aventureiro/aventureiro/<int:pk>/', cadastro_dados_aventureiro, name='cadastro-aventureiro-dados'),
    path('cadastro-aventureiro/aventureiro/<int:pk>/ficha/', cadastro_ficha_medica, name='cadastro-aventureiro-ficha'),
    path('cadastro-aventureiro/aventureiro/<int:pk>/termo/', cadastro_termo_imagem, name='cadastro-aventureiro-termo'),
    path('cadastro-aventureiro/revisao/', cadastro_revisao, name='cadastro-aventureiro-revisao'),
    path('dashboard/', dashboard_responsavel, name='dashboard-responsavel'),
    path('dashboard/generic/', dashboard_generic, name='dashboard-gen'),
]
