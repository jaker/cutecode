from django import forms
from models import Language

attrs_dict = {}

class AddCodeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AddCodeForm, self).__init__(*args, **kwargs)
        self.fields['language'].choices = [('', '----------')] + [(lang.id, lang.name) for lang in Language.objects.all()]
    
    title = forms.CharField(max_length=250, widget=forms.TextInput(attrs=attrs_dict))
    description = forms.CharField(widget=forms.Textarea(attrs=attrs_dict))
    source = forms.CharField(widget=forms.Textarea(attrs=attrs_dict))
    tag_list = forms.CharField(max_length=250, widget=forms.TextInput(attrs=attrs_dict))
    language = forms.ChoiceField(choices=(), widget=forms.Select(attrs=attrs_dict))


class EditCodeForm(forms.Form):
    title = forms.CharField(max_length=250, widget=forms.TextInput(attrs=attrs_dict))
    description = forms.CharField(widget=forms.Textarea(attrs=attrs_dict))
    source = forms.CharField(widget=forms.Textarea(attrs=attrs_dict))
    tag_list = forms.CharField(max_length=250, widget=forms.TextInput(attrs=attrs_dict))
