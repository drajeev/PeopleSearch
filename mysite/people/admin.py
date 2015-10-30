from django.contrib import admin
from people.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    def name(self, obj):
        return str(obj)
    name.short_description = 'Name'

    def image_view(self, obj):
        if obj.image:
           return '<img src="{url}" alt="{name}" width="200px">'.format(url=obj.image.url, name=obj.image.name)
        return ''
    image_view.short_description = 'Profile Picture'
    image_view.allow_tags = True

    list_display = ['name', 'seating_location', 'extn_no', 'image_view']

admin.site.register(Employee, EmployeeAdmin)
