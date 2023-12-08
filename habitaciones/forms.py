from django import forms
from  .models import Hab
class HabForm(forms.ModelForm):
    class Meta:
        model=Hab
        fields='__all__'