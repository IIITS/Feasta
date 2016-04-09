from django.conf.urls import url
from feasta.views import *
from django.conf import settings
from django.contrib.auth.decorators import login_required

urlpatterns = [
			url(r'^$', login_required(Home.as_view())),
			url(r'^accounts/login/$', Login.as_view()),
			url(r'^unregister/$', login_required(UnregisterView.as_view())),
			url(r'^bulkunregister/$', login_required(BulkUnregisterView.as_view())),
			url(r'^menu/$', login_required(MenuView.as_view())),
			url(r'^accounts/signout/$', login_required(signout)),
			url(r'^accounts/change-password/$', login_required(changePassword)),
			url(r'^accounts/edit-profile/$', login_required(EditProfile.as_view())),
			url(r'^getlist/today/$', login_required(ListForMeal.as_view()))
		]