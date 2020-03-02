"""insecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.dashboard import views as dash_view
from apps.contract import views as contract_view
from apps.users import views as user_view



urlpatterns = [
   path('', include('apps.dashboard.urls')),

    #api url

    # path('api/update-agency-total/', api_view.UpdateNumberAgencyTotal.as_view()),
    # path('api/update-agency-new/', api_view.UpdateNumberNewAgency.as_view()),
    # path('api/update-agency-channel/', api_view.UpdateNumberAgencyChannel.as_view()),
    # path('api/update-number-customer-day/', api_view.UpdateNumberCustomerDay.as_view()),
    # path('api/update-number-customer-month/', api_view.UpdateNumberCustomerMonth.as_view()),
    # path('api/update-number-customer-location/', api_view.UpdateNumberCustomerLocation.as_view()),
    # path('api/update-number-customer-channel/', api_view.UpdateNumberCustomerChannel.as_view()),
    # path('api/update-day-success/', api_view.UpdateDaySuccess.as_view()),
    # path('api/update-month-success/', api_view.UpdateMonthSuccess.as_view()),
    # path('api/update-channel-success/', api_view.UpdateSuccessChannel.as_view()),
    # path('api/update-main-product/', api_view.UpdateMainProductStatisticSuccess.as_view()),
    # path('api/update-sup-product/', api_view.UpdateSupProductStatisticSuccess.as_view()),
    # path('api/update-favorite-product/', api_view.UpdateFavoriteProductSuccess.as_view()),
    
    path('admin/', admin.site.urls),
    path('api/update-contract/',contract_view.UpdateContractApi.as_view()),
    path('api/update-user/',user_view.UpdateInfoUserApi.as_view()),
    path('api-order-home-success/',contract_view.InfoOrderHomeUserApi.as_view(), name='order_user_success'),
    path('api-user-success/',user_view.UpdateInfoUserApi.as_view(), name='user_success'),


]
