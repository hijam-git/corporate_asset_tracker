from django.contrib import admin
from .models import *

admin.site.register(Company)
admin.site.register(Staff)
admin.site.register(Employee)
admin.site.register(Asset)
admin.site.register(AssetLog)