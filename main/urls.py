from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import by_rubric, profile, profile_bb_add, profile_bb_delete, profile_bb_edit, profile_bb_detail, profile_bb_change
from .views import index
from .views import other_page
from .views import BBLoginView
from .views import BBLogoutView
from .views import ChangeUserInfoView
from .views import BBPasswordChangeView
from .views import RegisterUserView, RegisterDoneView
from .views import user_activate
from .views import DeleteUserView
from .views import detail

app_name = 'main'
urlpatterns = [
    path('accounts/register/activate/<str:sign>/', user_activate,
                                                   name='register_activate'),
    path('accounts/register/done/', RegisterDoneView.as_view(),
                                    name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(),name='register'),

    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(),
                                      name='password_change'),
    path('accounts/profile/delete/', DeleteUserView.as_view(),
                                     name='delete_user'),
    path('accounts/profile/edit/<int:pk>/', profile_bb_edit,
                                            name='profile_bb_edit'),
    path('accounts/profile/change/<int:pk>/', profile_bb_change, name='profile_bb_change'),                                            
    path('accounts/profile/delete/<int:pk>/', profile_bb_delete,
                                              name='profile_bb_delete'),
    path('accounts/profile/add/', profile_bb_add, name='profile_bb_add'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(),
                                     name='profile_change'),
    path('accounts/profile/<int:pk>/', profile_bb_detail,
                                       name='profile_bb_detail'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('<int:rubric_pk>/<int:pk>/', detail, name='detail'),
    path('<int:pk>/', by_rubric, name='by_rubric'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index')
]