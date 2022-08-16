from numpy import empty
from .models import Users, Booking
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth import authenticate, login, logout
from matplotlib.style import context
from sqlalchemy import null
import string
import random

context = {
        'otp': 0,
        'test' : False,
        'U_token' : "",
        "Who" : "",
        'mail':""
}

def index(request,flg=False):
    Whos = Users.objects.filter(username__contains = request.user)
    for Who in Whos:
        if Who.user_Pname != "":
            context['Who'] = Who.user_Pname
        else:
            context['Who'] = ""
    
    import random
    print(request.method)
    if request.method == 'POST' :
        otp = random.randint(1,999999)
        print('inside index')
        try:
            context['mail']=request.POST['frgt_mail']
        except MultiValueDictKeyError:
            context['mail']=request.user.email
        if flg == True:
            if(mail(request,otp)):
                context['otp']=otp
                context['test']=True
                context['flg']=flg
                return render(request,'auth.html',context)
        else: 
            if(mail(request,otp)):
                context['otp']=otp
                context['test']=True
                context['flg']=flg
                return render(request,'auth.html',context)
        
        
        # detail = Users.objects.filter(username__contains = request.user.username)
        # print (detail.user_fname, detail.user_lname, detail.user_phone,detail.user_email)
            
    else :
        print("hello")
        return render(request, 'index.html', context)

def getticket():
    import traceback
    print('inside getticket')
    print(context)
    if context['U_token']!='':
        bk=Booking.objects.get(U_token = context['U_token'])
        print(bk)
        print(bk.price,bk.U_VType,bk.U_TimeSlot,bk.O_Username)
        if bk.extended:
            abc='''<h6>Your booking is <b>Extended</b></h6>'''
        else:
            abc=''
        tick='''
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet"

    integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">

    <script src="https://kit.fontawesome.com/15a00c5ce9.js" crossorigin="anonymous"></script>

    <style>

        body{

            background-color: rgb(255, 178, 34);

            height: auto;

            width: auto;

        }

        .aboutus{

            height: 100%;

            width: 100%;

        }

 

        .aboutus h1{

            text-align: center;

        }

 

        .aboutus h5{

            text-align: center;

        }

 

        .aboutus h6{

            text-align: center;

            color: black;

        }

 

        .aboutus .card{

            width: 100%;

            background-color: rgb(255, 178, 34);;

            border-radius: 20px;

            border-color: rgb(255, 183, 0);

            padding: 5%;

        }

 

    </style>

</head>

<body>

    <div class="aboutus">

        <div class="card">

            <h1><B>PARKING TICKET</B></h1>

            <h5>

                <h6>PARKING NAME : '''+bk.O_Username+'''</h6>

                <h6>PARKING TIME : '''+str(bk.U_TimeSlot)+'''</h6>

                <h6>PARKING DURATION : '''+context['U_Duration']+'''</h6>

                <h6>PARKING TOKEN : '''+context['U_token']+'''</h6>

                <h6> VEHICLE TYPE : '''+bk.U_VType+'''</h6>
                '''+abc+'''
                <h6>PRICE : '''+str(bk.price)+'''</h6>

            </h5>

        </div>

    </div>

</body>

</html>
'''
        print('abcd',tick)
        return tick
    else:
        # print(bk.price,bk.U_VType,bk.U_TimeSlot,bk.O_Username)
        return None

