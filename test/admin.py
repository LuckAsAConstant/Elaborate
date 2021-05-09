from django.contrib import admin

from .models import Region, City, Central, Line, trellis

admin.site.register(Region)
admin.site.register(City)
admin.site.register(Central)
admin.site.register(Line)
admin.site.register(trellis)

