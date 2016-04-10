from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from feasta.models import *
from feasta.config import *
from feasta.forms import *
from feasta import methods
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.debug import sensitive_post_parameters

class Home(TemplateView):
	template_name = 'home.html'
	def get_context_data(self,**kwargs):
		context = super(Home, self).get_context_data(**kwargs)
		context['user']=self.request.user
		return context
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		if not self.request.user.is_active:
			return HttpResponseRedirect(settings.LOGIN_URL)
		return super(Home,self).dispatch(*args,**kwargs)
class Login(FormView):
	form_class = LoginForm
	template_name = 'login.html'
	success_url = settings.LOGIN_REDIRECT_URL
		
	def form_valid(self,form):
		redirect_to = settings.LOGIN_REDIRECT_URL
        	login(self.request, form.get_user())
        	if self.request.session.test_cookie_worked():
           		self.request.session.delete_test_cookie()
        	return HttpResponseRedirect(redirect_to) 
	
	def form_invalid(self,form):	
		return super(Login, self).form_invalid(form)
	@method_decorator(sensitive_post_parameters())	
	def dispatch(self, *args, **kwargs):
		if self.request.user.is_active:
			return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
		return super(Login,self).dispatch(*args, **kwargs)
	def get_context_data(self, **kwargs):
			context = super(Login,self).get_context_data(**kwargs)
			context['form']=self.form_class
			return context

class UnregisterView(FormView):
	form_class = UnregisterForm
	template_name = 'unregister.html'
	def get_context_data(self, **kwargs):
		context=super(UnregisterView,self).get_context_data(**kwargs)
		context['form']=UnregisterForm
		context['session_end_days']=methods.getSessionEndDays()
		context['user']=self.request.user
		return context
	def form_valid(self,form):
		#form.cleaned_data[]
		return super(UnregisterView,self).form_valid(form)
	def form_invalid(self,form):	
		return super(UnregisterView,self).form_invalid(form)
class BulkUnregisterView(FormView):
	form_class = BulkUnregisterForm
	template_name = 'bulkunregister.html'
	def get_context_data(self, **kwargs):
		context=super(BulkUnregisterView,self).get_context_data(**kwargs)
		context['form']=BulkUnregisterForm
		context['session_end_days']=methods.getSessionEndDays()
		context['user']=self.request.user
		return context
	def form_valid(self,form):
		#form.cleaned_data[]
		return super(BulkUnregisterView,self).form_valid(form)
	def form_invalid(self,form):	
		return super(BulkUnregisterView,self).form_invalid(form)
				
class MenuView(TemplateView):
	template_name = 'menu.html'
	def get_context_data(self, **kwargs):
		context=super(MenuView,self).get_context_data(**kwargs)
		context['user']=self.request.user
		return context


class MyAccount(TemplateView):	
	template_name = 'myaccount.html'
	def get_context_data(self, **kwargs):
		context=super(MyAccount,self).get_context_data(**kwargs)
		context['user']=self.request.user
		return context
class EditProfile(FormView):
	template_name = 'editprofile.html'
	def get_context_data(self, **kwargs):
		context = super(EditProfile,self).get_context_data(**kwargs)
		context['user']=self.request.user
		return context
class ListForMeal(TemplateView):
	template_name = 'listformeal.html'	
	def get_context_data(self, **kwargs):
		context=super(ListForMeal,self).get_context_data(**kwargs)
		context['user']=self.request.user
		return context
	