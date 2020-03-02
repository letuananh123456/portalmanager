from django.contrib import admin
from .models import Collaborators, ContractInformation
# Register your models here.
admin.site.register(Collaborators)
admin.site.register(ContractInformation)
from .models import OderProductHomeModel

# Register your models here.

admin.site.register(OderProductHomeModel)
