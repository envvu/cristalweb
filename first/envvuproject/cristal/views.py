from django.shortcuts import render

from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage





# Create your views here.

def index(request):
    return render(request, "index.html")


def introduction(request):
    return render(request, "introduction.html")


def management(request):
    return render(request, "management.html")


def directormessage(request):
    return render(request, "directors_msg.html")


def corecompetence(request):
    return render(request, "corecompetence.html")


def ourteam(request):
    return render(request, "ourteam.html")


def classIX(request):
    return render(request, "classIX.html")


def classX(request):
    return render(request, "classX.html")


def classXI(request):
    return render(request, "classXI.html")


def classXII(request):
    return render(request, "classXII.html")


def classXIIpass(request):
    return render(request, "classXIIpass.html")


def ibsbankcoaching(request):
    return render(request, "ibs-bank-coaching.html")


def result19_20(request):
    return render(request, "result-19-20.html")


def result18_19(request):
    return render(request, "result-18-19.html")


def result17_18(request):
    return render(request, "result-17-18.html")


def result16_17(request):
    return render(request, "result-16-17.html")


def result15_16(request):
    return render(request, "result-15-16.html")


def result14_15(request):
    return render(request, "result-14-15.html")


def result13_14(request):
    return render(request, "result-13-14.html")


def result12_13(request):
    return render(request, "result-12-13.html")


def result11_12(request):
    return render(request, "result-11-12.html")


def contactus(request):
    return render(request, "contactus.html")





def testimonials(request):
    return render(request,"testimonials.html")


def terms_and_conditions(request):
    return render(request, "terms_and_conditions.html")


def refund_policy(request):
    return render(request, "refund-policy.html")


def privacy_policy(request):
    return render(request, "privacy-policy.html")


def home_2(request):
    return render(request,"home_2.html")

def admission(request):
    return render(request,'admission_open.html')



'''def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        template = get_template('contactus2.txt')
        context = {'name':name,'email':email,'phone':phone,'message':message}
        content = template.render(context)
        email = EmailMessage(
            "contact from recieved",
            content,
            "contact from "+'',
            ['envvumarketing3@gmail.com','envvumarketing6@gmail.com'],
            headers = {'Reply to ':email}

        )
        email.send()
        messages.success(request,+'thank you for contacting us')
    return render(request,'contactus.html')'''


def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')


        data = {
            'name': name,
            'email': email,
            'phone': phone,
            'message': message,
        }
        print(data)

        message = '''

         Name: {}

         Email: {}

         phone: {}

         message: {}

        '''.format(data['name'], data['email'], data['phone'], data['message'])
        send_mail('ENQUIRY', message, '',
                  ['envvumarketing6@gmail.com','envvumarketing3@gmail.com'])

        html = "<html><body><br><br><h2>ThankYou For Submitting Registration form.</h2></body></html>"
        return HttpResponse(html)

    return render(request, "contactus.html", {})


def form1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        schoolname = request.POST.get('schoolname')
        parentname = request.POST.get('parentname')
        parentnumber = request.POST.get('parentnumber')
        board = request.POST.get('board')
        email=request.POST.get('email')
        test = request.POST.get('test')


        '''except MultiValueDictKeyError:
            phone = False
            message = False'''
        template = get_template('form1.txt')
        context = {'name': name, 'number':number,'schoolname':schoolname,'parentname':parentname,'parentnumber':parentnumber,'board':board,'test':test ,'email':email}
        print(context)
        content = template.render(context)
        print(content)
        email = EmailMessage(
            "Contact form Recieved",
            content,
            "Contact Form" + '',
            ['envvumarketing3@gmail.com', 'envvumarketing6@gmail.com'],
            headers={'Reply To': email}
        )
        email.send()
        # messages.success(request, f'Thank You For Contacting Us , Our Executive Will Contact You Soon')
        html = "<html><body><h2>Thank You For Contacting Us , Our Executive Will Contact You Soon</h2><br> <a href='https://www.newcristalacademy.com/'><h2>Home</h2></a> </body></html> "
        return HttpResponse(html)
    return render(request, 'form1.html')




