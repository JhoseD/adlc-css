from django import forms
from .models import client, project, requirement, task, rol, error, comment

class client_form(forms.ModelForm):
	class Meta:
		model = client
		fields = '__all__'


class project_form(forms.ModelForm):
	class Meta:
		model = project
		fields = '__all__'


class requirement_form(forms.ModelForm):
	class Meta:
		model = requirement
		fields = '__all__'


class task_form(forms.ModelForm):
	class Meta:
		model = task
		fields = '__all__'


class error_form(forms.ModelForm):
	class Meta:
		model = error
		fields = '__all__'


class comment_form(forms.ModelForm):
	class Meta:
		model = comment
		fields = '__all__'


class rol_form(forms.ModelForm):
	class Meta:
		model = rol
		fields = '__all__'
