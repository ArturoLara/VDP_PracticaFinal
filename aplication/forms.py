from django import forms


class NameForm(forms.Form):
    text = forms.CharField(label='Introduce Url', max_length=100, required=True,
                           widget=forms.Textarea(attrs={'rows': 1, 'cols': 76}))

    def getText(self):
        text = ""
        if 'execute' in self.data:
            text = self.cleaned_data['text']
        return text


class DateForm(forms.Form):
    date = forms.DateField(label='Introduce fecha formato YYYY-MM-DD', required=True)

    def getDate(self):
        date = ""
        if 'executeDate' in self.data:
            date = self.cleaned_data['date']
        return date