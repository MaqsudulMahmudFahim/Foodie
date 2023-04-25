from django.contrib import admin
from myapp.models import Contact

# Register your models here.
admin.site.site_header ="FooDie | Admin"


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','message','added_on','is_approved']

admin.site.register(Contact, ContactAdmin)