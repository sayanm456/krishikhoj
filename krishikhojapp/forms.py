from django import forms
from .models import Farmer


class FarmerForm(forms.ModelForm):
    class Meta:
       model = Farmer
       fields = '__all__'
       labels = {
          'name':'Full Name',
          'tractor_name':'Tractor Model',
          'registration_no':'Registration No',
          'contact_no': 'Contact No'
       }


    def __init__(self, *args, **kwargs):
        super(FarmerForm, self).__init__(*args, **kwargs)
        self.fields['tractor_name'].empty_label = "Select"   
        self.fields['registration_no'].required = "Select"   