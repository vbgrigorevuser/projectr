from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Manager

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('login-email', 'undefined')
        hpass = request.POST.get('login-password', 'undefined')

        qs = Manager.objects.filter(manager_email=email)

        context = {
            'email' : email
        }

        if not qs:
            return render(request, 'managerauth/noaccount.html', context=context)
        
        if hpass != qs[0].manager_hpass:
            return render(request, 'managerauth/invalidpassword.html', context=context)
        
        # Render logged
        return HttpResponse('Login well done!')

    raise Http404()

def register(request):
    if request.method == 'POST':
        name = request.POST.get('register-name', 'undefined')
        email = request.POST.get('register-email', 'undefined')
        hpass = request.POST.get('register-password', 'undefined')
        
        manager_with_email = Manager.objects.filter(manager_email=email)
        # print('\n\n\n{}\n\n\n'.format(manager_with_email))

        context = {
            'email' : email,
        }

        if manager_with_email:
            return render(request, 'managerauth/onregisteremail.html', context=context)
        
        manager = Manager(
            manager_name = name,
            manager_email = email,
            manager_hpass = hpass
        )

        manager.save()

        return render(request, 'managerauth/onregister.html', context=context)

    raise Http404()

def start(request):
    return render(request, 'managerauth/start.html')