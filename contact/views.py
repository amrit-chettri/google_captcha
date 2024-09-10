
from django.shortcuts import render, HttpResponse 
from .forms import ContactForm 

def contact(request): 
	if request.method == 'POST': 
		form = ContactForm(request.POST) 
		
		if form.is_valid(): 
			return HttpResponse("you are human") 
		else: 
			return HttpResponse("you are not human.") 
			
	else: 
		form = ContactForm() 
		
	return render(request, 'contact.html', {'form':form})
