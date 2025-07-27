from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.home, login_url='/accounts/login/'), name='home'),
    path('quiz/<int:quiz_id>/', login_required(views.quiz_detail, login_url='/accounts/login/') , name='quiz_detail'),
]