def mail(request,otp=null,ticket=False):
    print('inside mail')
    print(context)
    import smtplib
    from email.message import EmailMessage
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    try:
        em = EmailMessage()
        em['from'] = "parkersplace00@gmail.com"
        em['Subject'] = "Check this out"
        if(context['mail']!=''):
            em['To'] = context['mail']
        else:
            bk = Booking.objects.get(U_token = context['U_token'])
            em['To'] = bk.U_Email
            context['mail'] = bk.U_Email
        # print(context)
        if otp!=null:
            body='Dear customer your OTP : '+str(otp)
            em.set_content(body)
        elif ticket!=False:
            print(getticket())
            em.add_alternative(getticket(),subtype='html')
        else:
            return null
        print("reciever : "+context['mail'])
        if(server.login('parkersplace00@gmail.com','zvjyqgctatqdzszb')):
            print("login successful")
            print(otp,context['U_token']) #######add emailbelow context['mail']
            server.sendmail('parkersplace00@gmail.com',context['mail'],em.as_string()) 
            print ("Email Send")
            return True 
            
        else:
            print ("Email not Send")
            context['test']=True
            return False
    finally:
        server.quit()

def auth(request):
    otp=context['otp']
    # print(request.method,context)
    if request.method == 'POST' :
        try:
            otp2=str(request.POST['otp1'])
            otp2+=str(request.POST['otp2'])
            otp2+=str(request.POST['otp3'])
            otp2+=str(request.POST['otp4'])
            otp2+=str(request.POST['otp5'])
            otp2+=str(request.POST['otp6'])
            otp2= int(otp2)
            print(str(otp2)+"   "+str(otp))
        except MultiValueDictKeyError:
            otp2=" "    
        
        if(str(otp)==str(otp2)):            
            if(context['flg']):
                context['U_token']= ''.join(random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase) for i in range(10))
                print(request.user,'\t',request.user.username)
                details = Users.objects.filter(username__contains = request.user.username)
                for detail in details:
                    new_booking = Booking(O_Username =  context['O_Username'] , U_Username = request.user.username, U_FirstName = detail.user_fname, U_LastName = detail.user_lname, U_MobNo = detail.user_phone, U_Email = detail.user_email, 
                    U_VehicleNo = context['Vehicle_no'], U_TimeSlot = context['U_time'], U_Duration = context['U_Duration'], U_token = context['U_token'] , U_status = False , U_VType=context['VType'] , extended=False, price=context['price'])
                    new_booking.save()
                mail(request,null,True)
                messages.success(request, "Your booking is successfully completed.")
                return render(request, 'index.html', context)
            else:
                return render(request, 'index.html', context)

        else:
            messages.error(request, "Enter Correct OTP.")
            return render(request, 'auth.html',context)
    else:   
        messages.error(request, "Enter Correct OTP.")
        return render(request, 'auth.html',context)

def card_list(request):
    print('inside cardlist')
    from datetime import datetime
    hr =datetime.now().strftime("%H")
    mn =datetime.now().strftime("%M")
    if request.method == "POST":
        import re
        try:
            context['O_Username'] = request.POST['O_name']
            context['VType'] = request.POST['Vehicle']
            context['Vehicle_no'] = request.POST['reg']
            context['U_time']= request.POST['time']
            context['U_Duration'] = duration(request,request.POST['duration'])
            context['price'] = PriceCalc(context['U_Duration'],context['VType'])
            # Indian driving license number regex
            regex = '^[a-zA-Z]{2}[ -][0-9]{1,2}[ -][a-zA-Z]{1,2}[ -][0-9]{4}$'
            no_for = re.compile(regex)
            if(re.search(no_for,context['Vehicle_no'])):
                if index(request,True):
                    return render(request,'auth.html',context)
            else:   
                messages.error(request, "Enter proper vehicle number")
                return render(request,'card_list.html',context)
        except MultiValueDictKeyError:
            Vehicle_no=" "
                
        try:  
            Parkloc = request.POST['Searchloc']
        except MultiValueDictKeyError:
            Parkloc='all'
        if Parkloc == 'all':
            POs = Users.objects.all()
            return render(request, 'card_list.html', {'POs': POs, 'search': Parkloc, 'hr' : hr, 'mn' : mn, 'Who' : context['Who']})
        else:
            POs = Users.objects.filter(user_PAname__contains=Parkloc)
            return render(request, 'card_list.html', {'POs': POs, 'search': Parkloc, 'hr' : hr, 'mn' : mn, 'Who' : context['Who']})

    else:
        return render(request, 'index.html', context)

