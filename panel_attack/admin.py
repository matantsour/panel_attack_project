from django.contrib import admin
from django.apps import apps
from .models import Panel
# Register your models here.

class PanelAdmin(admin.ModelAdmin):
    model=Panel
    list_display = ['id','color']
admin.site.register(Panel)
#
# from django.apps import apps
#
# # model registered with custom admin
# admin.site.register(Panel)
# # all other models
# models = apps.get_models()
#
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass