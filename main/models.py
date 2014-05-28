# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
	user = models.ForeignKey(User, null=False, blank=False, verbose_name=u'Użytkownik')
	title = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'Tytuł')
	date = models.DateTimeField(auto_now_add=True, null=False, blank=False, verbose_name=u'Data')
	image = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name=u'Obraz')
	published = models.BooleanField(default=False, verbose_name=u'Opublikowane')

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name_plural = u'Zdjęcia'
		verbose_name = u'Zdjęcie'
        
