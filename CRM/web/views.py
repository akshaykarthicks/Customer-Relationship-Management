from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login,authenticate,logout 
from django.contrib import messages
from .models import Record  


# Create your views here.
def home(request):
    records=Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request, username=username, password=password)
        #login user
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('home')
      
    else:
        return render(request, 'home.html',{'records':records})



def logout_user(request):
    logout(request)
    messages.success(request, 'Logout successful')
    return redirect('home')


def c_record(request,pk):
    if request.user.is_authenticated:
        c_r=Record.objects.get(id=pk)  
        return render(request, 'c_record.html',{'c_r':c_r})  
    
    else:
        messages.error(request, 'You must be logged in to view this page')
        return redirect('home')

def delete_record(request,pk):
    if request.user.is_authenticated:
        c_r=Record.objects.get(id=pk)  
        c_r.delete()
        messages.success(request, 'Record deleted successfully')
        return redirect('home')
    
    else:
        messages.error(request, 'You must be logged in to view this page')
        return redirect('home')
    
def add_record(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name=request.POST['name']
            age=request.POST['age']
            email=request.POST['email']
            phone=request.POST['phone']
            address=request.POST['address']
            
            Record.objects.create(name=name,age=age,email=email,phone=phone,address=address)
            messages.success(request, 'Record added successfully')
            return redirect('home')
        else:
            return render(request, 'add_record.html')
    else:
        messages.error(request, 'You must be logged in to view this page')
        return redirect('home')



def update_record(request,pk):
    if request.user.is_authenticated:
        c_r=Record.objects.get(id=pk)
        if request.method=='POST':
            c_r.name=request.POST['name']
            c_r.age=request.POST['age']
            c_r.email=request.POST['email']
            c_r.phone=request.POST['phone']
            c_r.address=request.POST['address']
            c_r.save()
            messages.success(request, 'Record updated successfully')
            return redirect('home')
        else:
            return render(request, 'update_record.html',{'c_r':c_r})
    
    else:
        messages.error(request, 'You must be logged in to view this page')
        return redirect('home')

