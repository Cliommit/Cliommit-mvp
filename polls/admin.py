from django.contrib import admin

from .models import CarbonData, RegistrationData, AccountDetails, PaymentData

admin.site.register(CarbonData)
admin.site.register(RegistrationData)
admin.site.register(AccountDetails)
admin.site.register(PaymentData)
