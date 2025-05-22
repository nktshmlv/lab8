from django.contrib import admin
from .models import Client, Reason, Operator, Tag, Call

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'registration_date')

@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'hire_date')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
