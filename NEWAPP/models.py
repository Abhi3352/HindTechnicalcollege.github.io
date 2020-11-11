from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    cemail=models.CharField(max_length=50)
    phone=models.IntegerField()
    msgcont=models.CharField(max_length=150)

class Application(models.Model):
    name=models.CharField(max_length=50)
    DOB=models.CharField(max_length=15)
    gender_choice=(
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )
    Gender=models.CharField(max_length=20,choices=gender_choice)
    email=models.CharField(max_length=50)
    MobileNumber=models.IntegerField()
    cate_choice=(
        ('General','General'),
        ('Obc','Obc'),
        ('Other','Other'),
    )
    Categery=models.CharField(max_length=20,choices=cate_choice)
    incom_choice=(
        ('Upto one lakh','Upto one lakh'),
        ('More than one lakh','More than one lakh'),
    )
    Income=models.CharField(max_length=20,choices=incom_choice)    
    MotherName=models.CharField(max_length=50)
    FatherName=models.CharField(max_length=50)
    FatherOccupation=models.CharField(max_length=50)
    AlternaterContactNo=models.IntegerField()
    Alternateemail=models.CharField(max_length=50)
    CorrespondingAddress=models.CharField(max_length=100)
    PermanentAddress=models.CharField(max_length=100)
    BoardOfEducation=models.CharField(max_length=50)
    BoardRollNo=models.CharField(max_length=15)
    YearOfPassing=models.CharField(max_length=4)
    Mathematics=models.CharField(max_length=8)
    Physics=models.CharField(max_length=8)
    Chemistry=models.CharField(max_length=8)
    Total=models.CharField(max_length=8)
    Percentage=models.CharField(max_length=8)
    coures_choice=(
        ('B.Tech(Electronics & communication Engineering(ECE))','B.Tech(Electronics & communication Engineering(ECE))'),
        ('B.Tech(Electrial & Electronics Engineering(EN))','B.Tech(Electrial & Electronics Engineering(EN))'),
        ('B.Tech(Mechanical Engineering(ME))','B.Tech(Mechanical Engineering(ME))'),
        ('B.Tech(Computer Science & Engineering(CSE))','B.Tech(Computer Science & Eng,ineering(CSE))'),
        ('B.Tech(Information Technology (IT))','B.Tech(Information Technology (IT))'),
        ('B.Tech(Civil Engineering(CE))','B.Tech(Civil Engineering(CE))'),
        ('B.Tech(Electrical Engineering(EE))','B.Tech(Electrical Engineering(EE))'),
        ('B.Pharma','B.Pharma'),
        ('D.Pharma','D.Pharma'),
    )
    Coures=models.CharField(max_length=100,choices=coures_choice)


 
         
        