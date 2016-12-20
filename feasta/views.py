from django.shortcuts import render

# Create your views here.
def not_found(request):
	return render(request, '404.html', status=404)

def home(request):
	return render(request, 'theme.html')