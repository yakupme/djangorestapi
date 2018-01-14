from django.contrib import admin
from .models import MobilePhone

# Register your models here.
class MobilePhoneAdmin(admin.ModelAdmin):
	fields = ('made', 'modelname', 'colour')
	def view_phone(self, obj):
		return obj.modelname
	
#MobilePhone models added to admin 

admin.site.register(MobilePhone, MobilePhoneAdmin)