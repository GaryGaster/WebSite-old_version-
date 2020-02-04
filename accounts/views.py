from django.shortcuts import render, redirect
from .forms import SingupForm
from django.contrib import messages

def singup(request):
    if request.method == "POST":
        form = SingupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Zarejestrowano nowego użytkownika {username}!')
        return redirect('login')
    else:
        form = SingupForm()

    return render(request, "accounts/singup.html", {"form":form})