from django import forms
from .models import Club, Facility

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'category', 'content', 'tel_number', 'image', 'url']
        widgets = {
            'name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '동아리 이름',
                },
            ),
            'content' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '본문',
                },
            ),
            'tel_number' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '전화번호',
                },
            ),
            'url' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '관련 URL',
                },
            )
        }
        labels = {
            'name' : '동아리 이름',
            'catrgory' : '카테고리',
            'content' : '내용',
            'tel_number' : '전화번호',
            'image' : '이미지',
            'url' : '관련 URL'
        }
        
class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['name', 'category', 'content', 'tel_number', 'image', 'url']
        widgets = {
            'name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '시설 이름',
                },
            ),
            'content' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '본문',
                },
            ),
            'tel_number' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '전화번호',
                },
            ),
            'url' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '지도 URL',
                },
            )
        }
        labels = {
            'name' : '동아리 이름',
            'catrgory' : '카테고리',
            'content' : '내용',
            'tel_number' : '전화번호',
            'image' : '이미지',
            'url' : '지도 URL'
        }