from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import Customer_Form,PicknDropForm, CreateUserForm
from .models import Car, Customer, Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .filters import Carfilter 
# Create your views here.


def home(request):
  return render( request,'base/home.html')

def bookdetails(request, id):
  car = Car.objects.all()
  customer = Car.objects.get(id = id)
  try:
      current_customer = Customer.objects.get(car_user_id=customer.id)
  except Customer.DoesNotExist:
    current_customer = None

  form = Customer_Form()
  form2 = PicknDropForm()
  if request.method == 'POST':
    form = Customer_Form(request.POST)
    form2 = PicknDropForm(request.POST)
    if form.is_valid() and form2.is_valid():
      
     instance = form.save(commit = False) 
     instance.car_user = customer
     instance.save()
     customer.status = "Pending"
     customer.save()

     instance2 = form2.save(commit=False)
     instance2.customer_booking_id = instance.id
     instance2.save()
     return redirect('receipt',id = instance2.customer_booking_id)
    else:
      print(form.errors)
      print(form2.errors)
  context = {'form':form,'form2':form2, 'car':car,'current_customer':current_customer}
  return render(request, 'base/bookdetails.html', context)

def listcars(request):
  car = Car.objects.all()

  myFilter = Carfilter(request.GET, queryset=car)
  car = myFilter.qs

  context = {'car':car,'myFilter': myFilter}
  return render(request, 'base/listcars.html', context)

def receipt(request, id):
  car = Car.objects.all()
  customer = Customer.objects.get(id = id)
  custom_booking = Booking.objects.get(customer_booking_id=customer.id)
 
  context = {'customer':customer, 'car':car, 'custom_booking':custom_booking}
  return render(request, 'base/receipt.html', context)

def initialreceipt(request):

  return render(request, 'base/receipt.html')

def about(request):
  return render(request, 'base/about.html')

def adminview(request):
  customer = Customer.objects.all()
  car = Car.objects.all()
  context = {'customer':customer, 'car':car}
  return render(request, 'base/adminview.html', context)

@login_required(login_url='login')
def adminview(request):
  customer = Customer.objects.all()
  car = Car.objects.all()
  context = {'customer':customer, 'car':car}
  return render(request, 'base/adminview.html', context)

def loginPage(request):
  if request.user.is_authenticated:
       return redirect('home')
  else:
      if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')

          user = authenticate(request, username=username, password=password)

          if user is not None:
              login(request, user)
              return redirect('adminview')
          else: 
              messages.info(request, 'Username or password is incorrect')


  context = {}
  return render(request, 'base/login.html', context)

def logoutUser(request):
  logout(request)
  return redirect('login')


def register(request):
  if request.user.is_authenticated:
      return redirect('home')
  else:
      form = CreateUserForm()

      if request.method == 'POST':
          form = CreateUserForm(request.POST)
          if form.is_valid():
              form.save()
              user = form.cleaned_data.get('username')
              messages.success(request, 'Account was created for' + user)

              return redirect('login')

  context = {'form':form}
  return render(request, 'base/register.html', context)

def newupdate(request, id):
  car = Car.objects.all()
  customer = Customer.objects.get(id = id)
  booking = Booking.objects.get(customer_booking_id = id)
  form = Customer_Form()
  form2 = PicknDropForm()
  if request.method =="POST":
    form = Customer_Form(request.POST, instance = customer)
    form2 = PicknDropForm(request.POST, instance = booking)


    if form.is_valid():

      form.save()
    
    if form2.is_valid():
      
      form2.save()
    else:
      print(form.errors)
      print(form2.errors)
      return redirect('/adminview')



  context = {'form':form,'customer':customer, 'form2':form2, 'booking': booking, 'car':car}
  return render(request, 'base/newupdate.html', context)

def delete(request, id):  

  booking = Booking.objects.get(id = id)
  print(booking.customer_booking.Name)
  if request.method == "POST":

    booking.delete()

    return redirect ('adminview')

  context = {'booking': booking}
  return render(request, 'delete.html', context)
  
def confirm(request, id):

    car = Car.objects.get(id = id)
    car.status = "Approved!"
    car.save()
    return redirect ('adminview')

def turnin(request, id):

    car = Car.objects.get(id = id)
    car.status = None
    car.save()
    return redirect ('adminview')