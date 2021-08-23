from django.db import models


class RegistrationData(models.Model):
    # section 1
    company = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    # section 2
    country = models.CharField(max_length=100, default='Null')
    address = models.CharField(max_length=100, default='Null')
    reg_no = models.CharField(max_length=100, default='Null')
    employees = models.CharField(max_length=100, default='Null')
    sector = models.CharField(max_length=100, default='Null')
    turnover = models.CharField(max_length=100, default='Null')

    def __str__(self):
        return self.company


class CarbonData(models.Model):
    user = models.ForeignKey(RegistrationData, on_delete=models.CASCADE)
    # carbon-disclosure:section 1
    electricity_renewable = models.CharField(max_length=100, default='Null')
    electricity_amount = models.CharField(max_length=100, default='Null')
    electricity_provider = models.CharField(max_length=100, default='Null')
    electricity_type = models.CharField(max_length=100, default='Null')
    electricity_heating = models.CharField(max_length=100, default='Null')
    electricity_gas = models.CharField(max_length=100, default='Null')
    # carbon-disclosure:section 2
    travel_air_travel_long = models.CharField(max_length=100, default='Null')
    travel_air_travel_short = models.CharField(max_length=100, default='Null')
    travel_automobile_mileage = models.CharField(max_length=100, default='Null')
    travel_automobile_commute = models.CharField(max_length=100, default='Null')
    travel_bus = models.CharField(max_length=100, default='Null')
    travel_coach = models.CharField(max_length=100, default='Null')
    travel_train = models.CharField(max_length=100, default='Null')
    travel_int_train = models.CharField(max_length=100, default='Null')
    travel_subway = models.CharField(max_length=100, default='Null')
    travel_tram = models.CharField(max_length=100, default='Null')
    travel_taxi = models.CharField(max_length=100, default='Null')
    travel_accommodation_hotel = models.CharField(max_length=100, default='Null')
    travel_accommodation_motel = models.CharField(max_length=100, default='Null')
    travel_accommodation_airbnb = models.CharField(max_length=100, default='Null')
    # carbon-disclosure:section 3
    office_utilities_desktop = models.CharField(max_length=100, default='Null')
    office_utilities_laptop = models.CharField(max_length=100, default='Null')
    office_waste_bio = models.CharField(max_length=100, default='Null')
    office_waste_general = models.CharField(max_length=100, default='Null')
    office_water = models.CharField(max_length=100, default='Null')

    def __str__(self):
        return self.user.company

    class Meta:
        ordering = ['user']


class AccountDetails(models.Model):
    user = models.ForeignKey(RegistrationData, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=100, default='Null')
    bank_name = models.CharField(max_length=100, default='Null')
    bic = models.CharField(max_length=100, default='Null')
    iban = models.CharField(max_length=100, default='Null')

    def __str__(self):
        return self.user.company

    class Meta:
        ordering = ['user']


class PaymentData(models.Model):
    user = models.ForeignKey(RegistrationData, on_delete=models.CASCADE)
    organization = models.CharField(max_length=100, default='Null')
    authorizer = models.CharField(max_length=100, default='Null')
    bank_name = models.CharField(max_length=100, default='Null')
    account_number = models.CharField(max_length=100, default='Null')
    amount = models.IntegerField(default='Null')

    def __str__(self):
        return self.user.company

    class Meta:
        ordering = ['user']