from django.shortcuts import render
from web_updater import web_updater
from BBDD import gestorBBDD
from .forms import NameForm, DateForm


def get_name(request):
    # if this is a POST request we need to process the form data
    text = ""
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            text = web_updater(form.getText())
        else:
            form = DateForm(request.POST)
            if form.is_valid():
                text = gestorBBDD().showData(form.getDate())

    form = NameForm()
    date = DateForm()

    return render(request, 'formHTML.html', {'form': form, 'answer': text, 'dateForm': date})
