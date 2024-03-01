from django.shortcuts import render, redirect
from hospitalapp.models import member, message, users


# Create your views here.
def index(request):
    if request.method == 'POST':
        Message = message(name=request.POST['name'],
                          email=request.POST['email'],
                          subject=request.POST['subject'],
                          Message=request.POST['message'])
        Message.save()
        return redirect('/')
    else:
        return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        Member = member(username=request.POST['username'], email=request.POST['email'],
                        password=request.POST['password'])
        Member.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')


def upload(request):
    return render(request, 'upload.html')


def details(request):
    details = message.objects.all()
    return render(request, 'details.html', {'details': details})


def user(request):
    Users = users.objects.all()
    return render(request, 'users.html', {'users': Users})

def adminhome(request):
    if request.method == 'POST':
        if member.objects.filter(username=request.POST['username'],
                                 password=request.POST['password']).exist():
            Member = member.objects.get(username=request.POST['username'],
                                         password=request.POST['password'])
            return render(request,'adminhome.html',{'Member':Member})
        else:
            return render(request,'login.html',)
    else:
        return render(request,'login.html')