def client(request):
    if request.method == 'POST':
        try:
            print(request.POST)
            if request.POST['token']:
                bk=Booking.objects.get(U_token = request.POST['token'])
                bk.extended = False
                bk.U_status = True
                name=   bk.U_Username
                bk.save()
                messages.success(request, 'Booking of '+name+' is Verified') 
        except MultiValueDictKeyError:
            pass
        except Exception:
            pass
        try:
            print(request.POST)
            if request.POST['Extend']:
                bk=Booking.objects.get(U_token = request.POST['Extend'])
                try:
                    context['U_token'] = request.POST['Extend']
                    duration=extendDuration(request,bk.U_Duration)
                    context['U_Duration']=duration
                    bk.price=PriceCalc(duration,bk.U_VType)     
                    bk.U_Duration=duration
                    bk.extended =True 
                    bk.U_status = False   
                    name=   bk.U_Username
                    bk.save()
                    mail(request,null,True)
                    messages.success(request, 'Booking of '+name+' is Extended') 
                except Exception:
                    pass
        except MultiValueDictKeyError:
            pass
        try:        
            if request.POST['Remove']:
                Booking.objects.filter(U_token = request.POST['Remove']).delete()
                name=   bk.U_Username
                messages.error(request, 'Booking of '+name+' is removed')
                print ('removed')
        except MultiValueDictKeyError:
            pass
        try:
            if request.POST['sort'] == 'N_Verified':
                Bks = Booking.objects.filter(U_status = False )
                # Bks = Bks.filter(O_Username=request.user)
                for Bk in Bks:
                    Bk.U_Duration=str(Bk.U_Duration).strip("apm")
                return render(request, 'POwner.html', {'Bks': Bks, 'Who' : context['Who']})
            elif request.POST['sort'] == 'Verified':
                Bks = Booking.objects.filter(U_status = True )
                # Bks = Bks.filter(O_Username=request.user)
                for Bk in Bks:
                    Bk.U_Duration=str(Bk.U_Duration).strip("apm")
                return render(request, 'POwner.html', {'Bks': Bks, 'Who' : context['Who']})
            else:
                Bks = Booking.objects.filter(O_Username=request.user)
                for Bk in Bks:
                    Bk.U_Duration=str(Bk.U_Duration).strip("apm")
                return render(request, 'POwner.html', {'Bks': Bks, 'Who' : context['Who']})
        except MultiValueDictKeyError:
            pass
    else:
        pass
    Bks = Bks = Booking.objects.filter(O_Username=request.user)
    for Bk in Bks:
        Bk.U_Duration=str(Bk.U_Duration).strip("apm")
    return render(request, 'POwner.html',{'Bks':Bks, 'Who' : context['Who']})

def duration(request,a):
    if(a=='1 Hr'):
        return '01:00'
    elif(a=='2 Hr'):
        return '02:00'
    elif(a=='3 Hr'):
        return '03:00'
    elif(a=='4 Hr'):
        return '04:00'
    elif(a=='5 Hr'):
        return '05:00'
    else:
        return '00:30'

def extendDuration(request, duration):
    duration=str(duration)
    dur = duration.strip("apm APM")
    hr,mn,sc=dur.split(":")
    hr=int(hr) 
    mn=int(mn)
    mn+=30
    if mn>=60:
        mn-=60
        hr+=1
    tm=str(hr)+":"+str(mn)
    print('extended time :',tm)
    return(tm)

def PriceCalc(tm,type):
    hr,mn=tm.split(":")
    hr=int(hr)
    mn=int(mn)
    price=0
    mn=mn/30
    if type =='Bike':
        price+= hr*20
        if(mn!=0): price+=mn*10
    elif type =='Car':
        price += hr*40
        if(mn!=0): price+=mn*20
    else: pass
    print(price)
    return price

