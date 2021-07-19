from django.forms import ModelForm
from .models import Managekey

class KeyManage(ModelForm):
    class Meta:
        model = Managekey
        fields = ['key', 'owner', 'tool', 'hsd', 'date_create', 'expiration_date']