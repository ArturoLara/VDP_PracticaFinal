from django import forms


class NameForm(forms.Form):
    text = forms.CharField(label='Introduce Url', max_length=100, required=False,
                           widget=forms.Textarea(attrs={'rows': 1, 'cols': 76}))
    date = forms.DateField()

    def getText(self):
        text = ""
        if 'execute' in self.data:
            text = self.cleaned_data['text']
        return text
