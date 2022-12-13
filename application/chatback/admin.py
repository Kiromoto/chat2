from django.contrib import admin
from .models import Member, Chatroom, Message


class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'address', 'phone', 'online',)
    list_filter = ('user', 'online',)
    search_fields = ('user', 'address', 'phone',)


class ChatroomAdmin(admin.ModelAdmin):
    list_display = ('creator', 'chatname',)
    list_filter = ('creator', 'chatname',)
    search_fields = ('creator', 'chatname',)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'text', 'datetimecreate', 'read', 'inchatroom')
    list_filter = ('sender', 'datetimecreate', 'read', 'inchatroom')
    search_fields = ('sender', 'text', 'datetimecreate', 'inchatroom')


admin.site.register(Member, MemberAdmin)
admin.site.register(Chatroom, ChatroomAdmin)
admin.site.register(Message, MessageAdmin)
