from django.contrib import admin
from .models import Member, Chatroom


class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'online', 'avatar')
    list_filter = ('user', 'online',)


class ChatroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'dtcreate', 'owner',)
    list_filter = ('name', 'dtcreate', 'owner',)
    search_fields = ('name', 'owner',)


admin.site.register(Member, MemberAdmin)
admin.site.register(Chatroom, ChatroomAdmin)

