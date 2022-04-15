from django.shortcuts import render 
from.forms import ContactForm 
from django.core.mail import send_mail 
 
def contactview (request):
  name = '' 
  email = '' 
  comment = '' 
 
  form = ContactForm (request.POST or None) 
  if form.is_valid ():
        name = form.cleaned_data.get ("name") 
        email = form.cleaned_data.get ("email") 
        comment = form.cleaned_data.get ("comment") 
 
 
    comment = name + " with the email, " + email + ", sent the following message:\n\n" + comment;

    send_mail ('The title of this post', comment, 'admin@gmail.com', ['admin@gmail.com']) 
 
 
    context = {'form':form}
    return render(request, 'contact/contact.html', context)
else:
    context = {'form':form}
    return render(request, 'contact/contact.html', context) 
