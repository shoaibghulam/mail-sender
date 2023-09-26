from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import EmailMultiAlternatives
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.mail import EmailMessage

from .models import *
# Create your views here.
def home(request):
    return render(request,'index.html')


def send(request):

    senduser=[]

    subject="Request for acceptance letter"
    from_email="danishbahoot@gmail.com"
    alluser=Users.objects.all()
    for user in alluser:

        to=user.email

        html_content = f'''
                <div style="font-size:18px; color:#000;">
    <p>Honorable {user.name}</p>
    <p>I hope you will be fine. </p>

    <p>My name is Danish Ali Raza from Pakistan. I have recently completed my M.Phil. (Mathematical Sciences) under Dr. Marium Sultana’s supervision from FUUAST, Karachi.</p>
    <p>
  I have thoroughly checked your profile; research work and it shows pretty relevance to my interest domain. Now I want to apply for a Ph.D. degree along with the Chinese Government Scholarship at {user.university} under your supervision.</p>
    <p>
   I attached my CV here. I would be glad to provide any further information if needed.
</p>
<p>
I know you will be busy, but if you can take out some time and give me a thoughtful response, I will be very thankful.
</p>
<p>
I'm looking forward to hearing back from you.

</p>

    <br>


    <p>Best regards<br>


    Danish Ali Raza
    </p>
                </div>
                    '''
        # print("my file is ",data.cv)
        msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        data=myFiles.objects.all()[0]
        msg.attach('Danish Ali Raza cv.pdf', data.cv.read(), 'application/pdf')
       

        # msg.attach('file.pdf', data.cv)
        # msg.attach(data.cv.name, data.cv.read(), data.cv.content_type)
        msg.send()
        # msg.close()
        senduser.append(user.name)
    request.session['mydata']=senduser
    alluser.delete()
    return redirect('/done')


def done(request):
    return render(request,'done.html')