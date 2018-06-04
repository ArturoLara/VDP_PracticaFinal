from django.shortcuts import render
from web_updater import web_updater

from .forms import NameForm


def get_name(request):
    # if this is a POST request we need to process the form data
    text = ""
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            text = web_updater(form.getText())

    # if a GET (or any other method) we'll create a blank form

    form = NameForm()

    return render(request, 'formHTML.html', {'form': form, 'answer': text})
