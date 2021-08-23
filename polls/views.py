from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

from .forms import RegistrationForm, CarbonRegistration, LoginForm, AccountForm, PaymentForm
from .models import RegistrationData, CarbonData, AccountDetails, PaymentData


def register(request):
    context = {
        "form": RegistrationForm
    }
    return render(request, 'signup.html', context)


def addUser(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        myRegister = RegistrationData(company=form.cleaned_data['company'],
                                      password=form.cleaned_data['password'],
                                      email=form.cleaned_data['email'],
                                      phone=form.cleaned_data['phone'],
                                      country=form.cleaned_data['country'],
                                      address=form.cleaned_data['address'],
                                      reg_no=form.cleaned_data['reg_no'],
                                      employees=form.cleaned_data['employees'],
                                      sector=form.cleaned_data['sector'],
                                      turnover=form.cleaned_data['turnover'],
                                      )
        myRegister.save()
        request.session['reg_id'] = myRegister.id
    return redirect('polls:account')


def LogInPage(request):
    context = {
        "name": "cliommit",
        "form": LoginForm
    }
    return render(request, 'login.html', context)


def loginValidation(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        company = form.cleaned_data['company']
        if RegistrationData.objects.filter(company=company):
            user = RegistrationData.objects.get(company=company)
            if user.password == form.cleaned_data['password']:
                return redirect('polls:home', user.id)
            else:
                print("invalid password")
        else:
            print("invalid username")
    return redirect('polls:login')


def Home(request, id):
    user = RegistrationData.objects.get(id=id)
    # if CarbonData.objects.filter(user_id=id).exists():
    #     carbon_data = CarbonData.objects.get(user_id=id)
    #     emmissions = float(carbon_data.electricity_amount) * 0.706
    #     c_bool = True
    # else:
    #     emmissions = 0
    #     c_bool = False
    # cost = emmissions * 0.05
    request.session['project_id'] = id
    context = {
        "user": user,
        # "carbon_exists": c_bool,
        # "emmissions": emmissions,
        # "cost": cost
    }
    return render(request, 'home.html', context)


def carbonRegistration(request):
    id = request.session.get('project_id')
    registry = RegistrationData.objects.get(id=id)
    context = {
        "form": CarbonRegistration,
        "registry": registry
    }
    return render(request, 'carbon-registration.html', context)


def addCarbonData(request):
    form = CarbonRegistration(request.POST)
    id = request.session.get('project_id')
    if form.is_valid():
        myCarbonData = CarbonData(user=RegistrationData.objects.get(id=id),
                                  electricity_amount=form.cleaned_data['electricity_amount'],
                                  electricity_renewable=form.cleaned_data['electricity_renewable'],
                                  electricity_provider=form.cleaned_data['electricity_provider'],
                                  electricity_type=form.cleaned_data['electricity_type'],
                                  electricity_heating=form.cleaned_data['electricity_heating'],
                                  electricity_gas=form.cleaned_data['electricity_gas'],
                                  travel_air_travel_long=form.cleaned_data['travel_air_travel_long'],
                                  travel_air_travel_short=form.cleaned_data['travel_air_travel_short'],
                                  travel_automobile_mileage=form.cleaned_data['travel_automobile_mileage'],
                                  travel_automobile_commute=form.cleaned_data['travel_automobile_commute'],
                                  travel_bus=form.cleaned_data['travel_bus'],
                                  travel_coach=form.cleaned_data['travel_coach'],
                                  travel_train=form.cleaned_data['travel_train'],
                                  travel_int_train=form.cleaned_data['travel_int_train'],
                                  travel_subway=form.cleaned_data['travel_subway'],
                                  travel_tram=form.cleaned_data['travel_tram'],
                                  travel_taxi=form.cleaned_data['travel_taxi'],
                                  travel_accommodation_hotel=form.cleaned_data['travel_accommodation_hotel'],
                                  travel_accommodation_motel=form.cleaned_data['travel_accommodation_motel'],
                                  travel_accommodation_airbnb=form.cleaned_data['travel_accommodation_airbnb'],
                                  office_utilities_desktop=form.cleaned_data['office_utilities_desktop'],
                                  office_utilities_laptop=form.cleaned_data['office_utilities_laptop'],
                                  office_waste_bio=form.cleaned_data['office_waste_bio'],
                                  office_waste_general=form.cleaned_data['office_waste_general'],
                                  office_waste_hardware=form.cleaned_data['office_waste_hardware'],
                                  office_water=form.cleaned_data['office_water'],
                                  )
        myCarbonData.save()

    return redirect('polls:home', id)


def statsPage(request):
    queryset = CarbonData.objects.all()
    id = request.session.get('project_id')
    context = {
        'set': queryset,
        'id': id
    }
    return render(request, 'statistics.html', context)


def accountPage(request):
    context = {
        'form': AccountForm,
    }
    return render(request, 'account.html', context)

def addAccount(request):
    reg_id = request.session.get('reg_id')
    form = AccountForm(request.POST)
    if form.is_valid():
        myAccDetails = AccountDetails(user=RegistrationData.objects.get(id=reg_id),
                                      account_name = form.cleaned_data['account_name'],
                                      bank_name = form.cleaned_data['bank_name'],
                                      bic = form.cleaned_data['bic'],
                                      iban = form.cleaned_data['iban'],
                                      )
        myAccDetails.save()
    return redirect('polls:login')

def investments_pool(request):
    return render(request, 'investments_pool.html')

def investments_private(request):
    context = {
        'form': PaymentForm
    }
    return render(request, 'investments_private.html', context)
def addInvestment(request):
    reg_id = request.session.get('reg_id')
    form = PaymentForm(request.POST)
    if form.is_valid():
        investmentInfo = PaymentData(user=RegistrationData.objects.get(id=1),
                                     organization=form.cleaned_data['organization'],
                                     authorizer=form.cleaned_data['authorizer'],
                                     bank_name=form.cleaned_data['bank_name'],
                                     account_number=form.cleaned_data['account_number'],
                                     amount=form.cleaned_data['amount'])
        investmentInfo.save()
    return redirect('polls:redirecting')

def strategies(request):
    return render(request, 'strategies.html')

def redirecting(request):
    return render(request, 'redirecting.html')
