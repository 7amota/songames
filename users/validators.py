from django import forms
def passwdvalidate(value):
    if len(value) < 6:
        raise forms.ValidationError("be sure the password is more than 6 letters")