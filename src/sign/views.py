from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'index.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect('/event_manage/')
            # response.set_cookie('user', username, 3600)
            request.session['user'] = username
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password errors.'})


@login_required
def event_manage(request):
    # username = request.COOKIES.get('user', '')
    username = request.session.get('user', '')
    return render(request, "event_manage.html", {'user': username})
