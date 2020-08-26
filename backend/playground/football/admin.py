from django.contrib import admin
from football.models import Competition, Team, Manager, Player, Stadium


admin.site.register(Competition, admin.ModelAdmin)
admin.site.register(Team, admin.ModelAdmin)
admin.site.register(Manager, admin.ModelAdmin)
admin.site.register(Player, admin.ModelAdmin)
admin.site.register(Stadium, admin.ModelAdmin)
