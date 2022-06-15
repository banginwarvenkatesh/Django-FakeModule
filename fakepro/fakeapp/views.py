from django.shortcuts import render, redirect
from .models import Salesman
from faker import Faker

def ShowSalesman(request):
    template_name = 'fakeapp/show.html'
    obj = Salesman.objects.all()
    context = {'obj':obj}
    return render(request,template_name,context)

def FakeData(request):
    fake = Faker()
    for i in range(8):
        s = Salesman()

        s.name = fake.name()
        s.address = fake.address()
        s.email = fake.email()
        s.save()
    return redirect('show_url')

# Create your views here.
