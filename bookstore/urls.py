from django.contrib import admin
from django.urls import path
from bookstore.views.response_view import ResponseView
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("response/", ResponseView.as_view(), name='response_list'),  # Ajustado para não causar recursão.
    path('', ResponseView.as_view(), name='home'),  # Padrão para a página inicial.
    path('api/async/', views.api_view.async_view),
    path('api/sync/', views.api_view.sync_view),
]
