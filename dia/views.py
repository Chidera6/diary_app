from django.shortcuts import render,redirect
from .models import Contents,Category
from .forms import ContentForm,CategoryForm
from django.shortcuts import render
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("dia:home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request,"dia/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect("dia:home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request,"dia/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("dia:home")

def home(request):
    if request.user.is_authenticated:
        categories = Category.objects.filter(user=request.user)
    else:
        categories = []
    return render(request, 'dia/base_category.html', {'categories': categories})
    

def show_category(request,id):
    get_category = Category.objects.get(id=id)
    return index(request,id)

def see_category(request):
    if request.user.is_authenticated:
        categories = Category.objects.filter(user=request.user)
    else:
        categories = []
    return render(request,"dia/show_category.html",context={"x":categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            add_category = form.save(commit=False)
            add_category.user = request.user
            add_category.save()
            messages.success(request, 'The post has been created successfully.')
            return home(request)
        else:
            messages.error(request, 'Please correct the following errors:')
    form = CategoryForm()
    form.fields['user'].queryset = User.objects.filter(username=request.user)
    context = {'form':form}
    return render(request, 'dia/create_category.html',context)

def delete_category(request, id):
    cat = Category.objects.get(id=id)
    cat.delete()
    return home(request)

def edit_category(request, id):
    if request.user.is_authenticated:
        obj = Category.objects.get(id=id)
        form = CategoryForm(request.POST or None, instance= obj)
        if form.is_valid():
            obj= form.save(commit= False)
            obj.save()
            context= {'form': form}
            return home(request)
        else:
            context= {'form': form}
        form.fields['user'].queryset = User.objects.filter(username=request.user)
        return render(request,'dia/edit_category.html' , context)

def index(request,id):
    category = Category.objects.get(id=id)
    all_contents = Contents.objects.filter(categories=category)
    context = {"cont":all_contents}
    return render (request,"dia/base.html",context)

def show(request,id):
    get_content = Contents.objects.get(id=id)
    context = {"con":get_content}
    return render(request,"dia/show.html",context)

def add_diary(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ContentForm(request.POST)
            if form.is_valid():
                add_diary = form.save(commit=False)
                add_diary.user = request.user
                add_diary.save()
                messages.success(request, 'The post has been created successfully.')
                return home(request)
        form = ContentForm()
        form.fields['categories'].queryset = Category.objects.filter(user=request.user)
        context = {'form':form}
        return render(request, 'dia/create.html',context)

def delete(request, id):
    content = Contents.objects.get(id=id)
    content.delete()
    return index(request,id)

def edit(request, id):
    obj = Contents.objects.get(id=id)
    form = ContentForm(request.POST or None,instance=obj)
    context= {'form': form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        context = {'form': form}
        messages.success(request, 'Post updated successfully')
        return home(request)
    else:
        context= {'form': form}
    form.fields['categories'].queryset = Category.objects.filter(user_id=request.user.id)
    return render(request,'dia/edit.html' , context)

        
