from django import forms
from .models import Contents,Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContentForm(forms.ModelForm):
    class Meta:
        model = Contents
        fields = '__all__'

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    


