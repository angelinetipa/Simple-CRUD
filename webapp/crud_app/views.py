from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Customer_Record
from .forms import Add_Record

# Create your views here. Handles the logic for what happens when a user visits a page on your site.
def home(request):
    records = Customer_Record.objects.all() # retrieves all records from the Customer_Record model and stores them in the records variable
    if request.method == 'POST':
        username = request.POST['userName'] # extract the username and password from the submitted form data
        password = request.POST['passWord']
        # returns a user object if the credentials are valid, otherwise it returns None
        user =authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been Logged In!')
            return redirect('home')
        else:
            messages.warning(request, 'Wrong Username or Password, Please try again!')
            return redirect('home')
    return render(request, 'home.html', {'records':records}) # renders the ‘home.html’ template, passing the records variable to the template context

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been Logged Out!')
    return redirect('home')


def user_details(request, pk): #(pk - primary key) record.id passed to pk when the user clicks the button
    if request.user.is_authenticated:
        # look up record
        record_details = Customer_Record.objects.get(id=pk) # looks up the specific record in the Customer_Record table using the pk
        return render(request, 'details.html', {'record_details':record_details}) # renders the details.html template and dictionary passes the fetched record details to it
    else:
        messages.warning(request, 'You must be Logged In to view the page!')
        return redirect('home')
    
def user_delete(request, pk):
    if request.user.is_authenticated:
        # delete record
        del_record = Customer_Record.objects.get(id=pk)
        del_record.delete()
        messages.success(request, 'Customer Record Deleted Successfully!')
        return redirect('home')
    else:
        messages.warning(request, 'You must be Logged In to delete this Data!')
        return redirect('home')

def add_record(request):
    form = Add_Record(request.POST or None, request.FILES)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Record added successfully!')
                return redirect('home')
        else:
            return render(request, 'add.html',{'form':form})
    else:
        messages.warning(request, 'You must be Logged In to view the page!')
        return redirect('home')

def user_update(request, pk):
    if request.user.is_authenticated:
        current_record = Customer_Record.objects.get(id=pk)
        form = Add_Record(request.POST or None, request.FILES or None, instance=current_record)
        if form.is_valid():
            if form.has_changed():
                form.save()
                messages.success(request, 'Record Updated!')
                return redirect('home')
            else:
                messages.info(request, 'The record remain unchanged!')
                return redirect('details', pk=pk)
        return render(request, 'update.html',{'form':form})
    else:
        messages.warning(request, 'You must be Logged In to view the page!')
        return redirect('home')