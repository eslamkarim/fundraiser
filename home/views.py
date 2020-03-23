from django.shortcuts import render
import re
# Create your views here.


def home(request):
    return render(request,'home/home.html')


def check_password(password, conf_password):
    if password == '' | conf_password == '':
        return False;
    elif password != conf_password:
        return False;
    elif password == conf_password:
        return True;


def check_email(email_address):
    matcher = re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email_address)
    if matcher:
        if send_validation_email(email_address):
            return True
        return False
    return False


def send_validation_email(email_address):
    # Here is to send a code to this email address and to insert this code in the database (col: sign_up_code:###)
    # The first time the user logs into the system, there will be a page for the user to insert this code
    # Inserted correctly the code col in the database will be marked as validated
    return True


def check_phone(mobile_phone):
    matcher = re.search('^(010|011|015|012)([0-9]{8})', mobile_phone)
    if matcher:
        return True
    return False


def check_first_last_names(first_name, last_name):
    if first_name == '' | last_name == '':
        return False
    return True


def sign_up(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        email_address = request.POST['email']
        password = request.POST['password']
        conf_password = request.POST['conf_password']

        if (check_first_last_names(first_name, last_name)) & \
                (check_phone(phone_number)) & (check_email(email_address)) & \
                (check_password(password, conf_password)):
            user = {
                'first_name': first_name,
                'last_name': last_name,
                'phone_number': phone_number,
                'email_address': email_address,
                'password': password,
                'conf_password': conf_password
            }
            return user;
        else:
            return False;


def sign_in(email, password):
    # select from the database and get
    selected_user = "select from the database in this variable.. based on the given email and password."
    if (email == email &
            password == password):
        logged_in_user = {
            'first_name': 'first_name',
            'last_name': 'last_name',
            'phone_number': 'phone_number',
            'email_address': 'email_address',
            'password': 'password',
            'conf_password': 'conf_password'
        }
        return logged_in_user;
    return False;