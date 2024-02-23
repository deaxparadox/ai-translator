from django.contrib import admin

from app.models import LTSAPIToken

@admin.register(LTSAPIToken)
class LTSAdminMode(admin.ModelAdmin):
    pass