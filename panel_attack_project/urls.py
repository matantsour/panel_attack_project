from django.contrib import admin
from django.urls import path
from panel_attack import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index.as_view(), name='index'),
    path('panel_attack/<int:panel_id>/', views.panel_detail, name='panel_detail'),
    path('panel_attack/reset_game',views.reset_game_click,name='reset_game')
]
