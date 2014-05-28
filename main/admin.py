from django.contrib import admin
from .models import Photo

def publish(modeladmin, request, queryset):
    queryset.update(published=True)
publish.short_description = u'Opublikuj zaznaczone'

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'published')
    list_filter = ('date', 'published')
    search_fields = ('title',)
    actions = (publish,)
    raw_id_fields = ('user',)
    fields = ('user', ('title', 'image'), 'published')

admin.site.register(Photo, PhotoAdmin)