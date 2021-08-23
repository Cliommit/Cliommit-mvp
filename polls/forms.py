from django import forms

COUNTRIES = (
    ('', 'choose country'),
    ('DE', 'Germany'),
    ('US', 'United States'),
    ('UK', 'United Kingdom'),
    ('AU', 'Australia'),
    ('CD', 'Canada'),
    ('IN', 'India'),
)
SECTOR = (
    ('', 'choose sector'),
    ('Agriculture', 'Agriculture'),
    ('IT Services', 'IT Services'),
    ('Manufacturing', 'Manufacturing'),
    ('Food and Beverage', 'Food and Beverage'),
    ('Finance', 'Finance'),
    ('Health Care', 'Health Care'),
)


class RegistrationForm(forms.Form):
    company = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'input100', 'name': 'company', 'placeholder': 'Name of Company'
    }))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'type': 'password', 'class': 'input100', 'name': 'pass', 'placeholder': 'Password'
    }))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={
        'type': 'email', 'class': 'input100', 'name': 'email', 'placeholder': 'Email'
    }))
    phone = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'tel', 'class': 'input100', 'name': 'phone', 'placeholder': '0123456789'
    }))

    country = forms.ChoiceField(choices=COUNTRIES, widget=forms.Select(attrs={
        'type': 'text', 'class': 'input100', 'name': 'country', 'placeholder': 'Country'
    }))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'input100', 'name': 'address', 'placeholder': 'Address of the Company'
    }))
    reg_no = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'tel', 'class': 'input100', 'name': 'reg_no', 'placeholder': 'Registration number'
    }))
    employees = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'employees', 'placeholder': 'Number of employees'
    }))
    sector = forms.ChoiceField(choices=SECTOR, widget=forms.Select(attrs={
        'type': 'text', 'class': 'input100', 'name': 'sector', 'placeholder': 'Sector of the company'
    }))
    turnover = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'turnover', 'placeholder': 'Annual turnover (in Euros)'
    }))


YES_NO = (('yes', 'YES'), ('no', 'NO'))
E_PROVIDER = (
    ('', 'Select Provider'),
    ('eprimo', 'Eprimo'), ('QCells', 'Q-Cells'),
    ('lekker', 'Lekker'), ('lew', 'LEW'),
    ('vattenfall', 'Vattenfall')
)
E_TYPE = (
    ('', 'Select Type'),
    ('Natural Gas', 'Natural Gas'), ('Coal', 'Coal'),
    ('Wind', 'Wind'), ('Nuclear', 'Nuclear'),
    ('Bio-mass', 'Bio-mass')
)


class CarbonRegistration(forms.Form):
    electricity_amount = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'electricity_amount', 'placeholder': 'Electricity (in KWh)'
    }))
    electricity_renewable = forms.ChoiceField(choices=YES_NO, widget=forms.RadioSelect(attrs={
        'type': 'text', 'name': 'electricity_renewable', 'style':'font-family:Poppins-Regular'
    }))
    electricity_provider = forms.ChoiceField(choices=E_PROVIDER, widget=forms.Select(attrs={
        'type': 'text', 'class': 'input100', 'name': 'electricity_provider',
        'placeholder': 'Select Electricity Provider'
    }))
    electricity_type = forms.ChoiceField(choices=E_TYPE, widget=forms.Select(attrs={
        'type': 'text', 'class': 'input100', 'name': 'electricity_type', 'placeholder': 'Select Electricity Type'
    }))
    electricity_heating = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'electricity_heating', 'placeholder': 'Heating (in KWh)'
    }))
    electricity_gas = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'electricity_gas', 'placeholder': 'Gas (in Litres)'
    }))
    travel_air_travel_long = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_air_travel', 'placeholder': 'Number of long flights (<1600km)'
    }))
    travel_air_travel_short = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_air_travel', 'placeholder': 'Number of short flights (>1600km)'
    }))
    travel_automobile_mileage = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_automobile_mileage', 'placeholder': 'Mileage (in Km)'
    }))
    travel_automobile_commute = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_automobile_commute', 'placeholder': 'Daily commute (in '
                                                                                                   'Km) '
    }))
    travel_bus = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_bus', 'placeholder': 'Bus (No. of employees) '
    }))
    travel_coach = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_coach', 'placeholder': 'Coach (No. of employees) '
    }))
    travel_train = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_train', 'placeholder': 'National Train (No. of employees) '
    }))
    travel_int_train = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_int_train', 'placeholder': 'International Train (No. of employees) '
    }))
    travel_subway = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_subway', 'placeholder': 'Subway (No. of employees)'
    }))
    travel_tram = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_tram', 'placeholder': 'Tram (No. of employees)'
    }))
    travel_taxi = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_taxi', 'placeholder': 'Taxi (No. of employees)'
    }))
    travel_accommodation_hotel = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_accommodation_hotel', 'placeholder': 'Hotel (in days)'
    }))
    travel_accommodation_motel = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_accommodation_motel', 'placeholder': 'Motel (in days)'
    }))
    travel_accommodation_airbnb = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_accommodation_airbnb', 'placeholder': 'Airbnb (in days)'
    }))

    office_utilities_desktop = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'office_utilities_desktop', 'placeholder': 'Number of Desktops'
    }))
    office_utilities_laptop = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'office_utilities_laptop', 'placeholder': 'Number of Laptops'
    }))
    office_waste_bio = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'office_waste_bio', 'placeholder': 'Bio-waste (in Litres)'
    }))
    office_waste_general = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'office_waste_battery', 'placeholder': 'General waste (in Litres)'
    }))
    office_water = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'office_water', 'placeholder': 'Water (in Kilo Litres)'
    }))


class LoginForm(forms.Form):
    company = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'input100', 'name': 'company', 'placeholder': 'Name of Company'
    }))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'type': 'password', 'class': 'input100', 'name': 'pass', 'placeholder': ' Enter Password'
    }))


class AccountForm(forms.Form):
    account_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'input100', 'name': 'account_name', 'placeholder': 'Name of the Account'
    }))
    bank_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'input100', 'name': 'bank_name', 'placeholder': 'Name of the Bank'
    }))
    bic=forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'input100', 'name': 'bic', 'placeholder': 'BIC'
    }))
    iban=forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'input100', 'name': 'iban', 'placeholder': 'IBAN'
    }))


class PaymentForm(forms.Form):
    organization = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'input100', 'name': 'organization', 'placeholder': 'Name of the Organization'
    }))
    authorizer = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'input100', 'name': 'authorizer', 'placeholder': 'Name of the Authorizer'
    }))
    bank_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'input100', 'name': 'bank_name', 'placeholder': 'Name of the Bank'
    }))
    account_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'input100', 'name': 'account_number', 'placeholder': 'Bank Account'
    }))
    amount = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'amount', 'placeholder': 'Provide Pledged Amount'
    }))