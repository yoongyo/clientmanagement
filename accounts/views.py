from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import login, authenticate


def signin(request):
    # if request.COOKIES.get('username') is not None:
    #     username = request.COOKIES.get('username')
    #     password = request.COOKIES.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return HttpResponseRedirect(reverse('main'))
    #
    #     else:
    #         return render(request, 'accounts/login_fail.html')

    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('main'))
            response.set_cookie('username', username)
            response.set_cookie('password', password)
            return response

        else:
            return render(request, 'accounts/login_fail.html')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {
            'form': form
        })