from django.contrib import admin
from .models import Profile,Contact

admin.site.site_header='EDUTOTOP'
admin.site.site_title='EDUTOTOP'
admin.site.index_title='OVERVIEW'

admin.site.register(Profile)
admin.site.register(Contact)
