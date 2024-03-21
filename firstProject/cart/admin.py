from django.contrib import admin
from.models import order,orderItem
# Register your models here.

class orderIteminline(admin.TabularInline):
    model=orderItem

class orderAdmin(admin.ModelAdmin):
    inlines=[orderIteminline]


admin.site.register(order,orderAdmin)
admin.site.register(orderItem)