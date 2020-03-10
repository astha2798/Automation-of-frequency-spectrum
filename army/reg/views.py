from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from reg.models import Armyunit,Freqgrant,Headquarters
import random
from random import randint
from twilio.rest import Client
from django.shortcuts import render_to_response
from django.contrib import messages
from django.http import HttpResponseRedirect
import math
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image
# from StringIO import StringIO
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

    #Variable declaration

# Create your views here.
def index(request):
	template=loader.get_template('reg/index.html')
	context={


	}
	return HttpResponse(template.render(context,request))
def otp(request):
    global phone,fullname,email,password,rpassword,area,verification_code
    print(phone,verification_code)
    if request.method=="POST":
        otp1=request.POST['otp']
        print(otp1)
        if(otp1==verification_code):
            x="otp verified"
            print(x)
            u = Armyunit.objects.update_or_create(fullname=fullname, email=email, password=password,phone=phone,area=area)
            template=loader.get_template('reg/reg_complete.html')
            context={


            }
            # messages.success(request, 'Profile details updated.')
            # return render_to_response('reg/index.html', message='Registration complete! Please head over to the Main page to check logs or request for new grant.')
            return HttpResponse(template.render(context,request))
            context={


            }    # return render_to_response('reg/index.html', message='Registration complete! Please head over to the Main page to check logs or request for new grant.')
            return HttpResponse(template.render(context,request))
            # return HttpResponse("Registration complete! Please head over to the <a href='reg/index.html'>Main page</a> to check logs or request for new grant.")
        else:
            template=loader.get_template('reg/reg_wrong.html')
            context={


            }
            return HttpResponse(template.render(context,request))
    else:
        return render(request, "reg/otp.html", {})
        # return HttpResponse("OTP wrong !Please head over to the <a href='reg/register.html'>Registration</a> ")

def register(request):
    print("hoii")
    if request.method == "POST":
        global phone,fullname,email,password,rpassword,area,verification_code
        fullname = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['psw']
        rpassword = request.POST['psw-repeat']
        area = request.POST['area']
        phone = request.POST['phone']
        print(fullname)
        verification_code=str(randint(100000, 999999))
        print(verification_code)
        account_sid ='AC7a78f7ec6245eefecbc6a4a75771733f'
        auth_token ='1f37e9dc186fc4213271f8f4d6db6cda'
        twilio_number = '+15752194253'
        client = Client(account_sid, auth_token)
        client.api.messages.create(phone,
		               from_=twilio_number,
		               body=verification_code)
        template=loader.get_template('reg/otp.html')
        context={


		}
        return HttpResponse(template.render(context,request))
        # u = Armyunit.objects.update_or_create(fullname=fullname, email=email, password=password,phone=phone,area=area)
        # u.save()

        # return HttpResponse("Registration complete! Please head over to the <a href='/login/'>login page</a> to check logs or request for new grant.")

    return render(request, "reg/register.html", {})

def register_q(request):
    if request.method == "POST":
        global mobile,pas
        username = request.POST['username']
        passw = request.POST['passw']
        # print(mobile,pas)
        template=loader.get_template('reg/register.html')
        context={


        }
        u = Headquarters.objects.filter(username=username, password=passw)
        print(u)
        if(len(u)>0):
            return HttpResponse(template.render(context,request))
        else:
            return HttpResponseRedirect('/reg/register_q')
    return render(request, "reg/login_q.html", {})
def login_headq(request):
    if request.method == "POST":
        # a=Armyunit.objects.filter(phone=mobile, password=pas)
        # aid=a[0].id
        logs=Freqgrant.objects.filter()
        template=loader.get_template('reg/logs.html')
        context={
            'logs':logs,

            }
        username = request.POST['username']
        passw = request.POST['passw']
        # print(mobile,pas)
        u = Headquarters.objects.filter(username=username, password=passw)
        print(u)
        if(len(u)>0):
            return HttpResponse(template.render(context,request))
        else:
            return HttpResponseRedirect('/reg/login_headq')
    return render(request, "reg/login_headq.html", {})
