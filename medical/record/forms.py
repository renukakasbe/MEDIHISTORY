from django import forms
from .models import Person
from .models import MedicalRecord

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ("name", "age", "bloodGroup", "gender")

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ("symptoms", "medicines", "membername")