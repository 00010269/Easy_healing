from django import forms

from .models import Medicine
from .models import Distribution

class PharmacyForm(forms.Form):
    # YES = "yes"
    # NO = "no"
    # IS_WORKING = (
    #     (YES, "yes"),
    #     (NO, "no")
    # )
    name = forms.CharField(max_length=1024)
    phone_number = forms.IntegerField(min_value=9)
    location = forms.CharField(max_length=1024)
    # is_working = forms.CharField(max_length=10, choices=IS_WORKING)


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = "__all__"



class DistributionForm(forms.ModelForm):
    class Meta:
        model = Distribution
        fields = "__all__"

