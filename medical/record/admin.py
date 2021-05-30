from django.contrib import admin
from .models import Person
from .models import MedicalRecord


class PersonAdmin(admin.ModelAdmin):
    display=['name','age','bloodGroup','gender']

class MedicalRecordAdmin(admin.ModelAdmin):
        display = ['symptoms','medicines','membername']



admin.site.register(Person)

admin.site.register(MedicalRecord)

