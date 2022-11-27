from django.contrib import admin
from .models import Facility, Club, Scholarship, Multimajor

# Register your models here.
admin.site.register(Facility)
admin.site.register(Club)
admin.site.register(Scholarship)
admin.site.register(Multimajor)