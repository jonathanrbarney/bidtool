import django.forms as forms
from bidtool.models import *
class embassySearch(forms.ModelForm):
    class Meta:
        model = Embassy
        fields = ('name',)