def form2(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        standard = request.POST.get('standard')
        schoolname = request.POST.get('schoolname')
        wnumber = request.POST.get('wnumber')
        email = request.POST.get('email')
        parentno = request.POST.get('parentno')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        tuition = request.POST.get('tuition')
        subject = request.POST.getlist('subject[]')
        print(subject)

        '''except MultiValueDictKeyError:
            phone = False
            message = False'''
        template = get_template('form2.txt')
        context = {'name': name, 'email': email, 'standard': standard, 'schoolname': schoolname, 'wnumber': wnumber,
                   'parentno': parentno, 'address': address, 'city': city, 'state': state, 'country': country,
                   'tuition': tuition, 'subject': subject, }
        print(context)
        content = template.render(context)
        print(content)
        email = EmailMessage(
            "Contact form Recieved",
            content,
            "Contact Form" + '',
            ['envvumarketing3@gmail.com', 'envvumarketing6@gmail.com'],
            headers={'Reply To': email}
        )
        email.send()
        # messages.success(request, f'Thank You For Contacting Us , Our Executive Will Contact You Soon')
        html = "<html><body><h2>Thank You For Contacting Us , Our Executive Will Contact You Soon</h2><br> <a href='https://www.newcristalacademy.com/'><h2>Home</h2></a> </body></html> "
        return HttpResponse(html)
    return render(request, 'form2.html')


def form3(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        schoolname = request.POST.get('schoolname')
        grades = request.POST.get('grades')
        number = request.POST.get('number')
        email=request.POST.get('email')
        parentname = request.POST.get('parentname')
        parentnumber =request.POST.get('parentnumber')


        '''except MultiValueDictKeyError:
            phone = False
            message = False'''
        template = get_template('form3.txt')
        context = {'name': name, 'number':number,'schoolname':schoolname,'parentname':parentname,'parentnumber':parentnumber,'grades':grades ,'email':email}
        print(context)
        content = template.render(context)
        print(content)
        email = EmailMessage(
            "Contact form Recieved",
            content,
            "Contact Form" + '',
            ['envvumarketing3@gmail.com', 'envvumarketing6@gmail.com'],
            headers={'Reply To': email}
        )
        email.send()
        # messages.success(request, f'Thank You For Contacting Us , Our Executive Will Contact You Soon')
        html = "<html><body><h2>Thank You For Contacting Us , Our Executive Will Contact You Soon</h2><br> <a href='https://www.newcristalacademy.com/'><h2>Home</h2></a> </body></html> "
        return HttpResponse(html)
    return render(request, 'form3.html')



def form4(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        add1 = request.POST.get('add1')
        add2 = request.POST.get('add2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        wnumber = request.POST.get('wnumber')
        parent = request.POST.get('parent')
        parentjob = request.POST.get('parentjob')
        parentph = request.POST.get('parentph')
        schoolname = request.POST.get('schoolname')
        std = request.POST.get('std')
        board = request.POST.get('board')
        entrance = request.POST.get('entrance')
        us = request.POST.get('us')



        '''except MultiValueDictKeyError:
            phone = False
            message = False'''
        template = get_template('form4.txt')
        context = {'name': name, 'dob': dob, 'gender': gender, 'add1': add1, 'add2': add2,
                   'city': city, 'state': state, 'pin': pin, 'email': email, 'wnumber': wnumber,
                   'parent': parent, 'parentjob': parentjob, 'parentph': parentph, 'schoolname': schoolname,
                   'std': std, 'board': board, 'entrance': entrance, 'us': us}

        print(context)
        content = template.render(context)
        print(content)
        email = EmailMessage(
            "Contact form Recieved",
            content,
            "Contact Form" + '',
            ['envvumarketing3@gmail.com', 'envvumarketing6@gmail.com'],
            headers={'Reply To': email}
        )
        email.send()
        # messages.success(request, f'Thank You For Contacting Us , Our Executive Will Contact You Soon')
        html = "<html><body><h2>Thank You For Contacting Us , Our Executive Will Contact You Soon</h2><br> <a href='https://www.newcristalacademy.com/'><h2>Home</h2></a> </body></html> "
        return HttpResponse(html)
    return render(request, 'form4.html')




def regform(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        sdate = request.POST.get('sdate')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        school = request.POST.get('school')
        place = request.POST.get('place')
        pname = request.POST.get('pname')
        pemail = request.POST.get('pemail')
        pphone = request.POST.get('pphone')
        sclass = request.POST.get('sclass')
        board = request.POST.get('board')


        '''except MultiValueDictKeyError:
            phone = False
            message = False'''
        template = get_template('regform.txt')
        context = {'name': name, 'sdate': sdate, 'school': school, 'pname': pname, 'pphone': pphone, 'board': board,
                   'phone': phone, 'email': email, 'place': place, 'pemail': pemail, 'sclass': sclass}
        print(context)
        content = template.render(context)
        print(content)
        email = EmailMessage(
            "Contact form Recieved",
            content,
            "Contact Form" + '',
            ['envvumarketing3@gmail.com', 'envvumarketing6@gmail.com'],
            headers={'Reply To': email}
        )
        email.send()
        # messages.success(request, f'Thank You For Contacting Us , Our Executive Will Contact You Soon')
        html = "<html><body><h2>Thank You For Contacting Us , Our Executive Will Contact You Soon</h2><br> <a href='https://www.newcristalacademy.com/'><h2>Home</h2></a> </body></html> "
        return HttpResponse(html)
    return render(request, 'regnform.html')





def onlinereg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        wapp = request.POST.get('wapp')
        email = request.POST.get('email')
        school = request.POST.get('school')
        place = request.POST.get('place')
        pname = request.POST.get('pname')
        pemail = request.POST.get('pemail')
        pphone = request.POST.get('pphone')
        course =request.POST.get('course')
        sclass = request.POST.get('sclass')
        stream = request.POST.get('stream')


        '''except MultiValueDictKeyError:
            phone = False
            message = False'''
        template = get_template('onlinereg.txt')
        context = {'name': name, 'dob': dob, 'school': school, 'pname': pname, 'pphone': pphone, 'course': course,
                   'wapp': wapp, 'email': email, 'place': place, 'pemail': pemail, 'sclass': sclass,'stream':stream}
        print(context)
        content = template.render(context)
        print(content)
        email = EmailMessage(
            "Contact form Recieved",
            content,
            "Contact Form" + '',
            ['envvumarketing3@gmail.com', 'envvumarketing6@gmail.com'],
            headers={'Reply To': email}
        )
        email.send()
        # messages.success(request, f'Thank You For Contacting Us , Our Executive Will Contact You Soon')
        html = "<html><body><h2>Thank You For Contacting Us , Our Executive Will Contact You Soon</h2><br> <a href='https://www.newcristalacademy.com/'><h2>Home</h2></a> </body></html> "
        return HttpResponse(html)
    return render(request, 'online_regnform_tutions.html')









