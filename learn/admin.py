from django.contrib import admin
from .models import Register
# Register your models here.


class RegisterAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'designation']


admin.site.register(Register,RegisterAdmin)