def grant(request):
    print("hoii")
    if request.method == "POST":
        global mobile,pas
        print(mobile,pas)
        a=Armyunit.objects.filter(phone=mobile, password=pas)
        aid=a[0].id
        duration = request.POST['duration']
        etype = request.POST['etype']
        espec = request.POST['espec']
        flower = request.POST['flower']
        fupper = request.POST['fupper']

        Freqgrant.objects.update_or_create(aid=aid,duration=duration, etype=etype,espec=espec,flower=flower,fupper=fupper)
        template=loader.get_template('reg/grant_complete.html')
        context={


            }
            # messages.success(request, 'Profile details updated.')
            # return render_to_response('reg/index.html', message='Registration complete! Please head over to the Main page to check logs or request for new grant.')
        return HttpResponse(template.render(context,request))
        # return HttpResponse("Grant accepted! Please head over to the <a href='/login/'>login page</a> to start using your website.")

    return render(request, "reg/grant.html", {})
def log(request):
    global mobile,pas
    a=Armyunit.objects.filter(phone=mobile, password=pas)
    aid=a[0].id
    logs=Freqgrant.objects.filter(aid=aid)
    template=loader.get_template('reg/logs.html')
    context={
        'logs':logs,

        }
    return HttpResponse(template.render(context,request))

def login_grant(request):
    if request.method == "POST":
        global mobile,pas
        mobile = request.POST['mobile']
        pas = request.POST['psw']
        print(mobile,pas)
        template=loader.get_template('reg/grant.html')
        context={


        }
        u = Armyunit.objects.filter(phone=mobile, password=pas)
        print(u)
        if(len(u)>0):
            return HttpResponse(template.render(context,request))
        else:
            return HttpResponseRedirect('/reg/login_grant')
    return render(request, "reg/login.html", {})
def login_logs(request):
    if request.method == "POST":
        global mobile,pas
        mobile = request.POST['mobile']
        pas = request.POST['psw']
        print(mobile,pas)
        template=loader.get_template('reg/logs.html')
        context={


        }
        u = Armyunit.objects.filter(phone=mobile, password=pas)
        print(u)
        if(len(u)>0):
            aid=u[0].id
            logs=Freqgrant.objects.filter(aid=aid)
            print(logs)
            # template=loader.get_template('reg/logs.html')
            context={
                'logs':logs

                }
            return HttpResponse(template.render(context,request))
        else:
            return HttpResponseRedirect('/reg/login_logs')
    return render(request, "reg/login_log.html", {})

def pathloss(request):
    if request.method == "POST":
        global theight,rheight,cfreq
        theight = request.POST['theight']
        rheight = request.POST['rheight']
        cfreq = request.POST['cfreq']
        # print(mobile,pas)
        template=loader.get_template('reg/path_loss.html')
        context={


        }
        return HttpResponse(template.render(context,request))
    return render(request, "reg/loss_details.html", {})