def about(requst):
    return render(requst, 'about.html', context)

def services(request):
    print('abc',getticket())
    return render(request, 'services.html')

def contact(requst):
    return render(requst, 'contact.html')

def signup(requst):
    return render(requst, 'signup.html', context)

# Login Logout Signup Password Handling
def password_check(request, passwd):
      
    SpecialSym =['$', '@', '#', '%']
    val = True
      
    if len(passwd) < 6:
        messages.error(request, "LENGTH SHOULD BE AT LEAST 6!!!")
        val = False
          
    if len(passwd) > 20:
        messages.error(request, "LENGTH SHOULD NOT BE GREATER THAN 8!!!")
        val = False
          
    if not any(char.isdigit() for char in passwd):
        messages.error(request, "PASSWORD SHOULD HAVE AT LEAST ONE NUMERAL!!!")
        val = False
          
    if not any(char.isupper() for char in passwd):
        messages.error(request, "PASSWORD SHOULD HAVE AT LEAST ONE UPPERCASE LETTER!!!")
        val = False
          
    if not any(char.islower() for char in passwd):
        messages.error(request, "PASSWORD SHOULD HAVE AT LEAST ONE LOWERCASE LETTER!!!")
        val = False
          
    if not any(char in SpecialSym for char in passwd):
        messages.error(request, "PASSWORD SHOULD HAVE AT LEAST ONE OF THE SYMBOLS $@#!!!")
        val = False
    if val:
        return val

def handleSignUp(request):
    if request.method == 'POST':
        urname = request.POST['urname']
        fname = request.POST['fname']
        mname = request.POST['mname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        pwd = request.POST['pwd']
        cpwd = request.POST['confirm_pwd']
        parkname = request.POST['pname']
        parkaname = request.POST['apname']
        addr = request.POST['paddr']
        try:
            parkimg = request.FILES['user_Pimage']
        except:
            if parkname is null:
                parkimg = null
            else:
                parkimg = "home/images/row1.jpg"
    
        if User.objects.filter(username=urname):
            messages.error(request, "USERNAME ALREADY EXIST! PLEASE TRY SOME ANOTHER USERNAME")
            return redirect('/signup')

        if pwd != cpwd:
            messages.error(request, "PASSWARD DOES NOT MATCH!!!")
            return redirect('/signup')

        if (not password_check(request, pwd)):
            return redirect('/signup')

        if len(phone) < 10:
            messages.error(request, "INVALID PHONE NUMBER!!!")
            return redirect('/signup')

        parkname = parkname.upper()
        parkaname = parkaname.upper()

        #create 
        new_user = Users(username = urname, user_fname = fname, user_mname = mname, user_lname = lname, user_email = email, user_phone = phone, 
         user_Pname = parkname, user_PAname = parkaname, user_Paddr = addr, user_Pimage = parkimg)
        new_user.save()

        myuser = User.objects.create_user(urname, email, pwd)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created.")
        return redirect('/')
    else:
        return render(request, 'signup.html')

def handleLogin(request):
    if request.method == 'POST':
        log_usr = request.POST['log_username']
        log_pwd = request.POST['log_pwd']

        user = authenticate(username=log_usr, password=log_pwd)
        if user is not None:
            Whos = Users.objects.filter(username__contains = user)
            login(request, user)
            messages.success(request, 'Successfully Logged In.')
            for Who in Whos:
                print(Who.user_Pname)
                if Who.user_Pname == "":
                    context["Who"] = ""
                    return render(request, 'index.html', context)
                else:
                    context["Who"] = Who.user_Pname
                    return render(request, 'POwner.html', context)
        else:
            messages.error(request, 'Invalid Credentials, Please try again.')
            return redirect('/')
    return HttpResponse('404 - Not Found')

def handleLogout(request):
    context["Who"] = ""
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('/')