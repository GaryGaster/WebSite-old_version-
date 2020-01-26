from django.shortcuts import render, redirect
from .forms import SingupForm

def singup(request):
    if request.method == "POST":
        form = SingupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('all_movies')
    else:
        form = SingupForm()

    return render(request, "accounts/singup.html", {"form":form})