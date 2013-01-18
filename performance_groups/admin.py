from performance_groups.models import Group, Subscriber
#from subscribers.models import Subscriber
from django.contrib import admin

#admin.site.register(Group)

class SubscriberInline(admin.TabularInline):
	model = Subscriber
	extra = 1

class GroupAdmin(admin.ModelAdmin):
	fields = ['name', 'description', 'sample_image']
	#list_display = ('name')  #Add more fields
	search_fields = ['name']
	inlines = [SubscriberInline]

admin.site.register(Group, GroupAdmin)
