from django import forms
from forms_app.models import Contatto


class FormContatto(forms.ModelForm):
    class Meta:
        model = Contatto
        fields = "__all__"
