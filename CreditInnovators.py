from django.shortcuts import render
#from django.http import HttpResponse
import datetime

# vars
# database
# SQL
credit_accounts = {
    "a1": {
        "moneytotal": 0,
        "credit_section": []
    },
    "a2": {
        "moneytotal": 0,
        "credit_section": []
    },
    "a3": {
        "moneytotal": 0,
        "credit_section": []
    }
}
accounts = {
    "a1": "x",
    "a2": "x",
    "a3": "x"
}

authenticated_accounts = {
    "a1": False,
    "a2": False,
    "a3": False
}

current_account = ""


# utils
def strip_input(s):
    return s.strip().lower()


def remove_input(s):
    return s.replace(" ", "").lower()


def my_input_str(s):
    input_s = input(s)
    return remove_input(input_s)


# logic
def login(ID_number, password)

):
print(f"Login with {ID_number} and {password}")
try:
    account_password = accounts[ID_number]
    is_authenticated = account_password == ID_number
    if is_authenticated:
        accounts[current_account] = False
        current_account = ID_number
        accounts[ID_number] = True
    return is_authenticated
except Exception as e:
    print(f"[LOG] Login failed with user: {ID_number}", e)
    return False


def current_date():
    return datetime.datetime.now().strftime("%X %a %x")


# This function logs for each account
def log1(account_name, time, money_1):
    credit = {}
    period[time] = current_date()
    credit[feature] = money_1
    current_credit = credit_accounts[account_name]["credit_section"]
    current_credit.append(credit)
    return current_credit


def get_credit(money):
    log("Time", "get_credit", money, credit_section)
    return moneytotal + money


def pay_loan(moneytotal, money):
    can_draw = (money < moneytotal) and (moneytotal > 0)
    if can_draw:
        log("Time", "pay_credit", -money, credit_section)
        return moneytotal - money

    return -1


def total_money(ID_number):
return bank_accounts[ID_number]["moneytotal"]


def account_credit_section(ID_number):
return bank_accounts[ID_number]["credit_section"]


def account_log1(ID_number):
log1(ID_number, "Time", "Balance", total_money(ID_number))

def account_log():
    log("Time", "Balance", moneytotal, credit_section)
    return credit_section


def web_print(request, s, authenticated):
    # return HttpResponse(s)
    context = {'message': s,
               'authenticated': authenticated,
               }
    return render(request, 'main/index.html', context)


def check_authenticated(account_name):
    """
    Returns True or False if user has logined before.
    """
    try:
        return authenticated_accounts[account_name]
    except:
        return False


# Create your views here.
def home(request):
    # input
    ID_number_input = request.GET.get('ID number')
    password_input = request.GET.get('password')

    authenticated = check_authenticated(current_account)
    if not authenticated:
        authenticated = login(ID_number_input, password_input)
        if not authenticated:
            return web_print(request, "ReEnter your ID number and password", authenticated)

    # input
    # We only get when we need it
    feature_input = request.GET.get('feature')
    value_input = request.GET.get('value')

    # feature=paycredit&value=12321
    is_get_credit = feature_input == "get credit"
    is_pay_loan = feature_input == "pay loan"
    is_log = feature_input == "log"
    is_end = feature_input == "end"

    if is_get_credit:
        # input
        # money = my_input_float(
        # ("the amount you want: "))
        try:
            money = float(value_input)
        except:
            return web_print(request, "The amount you entered is invalid.", authenticated)

        moneytotal = get_credit(money)
        return web_print(request, "Thank you for using FE Credit", authenticated)


    elif is_pay_loan:
        # input
        # money = my_input_float(
        # "The amount you pay: ")
        try:
            money = float(value_input)
        except:
            return web_print(request, "The amount you entered is invalid.", authenticated)

        # logic
        moneytotal = pay_loan(moneytotal, money)

        # output
        if (moneytotal == -1):
            s = f"Your balance is invalid, please deposit more to this account: {moneytotal}"
            return web_print(request, s)

            #return web_print(request, "Thank you for using FE Credit")

        elif is_log:
            print(credit_section)
            context = {
                'authenticated': authenticated,
                'credit_section': credit_section}
        return render(request, 'main/index.html', context)
        # return web_print("The system is upgrading, come back soon, thank you")
        # print("Print my credit balance: \n")
        # credit_section = account_log()
        # for i in range(len(credit_section)):
        # print(credit_section[i])

    elif is_end:
        # return web_print(credit_section)
        return web_print(request, "Thank you for using Credit Innovators.", authenticated)
        # print("End of transaction, your credit balance: ")

    return web_print(request, "Please check your credit scores, offer credit, pay credit, log, end", authenticated)

    # return HttpResponse(f"Empty")
    # return render(request, 'main/index.html')
    # return HttpResponse(f"Empty")