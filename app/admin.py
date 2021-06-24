from django.contrib import admin
from app.models import Channel,CountDown

# Register your models here.



class CountDownInline(admin.TabularInline):
    model = CountDown

class CountDownAdmin(admin.ModelAdmin):
    model=CountDown
    fields = ('channel', "c_happening", "c_status", "c_start")

class ChannelAdmin(admin.ModelAdmin):
    model=Channel
    inlines=[CountDownInline,]
    list_display = ("title","slack_id","related_countdowns")#"countdown")

admin.site.register(Channel)#,ChannelAdmin)
admin.site.register(CountDown)#,CountDownAdmin)