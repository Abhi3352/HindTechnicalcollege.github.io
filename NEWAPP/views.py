from django.shortcuts import render
from django.http import HttpResponse
from NEWAPP.models import Contact
from NEWAPP.models import Application
# Create your views here.
def boot(request):
    return render(request,'NEWAPP/boot.html')
def home(request):
    return render(request,'NEWAPP/home.html')
def contact(request):
   return render(request,'NEWAPP/contact.html')
def about(request):
    return render(request,'NEWAPP/about.html')

def cont(request):
        v1=request.POST['nm']
        v2=request.POST['cemail']
        v3=request.POST['phone']
        v4=request.POST['msgcont']
        fobj=Contact()
        fobj.name=v1
        fobj.cemail=v2
        fobj.phone=int(v3)
        fobj.msgcont=v4
        fobj.save()
        return HttpResponse('Thanks For Contact Us') 
############ This view for appication form
def application(request):
   return render(request,'NEWAPP/application.html')        
def appliform(request):
        v1=request.POST['fullname']
        v2=request.POST['dob']
        v3=request.POST['gender']
        v4=request.POST['email']
        v5=request.POST['ph1']
        v6=request.POST['categ']
        v7=request.POST['income']
        v8=request.POST['mothername']
        v9=request.POST['fathername']
        v10=request.POST['fatheroccu']
        v11=request.POST['ph2']
        v12=request.POST['email1']
        v13=request.POST['cadd']
        v14=request.POST['padd']
        v15=request.POST['boe']
        v16=request.POST['brn']
        v17=request.POST['yop']
        v18=request.POST['math']
        v19=request.POST['physics']
        v20=request.POST['chemistry']
        v21=request.POST['totalmarks']
        v22=request.POST['perc']
        v23=request.POST['coures1']
        fobj=Application()
        fobj.name=v1
        fobj.DOB=v2
        fobj.Gender=v3
        fobj.email=v4
        fobj.MobileNumber=v5
        fobj.Categery=v6
        fobj.income=v7
        fobj.MotherName=v8
        fobj.FatherName=v9
        fobj.FatherOccupation=v10
        fobj.AlternaterContactNo=v11
        fobj.Alternateemail=v12
        fobj.CorrespondingAddress=v13
        fobj.PermanentAddress=v14
        fobj.BoardOfEducation=v15
        fobj.BoardRollNo=v16
        fobj.YearOfPassing=v17
        fobj.Mathematics=v18
        fobj.Physics=v19
        fobj.Chemistry=v20
        fobj.Total=v21
        fobj.Percentage=v22
        fobj.Coures=v23
        fobj.save()
        return HttpResponse('YOur Form Succesfully Submitted')  
        return render(request,'NEWAPP/application.html')         


      