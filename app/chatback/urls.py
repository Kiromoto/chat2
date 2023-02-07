from django.urls import path
from .views import MemberView, ChatroomView, AllMembersList, AllChatsList
from .views import show_profile, update_profile, show_one_chat, show_chatrooms
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from rest_framework.documentation import include_docs_urls

# chatback\urls.py
router = DefaultRouter()
router.register(r'members', MemberView, basename='memberurl')
router.register(r'chatrooms', ChatroomView, basename='chatroomurl')

app_name_member = "members"
app_name_chatroom = "chatrooms"

urlpatterns = [path('profile/', show_profile, name='show_profile'),
               path('editmyprofile/<int:pk>', update_profile, name='update_profile'),
               path('allmembers/', AllMembersList.as_view(), name='allmemberslist'),
               path('allchats/', AllChatsList.as_view(), name='allchatslist'),
               path('chat/<int:pk>', show_one_chat, name='chat'),
               path('crooms/', show_chatrooms, name='show_chatrooms'),
               # path('docs/', include_docs_urls(title='My API service'), name='api-docs'),
               ] + router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
