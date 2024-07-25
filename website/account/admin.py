from django.contrib import admin
from .models import User, DistrictOfficeList, BranchLocation

# Register your models here.
admin.site.register(User)
admin.site.register(DistrictOfficeList)
admin.site.register(BranchLocation)