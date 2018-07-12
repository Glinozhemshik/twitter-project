from django.contrib import admin

from .models import Twit


class TwitAdmin(admin.ModelAdmin):
    list_display = ("user", "text", "created_date")
    # list_editable = ("user",)
    search_fields = ["user__username", "created_date"]
    fields = ("user", "text", "created_date", "re_twit")
    list_filter = ("user",)



admin.site.register(Twit, TwitAdmin)
