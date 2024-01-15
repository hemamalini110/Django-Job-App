from django.contrib import admin
from .models import models, Form


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name" , "last_name" , "email")
    search_fields = ("first_name" , "last_name" , "email")
    list_filter = ("date" , "occupation")
    ordering = ("-first_name",)  # order reverse
    readonly_fields = ("occupation",) #can not change


admin.site.register(Form , FormAdmin)