def hatamodel(request):
    import random
    import django
    import datetime

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    global theight,rheight,cfreq
    print(theight,rheight,cfreq)
    d=np.array([1, 2, 3, 4, 5]);  #in km
    hb=theight; #Height of BS antenna in metres
    hm=rheight;# height of mobile antenna in matres
    fc=cfreq;#carrier frequency in MHz
    W=15;  #street width(m)
    b=30;  # distance between building along radio path (m) 
    phi=90; # incident angle relative to the street
    hr=30; #in m
    hb=int(hb); #Height of BS antenna in metres
    hm=int(hm);# height of mobile antenna in matres
    fc=int(fc);#carrier frequency in MHz

    #Calculations
    dellhm=hr-hm;

    #Okumura/Hata model
    ahm=(1.1*math.log10(fc)-0.7)*hm-(1.56*math.log10(fc)-0.8);
    L_50=69.55+26.16*np.log10(fc)+(44.9-6.55*np.log10(hb))*np.log10(d)-13.82*np.log10(hb)-ahm;
    L_50 = np.array(L_50)

    #Results
    fig=Figure()
    ax1=fig.add_subplot(111)
    ax1.plot(d,L_50,'b-')
    ax1.set_xlabel('Distance from transmitter(in km)')
    ax1.set_ylabel('Path loss (in dB)')
    # ax2 = ax1.twinx()
    # ax2.plot(d,L50,'r')
    # ax1.legend(['COST 231 model'],loc=0)
    # ax2.legend(['HATA model'],loc=0)
    # ax1.grid()
    # plt.show()
    canvas=FigureCanvas(fig)
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

def costmodel(request):
    import random
    import django
    import datetime

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter


    d=np.array([1, 2, 3, 4, 5]);  #in km
    hb=30; #Height of BS antenna in metres
    hm=2;# height of mobile antenna in matres
    fc=900;#carrier frequency in MHz
    W=15;  #street width(m)
    b=30;  # distance between building along radio path (m) 
    phi=90; # incident angle relative to the street
    hr=30; #in m

    #Calculations
    dellhm=hr-hm;
    #L50=Lf+Lrts+Lms

    # By COST 231 model
    Lf=32.4+20*np.log10(d)+20*np.log10(fc);
    L0=4-0.114*(phi-55);
    Lrts=-16.9-10*math.log10(W)+10*math.log10(fc)+20*math.log10(dellhm)+L0;
    Lbsh=-18*math.log10(11);
    ka=54-0.8*hb;
    dellhb=hb-hr;
    kd=18-15*dellhb/dellhm;
    kf=4+0.7*(fc/925-1);
    Lms=Lbsh+ka+kd*np.log10(d)+kf*np.log10(fc)-9*np.log10(b);
    L50=np.array([0, 0, 0, 0, 0])
    L50=Lf+Lrts+Lms;

    # #Okumura/Hata model
    # ahm=(1.1*math.log10(fc)-0.7)*hm-(1.56*math.log10(fc)-0.8);
    # L_50=69.55+26.16*np.log10(fc)+(44.9-6.55*np.log10(hb))*np.log10(d)-13.82*np.log10(hb)-ahm;
    # L_50 = np.array(L_50)

    #Results
    fig=Figure()
    ax1=fig.add_subplot(111)
    ax1.plot(d,L50,'b-')
    ax1.set_xlabel('Distance from transmitter(in km)')
    ax1.set_ylabel('Path loss (in dB)')
    # ax2 = ax1.twinx()
    # ax2.plot(d,L50,'r')
    # ax1.legend(['COST 231 model'],loc=0)
    # ax2.legend(['HATA model'],loc=0)
    # ax1.grid()
    # plt.show()
    canvas=FigureCanvas(fig)
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

