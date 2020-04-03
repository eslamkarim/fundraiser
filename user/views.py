import random, string
import smtplib
import re
from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import User


def home(request):
    return render(request, 'home/home.html')


def generate_sign_up_code():
    sign_up_code = random.getrandbits(32)
    return sign_up_code

def randomStringDigits(stringLength=11):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

def send_sign_up_validation_email(user_name, user_email_address):
    # vars to declare sending the email
    sender_email_address = 'fundraiser.charity.org@gmail.com'
    sender_email_password = 'Fundraiser.Charity.Org.Project'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(sender_email_address, sender_email_password)
    try:
        # getting the user key.
        user_sign_up_code = generate_sign_up_code()
       # user_sign_up_code = randomStringDigits()
        # Putting the user name and user code in the validation email to the user.
        reading_file = open("user/email_forms/email_validation_form.txt", "r")
        new_file_content = ""
        for line in reading_file:
            stripped_line = line.strip()
            if re.search('user_name,$', stripped_line):
                new_line = stripped_line.replace("user_name", "%s" % user_name)
                new_file_content += new_line + "\n"
            elif re.search('code_here$', stripped_line):
                new_line = stripped_line.replace("code_here", "%s" % user_sign_up_code)
                new_file_content += new_line + "\n"
            else:
                new_file_content += stripped_line + "\n"
        reading_file.close()
        # closing the final email message after processing
        final_email_body = open("user/email_forms/final_email_validation.txt", "w")
        final_email_body.write(new_file_content)
        final_email_body.close()

        with open('user/email_forms/final_email_validation.txt', 'r') as validation_message:
            email_body = validation_message.read()

        # clearing the file after getting the email body.
        writing_file = open("user/email_forms/final_email_validation.txt", "w")
        writing_file.write("")
        writing_file.close()
        # sending the email to the user with the body of signing up
        server.sendmail(sender_email_address, user_email_address, email_body)
        server.quit()

        return user_sign_up_code
    except:
        return False


def send_forgot_password_email(user_name, user_email_address, user_id):
    sender_email_address = 'fundraiser.charity.org@gmail.com'
    sender_email_password = 'Fundraiser.Charity.Org.Project'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(sender_email_address, sender_email_password)
    try:
        # sending the email to the user with the body of
        reading_file = open("user/email_forms/forgot_passowrd_form.txt", "r")
        new_file_content = ""
        for line in reading_file:
            stripped_line = line.strip()
            if re.search('user_name,$', stripped_line):
                new_line = stripped_line.replace("user_name", f"{user_name}")
                new_file_content += new_line + "\n"
            elif re.search('id_here$', stripped_line):
                new_line = stripped_line.replace("id_here", f"{user_id}")
                new_file_content += new_line + "\n"
            elif re.search('link_here$', stripped_line):
                new_line = stripped_line.replace("link_here", f"http://localhost:8000/updatepassowrd")
                new_file_content += new_line + "\n"
            else:
                new_file_content += stripped_line + "\n"
        reading_file.close()

        # closing the final email message after processing
        final_email_body = open("user/email_forms/final_forgot_password.txt", "w")
        final_email_body.write(new_file_content)
        final_email_body.close()

        with open('user/email_forms/final_forgot_password.txt', 'r') as validation_message:
            email_body = validation_message.read()

        # clearing the file after getting the email body.
        writing_file = open("user/email_forms/final_forgot_password.txt", "w")
        writing_file.write("")
        writing_file.close()
        # sending the email to the user with the body of signing up
        server.sendmail(sender_email_address, user_email_address, email_body)
        server.quit()
        return True
    except:
        print("Error sending the email..")
        return False


def check_password(password, conf_password):
    if password == '' or conf_password == '':
        return False;
    if password != conf_password:
        return False;
    if password == conf_password:
        return True;


def check_email(email_address):
    matcher = re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email_address)
    if matcher:
        return True
    return False


def check_phone(mobile_phone):
    matcher = re.search('^(010|011|015|012)([0-9]{8})', mobile_phone)
    if matcher:
        return True
    return False


def check_first_last_names(first_name, last_name):
    if first_name == '' or last_name == '':
        return False
    return True


