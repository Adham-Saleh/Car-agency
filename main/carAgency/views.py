from django.shortcuts import render, redirect
from .models import Car, Client
from .forms import CreateCarForm, CreateClientForm
# Create your views here.

def carView(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    if request.method == 'GET':
        return render(request, 'base/cars.html', context)
    
def createCarView(request):
    form = CreateCarForm()
    if request.method == 'POST':
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'base/create.html', {'form': form})

def deleteCarView(request, id):
    if request.method == 'POST':
        try:
            car = Car.objects.get(id=id)
            car.delete()
            return redirect('home')
        except:
            return render(request, 'base/cars.html')

def getCarView(request, id):
    if request.method == 'GET':
        car = Car.objects.get(id=id)
        return render(request, 'base/singleCar.html', {'car': car})

def updateCarView(request, id):
    car = Car.objects.get(id=id)
    form = CreateCarForm(instance=car)
    if request.method == 'POST':
        form = CreateCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'base/updateForm.html', {'car': car, 'form': form})


def clientView(request):
    clients = Client.objects.all()
    return render(request, 'base/clients.html', {'clients': clients})

def createClientView(request):
    form = CreateClientForm()
    if request.method == 'POST':
        form = CreateClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients')
    return render(request, 'base/createClients.html', {'form': form})

def deleteClientView(request, id):
    if request.method == 'POST':
        try:
            car = Client.objects.get(id=id)
            car.delete()
            return redirect('clients')
        except:
            return render(request, 'base/cars.html')

def getClientView(request, id):
    try:
        client = Client.objects.get(id=id)
        print(client)
        return render(request, 'base/singleClientPage.html', {'client': client})
    except:
        return redirect('clients')
    
def updateClientView(request, id):
    client = Client.objects.get(id=id)
    form = CreateClientForm(instance=client)
    if request.method == 'POST':
        form = CreateClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients')
    return render(request, 'base/updateForm.html', {'form': form})