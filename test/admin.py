from django.contrib import admin

from .models import *

admin.site.register(Region)
admin.site.register(Central)
admin.site.register(Line)
admin.site.register(Pylon)
admin.site.register(Accumulation)
admin.site.register(Cabinet)