@ensure_csrf_cookie
def sign_up(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone_number = request.POST.get("phone_number")
        email_address = request.POST.get("email")
        birthday=request.POST.get("birthday")
        password = request.POST.get("password")
        conf_password = request.POST.get("conf_password")

        user_full_name = first_name + " " + last_name
        if (check_first_last_names(first_name, last_name)) and \
                (check_phone(phone_number)) and (check_email(email_address)) and \
                (check_password(password, conf_password)):
            user = {
                'first_name': first_name,
                'last_name': last_name,
                'phone_number': phone_number,
                'email_address': email_address,
                'password': password,
                'conf_password': conf_password
            }

            validation_code = send_sign_up_validation_email(user_full_name, email_address)
            if validation_code:
                user_instance = User(user_first_name=first_name,
                                     user_last_name=last_name,
                                     user_email_address=email_address,
                                     user_password=password,
                                     user_birthDate=birthday,
                                     user_phone_number=phone_number,
                                     verification_code= validation_code)
                user_instance.save()
                return render(request, 'user/code_validation.html')
            else:
                return render(request, 'user/invalid_sign_up.html')
        else:
            return render(request, 'user/invalid_sign_up.html')
    return render(request, 'user/sign_up.html')


@ensure_csrf_cookie
def sign_in(request):
    if request.method == "POST":
        if request.POST.get('email') and request.POST.get('pass'):
            email = request.POST.get('email')
            password = request.POST.get('pass')
            try:
                logged_user = User.objects.get(user_email_address=email, user_password=password)
                if logged_user.is_verified_user:
                    request.session['logged_in_user'] = logged_user.user_id
                    return redirect('home')
                else:
                    return render(request, 'user/code_validation.html')
            except:
                return render(request, 'user/invalid_login.html')
    return render(request, 'user/sign_in.html')


def sign_out(request):
    try:
        del request.session['logged_in_user']
    except KeyError:
        pass
    return redirect('home')


def code_validation(request):
    if request.method == "POST":

        if request.POST.get('sign_up_code'):

            user_code = request.POST.get('sign_up_code')

            try:

                is_code_exist = User.objects.get(verification_code=int(user_code))
                print(is_code_exist)
                if is_code_exist:

                    User.objects.filter(verification_code=user_code, is_verified_user=False).update(is_verified_user=True)

                    return render(request, 'user/valid_code.html')
                else:
                    return render(request, 'user/invalid_code.html')
            except:

                return redirect("/") 
    return redirect("/") 


def is_email_exist(email):
    if email:
        try:
            is_exist = User.objects.get(user_email_address=email)
            if is_exist:
                return is_exist
        except:
            return False
    return False


@ensure_csrf_cookie
def forgot_password_form(request):
    if request.method == "POST":
        if request.POST.get('email'):
            forgot_password_email = request.POST.get('email')
            is_exist = is_email_exist(forgot_password_email)
            if is_exist:
                user_full_name = is_exist.user_first_name + " " + is_exist.user_last_name
                user_id = is_exist.user_id
                sent_forgot_password_email = send_forgot_password_email(user_full_name, forgot_password_email, user_id)
                if sent_forgot_password_email:
                    return render(request, 'user/forgot_password_message.html')
                return render(request, 'user/invalid_email.html')
            return render(request, 'user/invalid_email.html')
    return render(request, 'user/invalid_email.html')


# User.objects.filter(verification_code=user_code, is_verified_user=False).update(is_verified_user=True)
@ensure_csrf_cookie
def update_password(request):
    if request.method == "POST":
        if request.POST.get('user_id') and request.POST.get('password') and request.POST.get('conf_password'):
            user_id = request.POST.get('user_id')
            password = request.POST.get('password')
            conf_password = request.POST.get('conf_password')

            is_valid_password = check_password(password, conf_password)
            if is_valid_password:
                try:
                    User.objects.filter(user_id=user_id).update(user_password=password)
                    return render(request, 'user/updated_password_confirmation.html')
                except:
                    return render(request, 'user/error_updating_password.html')
            return render(request, 'user/invalid_password.html')
    return render(request, 'user/update_password.html')
