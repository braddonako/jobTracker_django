from django.contrib import admin
# import your models here
from .models import Job, Note, Upload

# Register your models here
admin.site.register(Job)
admin.site.register(Note)
admin.site.register(Upload)

