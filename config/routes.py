"""market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from api.views.admin.book_views import BookView as AadminBookView
from api.views.admin.tag_views import TagView as AdminTagView

from api.views.user_view import UserView
from api.views.token_view import TokenView

api_path = 'api/'
admin_path = 'admin/'
urlpatterns = [
    path(api_path + 'user', UserView.as_view()),
    path(api_path + 'login', TokenView.login),

    path(api_path + admin_path + 'books', AadminBookView.as_view()),
    path(api_path + admin_path + 'books/<int:id>', AadminBookView.as_view()),

    path(api_path + admin_path + 'tags', AdminTagView.as_view()),
    path(api_path + admin_path + 'tags/<str:name>', AdminTagView.as_view()),
]
