from django import forms

from MyLibrary.models import my_library, authors

class libraryForm(forms.ModelForm):
    class Meta:
        model = my_library
        fields = ['book_name', 'author', 'year', 'pages']

class authorsForm(forms.ModelForm):
    class Meta:
        model = authors
        fields = ['surname', 'name', 'birthday']