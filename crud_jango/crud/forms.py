
from django import forms
from .models import CrudData


class FormData(forms.ModelForm):
    class Meta:
        model=CrudData
        fields=["Name","Age","Email","Degree","Passed_out"]
        
    def __init__(self, *args, **kwargs):
        super(FormData, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = False
    
    def clean(self):
        cleaned_data=super().clean()
        Age = cleaned_data.get("Age")
        if Age is None:
            self.add_error('Age', "Age field cannot be empty.")
        # elif Age == '':
        #     self.add_error('Age', "Age field cannot be empty.")
        elif Age < 0:
            self.add_error('Age', "Age cannot be less than 0")
        Passed_out = cleaned_data.get("Passed_out")
        if Passed_out is None:
            self.add_error('Passed_out', "year of passed field cannot be empty.")
        elif Passed_out == '':
            self.add_error('Passed_out', "year of passed field cannot be empty.")
        elif Passed_out < 0:
            self.add_error('Passed_', "Age cannot be less than 0")
        Name = cleaned_data.get("Name")
        if not Name:
            self.add_error('Name', "Name field cannot be empty.")
        elif len(Name) < 3:
            self.add_error('Name', "Name should be more than 3 characters.")
        Email = cleaned_data.get("Email")
        if not Email:
            self.add_error('Email', "email field cannot be empty.")
        Degree = cleaned_data.get("Degree")
        if not Degree:
            self.add_error('Degree', "degree field cannot be empty.")
        