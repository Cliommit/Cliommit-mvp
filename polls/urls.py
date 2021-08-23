from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('signup/', views.register, name="register"),
    path('addUser/', views.addUser, name="addUser"),
    path('login/', views.LogInPage, name="login"),
    path('loginCheck/', views.loginValidation, name="loginCheck"),
    path('home/<int:id>', views.Home, name="home"),
    path('addCarbon/', views.carbonRegistration, name="addCarbon"),
    path('addCarbonData/', views.addCarbonData, name="addCarbonData"),
    path('statistics/', views.statsPage, name="statistics"),
    path('account/', views.accountPage, name="account"),
    path('addAccount/', views.addAccount, name="addAccount"),
    path('investments/', views.investments_pool, name="investments"),
    path('investments_private/', views.investments_private, name="investments_private"),
    path('addInvestments', views.addInvestment, name="addInvestment"),
    path('strategies/', views.strategies, name="strategies"),
    path('redirecting', views.redirecting, name="redirecting")
]
