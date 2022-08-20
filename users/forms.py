from django import forms
from .models import User, Profile


class RegisterForm(forms.Form):
    username = forms.CharField(label='User name', max_length=80)
    first_name = forms.CharField(label='First Name', max_length=80)
    last_name = forms.CharField(label='Last Name', max_length=80)
    phone_number = forms.IntegerField(label='Phone Number')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)
    radio_buttons = forms.ChoiceField(
        choices=(
            ('is_landlord', "Landlord"),
            ('is_student', "Student")
        ),
        widget=forms.RadioSelect,
        label='Select your status'
    )
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'is_landlord', 'is_student', 'phone_number']
    
    
    def save(self, commit=True):
        User = super().save(commit=False)
        User.set_password(self.cleaned_data["password"])
        if commit:
            User.save()
        return User
    


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(label='User name', max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']



class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']