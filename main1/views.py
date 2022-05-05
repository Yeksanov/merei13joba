from django.shortcuts import render, redirect
from .models import Person
from .models import Person1
from .models import Person2
from .models import Person3
from .models import city
from .models import Form
from .forms import FormCreate
from django.core.mail import send_mail
from django.core.mail import EmailMessage



def send_message(request): 
    send_mail("Welcome to testing page","My content","200103509@stu.sdu.edu.kz",["200103509@stu.sdu.edu.kz","200103509@stu.sdu.edu.kz"], 
              fail_silently=False,html_message="<b>Bold text </b> <i>Italic text </i>" )
    return render (request,'main1/successfull.html')





















def register(request):
    register = FormCreate()
    if request.method == 'POST':
        register = FormCreate(request.POST, request.FILES)
        if register.is_valid():
            try:
                register.save()
                return redirect('index')
            except:
                register.add_error(None, 'Your form is wrong.')
    else:
        register = FormCreate()
    return render(request, 'main1/form.html', {'registration':register})


def home(request):
    person = Person.objects.all()
    return render(request,'main1/page0.html',{'title':'Footbal-Home','person':person})

def boxing(request):

    person=Person2.objects.all()
    return render(request, 'main1/page1.html',{'title':'Boxing-Hall','person':person})


def wrestling(request):
    person=Person1.objects.all()

    return render(request,'main1/index.html',{'title':'Wresling-Hall','person':person})

def footbal(request):
    person = Person3.objects.all()
    return render(request,'main1''/page3.html',{'title':'Footbal-Hall','person':person})

