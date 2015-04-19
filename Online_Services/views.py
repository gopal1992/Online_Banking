from django.shortcuts import render, HttpResponse
from Online_Services.models import Login, Register


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def sign_up(request):
    return render(request, 'sign_up.html')


def sign_up_user(request):
    #import pdb
    #pdb.set_trace()
    if request.method == 'POST':
        uid = request.POST['uid']
        try:
            obj = Register.objects.get(UID=uid)
        except:
            obj = None
            if not obj:
                if request.POST['pwd1'] == request.POST['pwd2']:
                    obj = Register(UID=request.POST['uid'],
                                   Login_Name=request.POST['username'],
                                   Password=request.POST['pwd1'],
                                   Confirmpassword=request.POST['pwd2'],
                                   Phonenumber=request.POST['phonenumber'],
                                   Email_id=request.POST['emailid'])
                    obj.save()
                    obj = Login(UserName=request.POST['username'],
                                password=request.POST['pwd1'])
                    obj.save()
                    return render(request, 'login.html')
                else:
                    return HttpResponse("Password doesn't match")
            else:
                return HttpResponse("user already exist")
