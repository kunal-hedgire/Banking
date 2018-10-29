from django.shortcuts import render,redirect
from BankApp.forms import RegisterForm,LoginForm,Account_Register,Account_Info,Insurance_Register,Loan_Register,Withdrawn_Deposite
from BankApp.models import Login,Register
from BankApp.Image_Upload.upload import handle_uploaded_file

import requests
from rest_framework.response import Response

def getcustidbyname(name):
    response = requests.get("http://eknath.pythonanywhere.com/customers/").json()
    data1=response
    for cust in data1:
        print(cust)
        print(name)
        print(cust['customerName'])
        if cust['customerName'] == name:
            return cust['customerID']

    '''
   
         print(data1['customerID'])
         s=data1['customerID']
         return s
         '''
def login(request):

    if request.method=="POST":

        lform = LoginForm(request.POST)

        username = request.POST['customerName']
        #print(username)
        Password = request.POST['password']
        user = Register.objects.filter(customerName=username)
        #print(user[0].password)

        password = user[0].password

        #print(Password)
        if password == Password:
             #return redirect('/show',{'name':username})
             cust_id=getcustidbyname(username)
             print(cust_id)
             return render(request,'show.html',{'name':username,'cust_id':cust_id})

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
            username = userObj['customerName']
            if not (Register.objects.filter(customerName=username).exists()):
                Register.objects.all()
                handle_uploaded_file(request.FILES['imgfile'])
                sform.save()
                response=requests.post('http://eknath.pythonanywhere.com/customers/',data=request.POST)
                return redirect('/signin')

            else:
                #sform = RegisterForm()
                return render(request, 'register.html', {'form': sform})


    else:
        sform = RegisterForm()
        return render(request,'register.html',{'form':sform})
'''
def DiffAcc(request):

    return render(request,'show.html')
'''

def Acc_Register(request,id):
    if request.method =='POST':
        print(request.POST)
        resposne = requests.post("http://eknath.pythonanywhere.com/accounts/", data=request.POST).json()
        sform = Account_Info()
        return render(request, 'Single.html', {'form': sform, 'resposne':resposne})

    else:
        rform=Account_Register()
        return render(request,'Acc_Register.html',{'form':rform,'id':id})

def Acc_Info(request):
    sform=Account_Info()
    return render(request, 'Single.html',{'form':sform})

def Acc_Get(request):
        #print(request.method)
        if request.method == 'GET':
            ide = request.GET['id']
            #print(ide)
            # uriget=
            response = requests.get("http://eknath.pythonanywhere.com/accounts/{}".format(ide))
            getid = response.json()
            print(getid)
            return render(request, 'Show_Acc_Details.html', {'mylist': getid})

            #return render(request, 'Single.html',{'mylist':ide})
        else:
            ide = request.GET['id']
            return render(request, 'Single.html', {'mylist': ide})

def With_Depo(request):

    if request.method == 'POST':
        print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii_____________________")
        NO = request.POST
        print(NO)
        # uriget=
        response=requests.post("http://eknath.pythonanywhere.com/transaction/",data=request.POST)
        print(response)
        getid = response.json()
        #print(getid)
        return render(request, 'Show_Acc_Details.html', {'mylist': getid})
        #return Response(response)

        # return render(request, 'Single.html',{'mylist':ide})
    else:
        NO = Withdrawn_Deposite()
        return render(request, 'With_depo.html', {'form': NO})


def Insurance_Info(request):
    if request.method == 'POST':
        iform = Insurance_Register(request.POST)
        if iform.is_valid():
            resposne = requests.post("http://niraj123.pythonanywhere.com/postinsurance/", data=request.POST)
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


