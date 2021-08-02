from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import random
import array

# Create your views here.
def random_code():
    MAX_LEN = 12
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<', '[', ']']
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    # randomly select at least one character from each character set above
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
    password = ""
    for x in temp_pass_list:
        password = password + x
        return password


def signup_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        town = request.POST.get('town')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            #Enter the details to the db
            return render(request,"products/products.html")
        else:
            error_msg = "Passwords do not match!!"
            
    return render(request, 'accounts/signup.html')

def login_view(request):
    if request.method == "POST":
        user_mail = request.POST.get('uname')
        password_entered = request.POST.get('password')
        print(user_mail)
        print(password_entered)
        return render(request, "products/products.html")
    return render(request, 'accounts/login.html')

def reset_password(request):
    render(request, 'accounts/resetpassword.html')
    if request.method == "POST":
        user_mail = request.POST.get('usermail')
        if user_mail == db_mail_entered:
            relative_password = random_code()
            #update password to relative_password in db
            #send relative_password to the email of the user
            send_mail(
                'Change in password',
                'Your new password is '+relative_password+" use it to log in then you can change to your prefered password",
                'noreply@django-nabesh.com',
                [user_mail],
                fail_silently=False,
            )
            render(request, 'accounts/login.html')
        else:
            pass
