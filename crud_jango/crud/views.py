from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import FormData
from .models import CrudData


# Create your views here.
def home(request):
    data=CrudData.objects.all()
    if data!=" ":
        return render(request,'index.html',{'datas':data})
    else:
        return render(request,'index.html')

def create_table(request):
    if request.method == "POST":
        errors={}
        form = FormData(request.POST)
        if form.is_valid():
            form.save()
            print("success")
            return redirect("home")
    else:
        form = FormData()
    return render(request, 'newtable.html', {'form':form})

def update_table(request,id):
    data = CrudData.objects.get(id=id)
    errors = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        degree = request.POST.get('degree')
        passed_out = request.POST.get('passed_out')
        if not name or len(name) < 3:
            errors['name'] = 'Name must be at least 3 characters long.'
        if not age or int(age) < 1:
            errors['age'] = 'Age must be greater than 0.'
        if not email:
            errors['email'] = 'Email is required.'
        if not degree:
            errors['degree'] = 'Degree is required.'
        if not passed_out:
            errors['passed_out'] = 'year is required.'
        if not errors:
            data.Name = name
            data.Age = age
            data.Email = email
            data.Degree = degree
            data.Passed_out = passed_out
            data.save()
            return redirect('home')
        else:
            return render(request, 'update.html', {'mydatas': data, 'errors': errors})
    return render(request, 'update.html',{'mydatas': data})
def delete_table(request,id):
    data=CrudData.objects.get(id=id)
    data.delete()
    return redirect("home")