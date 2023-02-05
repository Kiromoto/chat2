from .models import Member, Chatroom
from rest_framework import serializers


class MemberSerializer(serializers.ModelSerializer):
    ownchatrooms = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    guestofchatrooms = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Member
        fields = ['user', 'online', 'avatar', 'ownchatrooms', 'guestofchatrooms', ]


class ChatroomSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.user.username')

    class Meta:
        model = Chatroom
        fields = ['name', 'dtcreate', 'owner', 'guests', ]
