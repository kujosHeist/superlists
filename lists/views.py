from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Item

# Create your views here.

def home_page(request):

	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/')
	
	# return render(request, 'lists/home.html', {
	# 	'new_item_text': new_item_text
	# })
	return render(request, 'lists/home.html')
	

	