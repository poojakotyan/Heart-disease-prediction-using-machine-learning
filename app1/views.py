from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score 

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 == pass2:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
            #return render(request,'login.html')
        else:
            return HttpResponse("Password Not Matching !!!!!")
    return render(request,'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else : 
            return HttpResponse('Username or Password is incorrect !!!')

    return render(request,'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')

def result(request):
    data = pd.read_csv(r"C:\Users\pooja\Desktop\django\heart_disease\static\Heart_Disease_Prediction.csv")
    X = data.drop("Heart Disease",axis=1)
    Y = data['Heart Disease']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)
    model = LogisticRegression()
    model.fit(X_train, Y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    val9 = float(request.GET['n9'])
    val10 = float(request.GET['n10'])
    val11 = float(request.GET['n11'])
    val12 = float(request.GET['n12'])
    val13 = float(request.GET['n13'])

    pred = model.predict([[val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13,]])

    result1 = ""
    if pred==[1]:
        result1 = "Positive"
    else :
        result1 = "Negetive"

    return render(request, 'home.html',{"result2":result1})