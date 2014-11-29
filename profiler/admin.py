from django.contrib import admin
from profiler.models import Student

class StudentAdmin(admin.ModelAdmin):
    
    ##Trial - 1:
    ##Following line shows only specified fields in admin site in entered order
    #fields = ["first_name", "last_name"]

	##Trial - 2:
	##We can set HTML classes to each fieldset. 
	#fieldsets = [
	#	(None,	{'fields':['first_name','last_name']}),
	#	('Contact Information', {'fields':['email'], 'classes':['collapse']}),
	#]
	
	##Trial - 3
	##Now we can see three columns while clicking on Student link
	#list_display = ('first_name', 'roll_no', 'admission_date', '')		#Look at this line
	#fieldsets = [
	#	(None,	{'fields':['first_name','last_name']}),
	#	('Contact Information', {'fields':['email'], 'classes':['collapse']}),
	#]
	
	##Trial - 4
	##We can also filter by any database field using "list_filter"
	list_display = ('first_name', 'roll_no', 'admission_date', 'fees_paid')		
	list_filter = ['fees_paid']											#Look at this line
	fieldsets = [
		(None,	{'fields':['first_name','last_name']}),
		(None,	{'fields':['fees_paid']}),
		('Contact Information', {'fields':['email'], 'classes':['collapse']}),
	]
admin.site.register(Student, StudentAdmin)
