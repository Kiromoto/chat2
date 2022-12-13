from django.contrib.auth.models import User
from .models import Member, Chatroom, Message


# def navigate_context(request, *args, **kwargs):
#     category_type = Ad.TYPE
#     current_user = request.user
#     isaut = True if current_user.is_authenticated else False
#     responses = Response.objects.all()
#     allusers =  User.objects.all()
#     aut = []
#     for u in allusers:
#         print(u.is_authenticated)
#         aut.append(u.is_authenticated)
#
    # context = {
    #     **super().get_context_data(*args, **kwargs),
#         'responses': responses,
#         'category_type': category_type,
#         'current_user': current_user,
#         'isaut': isaut,
#         'allusers': allusers,
#         'aut': aut,
#     }
#
    # return context
#
#
# def get_user(request):
#     return request.user