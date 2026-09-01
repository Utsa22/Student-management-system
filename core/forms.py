from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student

class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        required=True
    )


    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


class StudentForm(forms.ModelForm):


    class Meta:

        model = Student

        fields = [
            'name',
            'email',
            'roll',
            'department',
        ]


    def clean_name(self):

        name = self.cleaned_data.get('name')

        if not name:

            raise forms.ValidationError(
                'Student name is required.'
            )

        name = name.strip()

        if len(name) < 3:

            raise forms.ValidationError(
                'Name must contain at least 3 characters.'
            )

        return name


    def clean_roll(self):

        roll = self.cleaned_data.get('roll')

        if roll is None:

            raise forms.ValidationError(
                'Roll number is required.'
            )

        if roll <= 0:

            raise forms.ValidationError(
                'Roll number must be greater than 0.'
            )

        return roll


    def clean_department(self):

        department = self.cleaned_data.get('department')

        if not department:

            raise forms.ValidationError(
                'Department is required.'
            )

        department = department.strip()

        if len(department) < 2:

            raise forms.ValidationError(
                'Department name is too short.'
            )

        return department