from django.contrib import admin

from .models import Region, Central, Line, Trellis, Cabinet, Accumulations, Users

admin.site.register(Region)
admin.site.register(Central)
admin.site.register(Line)
admin.site.register(Trellis)
admin.site.register(Accumulations)
admin.site.register(Users)

