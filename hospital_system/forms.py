from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Patient


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label='First Name')
    last_name = forms.CharField(required=True, label='Last Name')
    phone = forms.CharField(required=False, label='Phone Number')
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(required=False, choices=[('M', 'Male'), ('F', 'Female')])
    blood_group = forms.ChoiceField(required=False, choices=[
        ('', 'Select Blood Group'),
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
    ])
    address = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Create associated Patient record
            Patient.objects.create(
                user=user,
                name=f"{user.first_name} {user.last_name}",
                email=user.email,
                phone=self.cleaned_data.get('phone', ''),
                date_of_birth=self.cleaned_data.get('date_of_birth'),
                gender=self.cleaned_data.get('gender', ''),
                blood_group=self.cleaned_data.get('blood_group', ''),
                address=self.cleaned_data.get('address', ''),
            )
        return user
