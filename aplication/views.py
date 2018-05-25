from django.shortcuts import render
from text_data_miner import text_data_miner

from .forms import NameForm


def get_name(request):
    # if this is a POST request we need to process the form data
    text = ""
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            text = text_data_miner(form.getText())

    # if a GET (or any other method) we'll create a blank form

    form = NameForm()

    return render(request, 'formHTML.html', {'form': form, 'answer': text})
