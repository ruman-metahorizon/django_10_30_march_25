"""
re_path configuration for blogs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls import include, re_path

# from django.conf.urls import url
from boards import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.home, name="home"),
    re_path(r"^about/$", views.about, name="about"),
    re_path(r"^questions/(?P<pk>\d+)/$", views.question, name="question"),
    re_path(r"^posts/(?P<slug>[-\w]+)/$", views.post, name="post"),
    re_path(r"^blog/(?P<slug>[-\w]+)-(?P<pk>\d+)/$", views.blog_post, name="blog_post"),
    re_path(
        r"^profile/(?P<username>[\w.@+-]+)/$", views.user_profile, name="user_profile"
    ),
    re_path(r"^articles/(?P<year>[0-9]{4})/$", views.year_archive, name="year"),
    # re_path(r'^$', views.home, name='home'),
    re_path(r"^boards/(?P<pk>\d+)/$", views.board_topics, name="board_topics"),
    re_path(r"^boards/(?P<pk>\d+)/new/$", views.new_topic, name="new_topic"),
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),
    
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),
    path("admin/", admin.site.urls),

    path(r'^new_post/$', views.NewPostView.as_view(), name='new_post'),
    path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
        views.PostUpdateView.as_view(), name='edit_post'),


    re_path(r"^signup/$", accounts_views.signup, name="signup"),
    re_path(r"^logout/$", auth_views.LogoutView.as_view(http_method_names = ['get', 'post', 'options']), name="logout"),
    re_path(
        r"^login/$",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
    
    re_path(
        r"^reset/$",
        auth_views.PasswordResetView.as_view(
            template_name="password_reset.html",
            email_template_name="password_reset_email.html",
            subject_template_name="password_reset_subject.txt",
        ),
        name="password_reset",
    ),
    re_path(
        r"^reset/done/$",
        auth_views.PasswordResetDoneView.as_view(
            template_name="password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path('reset/confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), 
        name="password_reset_confirm"),
    re_path(
        r"^reset/complete/$",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),



    re_path(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    re_path(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),
]
