from django.contrib import admin

# Register your models here.

from .models import Candidates , Votes

admin.site.register(Candidates)
admin.site.register(Votes)