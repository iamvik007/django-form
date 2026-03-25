from django.shortcuts import render, redirect
from .form import ContactForm

def home(request):
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ContactForm()  # reset form after submit
    else:
        form = ContactForm()

    return render(request, 'formapp/home.html', {
        'form': form,
        'success': success
    })