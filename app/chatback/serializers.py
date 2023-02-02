from .models import Member, Chatroom
from rest_framework import serializers


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['user', 'online', 'avatar']


class ChatroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatroom
        fields = ['name', 'dtcreate', 'owner', 'guests', ]