def costmodel_calc(request):
    import random
    import django
    import datetime

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter


    d=np.array([1, 2, 3, 4, 5]);  #in km
    hb=30; #Height of BS antenna in metres
    hm=2;# height of mobile antenna in matres
    fc=900;#carrier frequency in MHz
    W=15;  #street width(m)
    b=30;  # distance between building along radio path (m) 
    phi=90; # incident angle relative to the street
    hr=30; #in m

    #Calculations
    dellhm=hr-hm;
    #L50=Lf+Lrts+Lms

    # By COST 231 model
    Lf=32.4+20*np.log10(d)+20*np.log10(fc);
    L0=4-0.114*(phi-55);
    Lrts=-16.9-10*math.log10(W)+10*math.log10(fc)+20*math.log10(dellhm)+L0;
    Lbsh=-18*math.log10(11);
    ka=54-0.8*hb;
    dellhb=hb-hr;
    kd=18-15*dellhb/dellhm;
    kf=4+0.7*(fc/925-1);
    Lms=Lbsh+ka+kd*np.log10(d)+kf*np.log10(fc)-9*np.log10(b);
    L50=np.array([0, 0, 0, 0, 0])
    L50=Lf+Lrts+Lms;

    # #Okumura/Hata model
    # ahm=(1.1*math.log10(fc)-0.7)*hm-(1.56*math.log10(fc)-0.8);
    # L_50=69.55+26.16*np.log10(fc)+(44.9-6.55*np.log10(hb))*np.log10(d)-13.82*np.log10(hb)-ahm;
    # L_50 = np.array(L_50)
    # ax2 = ax1.twinx()
    # ax2.plot(d,L50,'r')
    # ax1.legend(['COST 231 model'],loc=0)
    # ax2.legend(['HATA model'],loc=0)
    # ax1.grid()
    # plt.show()
    template=loader.get_template('reg/calc_model.html')
    context={
                'loss0':L50[0],
                'loss1':L50[1],
                'loss2':L50[2],
                'loss3':L50[3],
                'loss4':L50[4],


                }
    return HttpResponse(template.render(context,request))
    return response

def hatamodel_calc(request):
    import random
    import django
    import datetime

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    global theight,rheight,cfreq
    print(theight,rheight,cfreq)
    d=np.array([1, 2, 3, 4, 5]);  #in km
    hb=theight; #Height of BS antenna in metres
    hm=rheight;# height of mobile antenna in matres
    fc=cfreq;#carrier frequency in MHz
    W=15;  #street width(m)
    b=30;  # distance between building along radio path (m) 
    phi=90; # incident angle relative to the street
    hr=30; #in m
    hb=int(hb); #Height of BS antenna in metres
    hm=int(hm);# height of mobile antenna in matres
    fc=int(fc);#carrier frequency in MHz

    #Calculations
    dellhm=hr-hm;

    #Okumura/Hata model
    ahm=(1.1*math.log10(fc)-0.7)*hm-(1.56*math.log10(fc)-0.8);
    L_50=69.55+26.16*np.log10(fc)+(44.9-6.55*np.log10(hb))*np.log10(d)-13.82*np.log10(hb)-ahm;
    L_50 = np.array(L_50)
    template=loader.get_template('reg/calc_model.html')
    context={
                'loss0':L_50[0],
                'loss1':L_50[1],
                'loss2':L_50[2],
                'loss3':L_50[3],
                'loss4':L_50[4],


                }
    return HttpResponse(template.render(context,request))
    #Results
    return response

def power_rec(request):
    if request.method == "POST":
        carfreq = request.POST['carfreq']
        # print(mobile,pas)
        Lp=140; # path losses in dB 
        k=1.38*10**-23; # Boltzmann’s constant (W/Kelvin-Hz)
        k_db=10*math.log10(k);
        f=carfreq;#in MHz
        Gt=8; #transmitting antenna gain(dB)
        Gr=0; #receiver antenna gain(dB)
        Ag=24;#gain of receiver ampliﬁer in dB 
        Fmargin=8;#Fade margin(dB)
        Nf=6;#Noise figure(dB)
        L0=20; # other losses in dB
        Lf=12; # antenna feed line loss in dB 
        T=24.6;#Temperature expressed in dB
        R=39.8; # data rate in dB 
        M=8;  #overall link margin(dB)
        Eb_No=10;#dB

        #Calculations
        #From equation  (3.54)
        pt_db=M-Gt-Gr-Ag+ Nf + T+ k_db+ Lp+ Lf+ L0 + Fmargin+ R+ Eb_No;

        Pt=10**(pt_db/10);  #dB into normal number
        template=loader.get_template('reg/received_power.html')
        context={
            "rpower":Pt

        }
        return HttpResponse(template.render(context,request))
    return render(request, "reg/received_details.html", {})