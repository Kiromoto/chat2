from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction

from rest_framework import viewsets

from .models import Member, Chatroom
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from .serializers import MemberSerializer, ChatroomSerializer


class MemberView(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()


class ChatroomView(viewsets.ModelViewSet):
    serializer_class = ChatroomSerializer
    queryset = Chatroom.objects.all()


class AllMembersList(ListView):
    model = User
    ordering = 'username'
    template_name = 'allmemberslist.html'
    context_object_name = 'allmemberslist'
    paginate_by = 50


class AllChatsList(ListView):
    model = Chatroom
    ordering = 'name'
    template_name = 'allchatslist.html'
    context_object_name = 'allchatslist'
    paginate_by = 50


def show_profile(request, *args, **kwargs):
    return render(request, 'userinfo.html')


@login_required
@transaction.atomic
def update_profile(request, pk):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.member)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваш профиль был успешно обновлен!')
            return redirect('show_profile')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.member)
    return render(request, 'edituserinfo.html', context={'user_form': user_form, 'profile_form': profile_form})


def show_one_chat(request, pk):
    chat_one = get_object_or_404(Chatroom, pk=pk)
    chat_one_members = Chatroom.objects.get(pk=pk).guests.all()

    return render(request, 'chat.html',
                  context={'chat_one': chat_one, 'chat_one_members': chat_one_members, "room_name": pk})
