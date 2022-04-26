from email import message
from django.shortcuts import render,redirect
from .forms import UserImage
from .models import UploadImage
from .utils import demo
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,'home.html')
def contact(request):
    print(request.POST)
    return render(request,'contact.html')
def upload(request):  
    if request.method == 'POST':  
        form = UserImage(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
            img_object = form.instance  
            driving = demo(f".{img_object.driving.url}")
            print(driving)
            if driving!="driving":
                messages.error(request,"Not a Driving Image. Please upload valid image.")
                return render(request,"upload.html")
            pancard = demo(f".{img_object.pancard.url}")  
            print(pancard)
            if pancard != "pancard":
                messages.error(request,"Not a Pancard Image. Please upload valid image.")
                return render(request,"upload.html")
            cheque = demo(f".{img_object.cheque.url}") 
            print(cheque) 
            if cheque!="chequebook":
                messages.error(request,"Not a Cheque Image. Please upload valid image.")
                return render(request,"upload.html")
            salary = demo(f".{img_object.salaryslip.url}")  
            print(salary)
            if salary!="salary_slip":
                messages.error(request,"Not a Salary Slip Image. Please upload valid image.")
                return render(request,"upload.html")
        
            messages.error(request,"Image Classified Successfully.")    
            return render(request, 'upload.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = UserImage()
    return render(request, 'upload.html', {'form': form})  