from django import forms


class NameForm(forms.Form):
    text = forms.CharField(label='Introduce Texto', max_length=100, required=False,
                           widget=forms.Textarea(attrs={'rows': 5, 'cols': 25}))

    def getText(self):
        text = ""
        if 'execute' in self.data:
            text = self.cleaned_data['text']
        return text
