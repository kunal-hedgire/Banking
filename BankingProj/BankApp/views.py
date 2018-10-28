from django.shortcuts import render,redirect
from BankApp.forms import RegisterForm,LoginForm,Account_Register,Account_Info,Insurance_Register,Loan_Register
from BankApp.models import Login,Register
from BankApp.Image_Upload.upload import handle_uploaded_file
from django.contrib.auth import authenticate
import requests

def login(request):

    if request.method=="POST":

        lform = LoginForm(request.POST)

        username = request.POST['userName']
        Password = request.POST['password']
        user = Register.objects.filter(userName=username)
        print(user[0].password)

        password = user[0].password

        print(Password)
        if password == Password:
             return redirect('/show',{'name':request.POST['userName']})
        
        else:
            lform=LoginForm()
            return render(request, 'Login.html',{'form':lform})

    else:
        lform = LoginForm()
        return render(request,'Login.html',{'form':lform})


def register(request):
    if request.method == "POST":
        sform = RegisterForm(request.POST, request.FILES)
        #print(sform)
        if sform.is_valid(): #validation
            userObj = sform.cleaned_data
            username = userObj['userName']
            if not (Register.objects.filter(userName=username).exists()):
                Register.objects.all()
                handle_uploaded_file(request.FILES['imgfile'])
                sform.save()
                #response=requests.post('api',data=request.POST)
                return redirect('/signin')

            else:
                #sform = RegisterForm()
                return render(request, 'register.html', {'form': sform})


    else:
        sform = RegisterForm()
        return render(request,'register.html',{'form':sform})

def DiffAcc(request):

    return render(request,'show.html')


def Acc_Register(request):
    if request.method =='POST':
        rform = Account_Register(request.POST)
        if rform.is_valid():
            #resposne = requests.post("API", data=request.POST)
            return render(request, 'show.html')

    else:
        rform=Account_Register()
        return render(request,'Acc_Register.html',{'form':rform})

def Acc_Info(request):
    sform=Account_Info()
    return render(request, 'Single.html',{'form':sform})

def Acc_Get(request):
        if request.method == 'GET':
            ide = request.GET['id']
            print(ide)
            # uriget=
            #response = requests.get("API ID?ACCNO-->{}".format(ide))
            #getid = response.json()
            #print(getid)
            #return render(request, 'Single.html', {'mylist': getid})

            return render(request, 'Single.html',{'mylist':ide})
        else:
            ide = request.GET['id']
            return render(request, 'Single.html', {'mylist': ide})

def Acc_Get_details(request):
    pass


def Insurance_Info(request):
    if request.method == 'POST':
        iform = Insurance_Register(request.POST)
        if iform.is_valid():
            #resposne = requests.post("API", data=request.POST)
            return render(request, 'insurance_Reg.html')

    else:
        rform = Insurance_Register()
        return render(request, 'insurance_Reg.html', {'form': rform})


def Ins_Info(request):
    sform = Account_Info()
    return render(request, 'Single.html', {'form': sform})


def Loan_Reg(request):
    if request.method == 'POST':
        iform = Loan_Register(request.POST)
        if iform.is_valid():
            #resposne = requests.post("API", data=request.POST)
            return render(request, 'loan_Reg.html')

    else:
        rform = Loan_Register()
        return render(request, 'loan_Reg.html', {'form': rform})


