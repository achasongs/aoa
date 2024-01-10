from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings

def mainapp(request):
  template = loader.get_template('mainapp/index.html')
 
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('mainapp/about.html')
 
  return HttpResponse(template.render())

def connect(request):
  if request.method == "POST":
    message_name = request.POST['name'].upper()
    message_email = request.POST['email']
    message_phone = request.POST['phone']
    message_title = request.POST['title'] 
    message_body = request.POST['body']

    # Send Email
    send_mail(
       message_title,    # subject
       f"from {message_email}\n {message_name}\n {message_phone}\n\n\n {message_body}",      # message
       message_email,
      ['adieleacha@gmail.com'],
        fail_silently=False   
    )

    return render(request, 'mainapp/connect.html', {
      'message_name': message_name
    })


  else:
    return render(request, 'mainapp/connect.html', {})
  

  
# def subscriber(request):
  
#   if request.method == "POST":
#     sub_email = request.POST['email']
#     sub_email.save()

#     # Send Email
#     send_mail(
#        'AOA',    # subject
#        'Thank you for Subscribing!\n We will regularly keep you informed on our services',      # message
#        sub_email,
#       ['sub_email'],
#         fail_silently=False   
#     )

#     return render(request, 'mainapp/index.html', {
#       'sub_email': sub_email
#     })


#   else:
#     return render(request, 'mainapp/index.html', {})
