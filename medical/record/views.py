from django.shortcuts import render,redirect
from django.http import HttpResponse



from.models import Person
from.models import MedicalRecord
from.forms import PersonForm
from.forms import MedicalRecordForm

from django import views

# Create your views here.
def welcome(request):
    return render(request, "welcome.html")

def load_form(request):
    form = PersonForm
    return render(request, "index.html", {'form': form})

def add(request):
    form = PersonForm(request.POST)
    print("in add method ");
    print(form.data.values())
    form.save()
    person = Person.objects.all
    return render(request, "show.html", {'person':person})

def show(request):
    # we create a instance for model form we create photo copy of model form
    # to catch data objects.all()
    person =Person.objects.all
    print("in show method ")
    print(person)
    # we to show the details on show.html for that purpuse we write below code
    return render(request, 'show.html', {'person':person})


def addMedicalRecord(request):
    person = Person.objects.all
    return render(request, 'addMedicalRecord.html', {'person': person})

def saveMedicalRecord(request):
    form = MedicalRecordForm(request.POST)
    print("in add method ");
    print(form.data.values())
    form.save()
    medical = MedicalRecord.objects.all
    return render(request, "showMedicalRecord.html", {'medical':medical})

def viewMedicalRecords(request):
    # we create a instance for model form we create photo copy of model form
    # to catch data objects.all()
    medical = MedicalRecord.objects.all
    return render(request, "showMedicalRecord.html", {'medical': medical})



def delete_data(request,id):
    person=Person.objects.get(id=id)
    person.delete()
    return redirect("/show")


def delete_medicalRecord(request,id):
    medicalRecord=MedicalRecord.objects.get(id=id)
    medicalRecord.delete()
    return redirect("/viewMedicalRecords")




































































































