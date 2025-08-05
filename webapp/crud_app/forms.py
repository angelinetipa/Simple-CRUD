from django import forms
from .models import Customer_Record

class Add_Record(forms.ModelForm):  # transform html code from home to django and data from model
    
    last_name = forms.CharField(required=True,
        widget=forms.TextInput(attrs={
        'placeholder': 'Last name',
        'class': 'form-control'}),
        label=''
        )
    
    first_name = forms.CharField(required=True,
        widget=forms.TextInput(attrs={
        'placeholder': 'First name',
        'class': 'form-control'}),
        label=''
        )
    
    middle_name = forms.CharField(required=False,
        widget=forms.TextInput(attrs={
        'placeholder': 'Middle name',
        'class': 'form-control'}),
        label=''
        )
    
    suffix = forms.ChoiceField(required=False,
        choices=[('','Select Suffix')] + list(Customer_Record.SUFFIXES),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label=''
        )
    
    gender = forms.ChoiceField(required=True,
        choices=[('','Select Gender')] + list(Customer_Record.GENDER),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label=''
        )
    
    email = forms.CharField(required=False,
        widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control'}),
        label=''
        )
    
    phone = forms.CharField(required=False,
        widget=forms.TextInput(attrs={
        'placeholder': 'Phone',
        'class': 'form-control'}),
        label=''
        )
    
    address = forms.CharField(required=True,
        widget=forms.TextInput(attrs={
        'placeholder': 'Address',
        'class': 'form-control'}),
        label=''
        )
    
    brgy = forms.ChoiceField(required=True,
        choices=[('','Select Barangay')] + list(Customer_Record.BRGY_CHOICES),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label=''
        )
    
    upload_image = forms.ImageField(required=False, label=''
        )

    class Meta: # designate what model to use
        model = Customer_Record
        exclude = ('user',) # exclude the user and include all the field in form serializer 