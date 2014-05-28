# -*- encoding: utf-8 -*-

from django import forms

from .models import Photo

class PhotoForm(forms.ModelForm):
	class Meta:
		model = Photo
		fields = ['title', 'image']

	def __init__(self, *args, **kwargs):		
		super(PhotoForm, self).__init__(*args, **kwargs)
		self.fields['title'].required = True
		self.fields['image'].required = True		