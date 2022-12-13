from models import Member, Chatroom, Message
from rest_framework import serializers

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ['user', 'avatar', 'address', 'phone', 'online',]


class ChatroomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chatroom
        fields = ['creator', 'chatname', 'chatmember',]

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ['sender', 'text', 'datetimecreate', 'read', 'inchatroom',]
