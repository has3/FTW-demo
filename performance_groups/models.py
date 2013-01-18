from django.db import models
from django.forms import ModelForm

class Group(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	sample_image = models.URLField(blank=True)

	def __unicode__(self):
		return self.name

TITLE_CHOICES = (
	('MR', 'Mr.'),
	('MRS', 'Mrs.'),
	('MS', 'Ms.'),
)

STATE_CHOICES = (
	('AL', 'Alabama'),
	('AK', 'Alaska'),
	('AZ', 'Arizona'),
	('AR', 'Arkansas'),
	('CA', 'California'),
	('CO', 'Colorado'),
	('CT', 'Connecticut'),
	('DE', 'Delaware'),
	('FL', 'Florida'),
	('GA', 'Georgia'),
	('HI', 'Hawaii'),
	('ID', 'Idaho'),
	('IL', 'Illinois'),
	('IN', 'Indiana'),
	('IA', 'Iowa'),
	('KS', 'Kansas'),
	('KY', 'Kentucky'),
	('LA', 'Louisiana'),
	('ME', 'Maine'),
	('MD', 'Maryland'),
	('MA', 'Massachusetts'),
	('MI', 'Michigan'),
	('MN', 'Minnesota'),
	('MS', 'Mississippi'),
	('MO', 'Missouri'),
	('MT', 'Montana'),
	('NE', 'Nebraska'),
	('NV', 'Nevada'),
	('NH', 'New Hampshire'),
	('NJ', 'New Jersey'),
	('NM', 'New Mexico'),
	('NY', 'New York'),
	('NC', 'North Carolina'),
	('ND', 'North Dakota'),
	('OH', 'Ohio'),
	('OK', 'Oklahoma'),
	('OR', 'Oregon'),
	('PA', 'Pennsylvania'),
	('RI', 'Rhode Island'),
	('SC', 'South Carolina'),
	('SD', 'South Dakota'),
	('TN', 'Tennessee'),
	('TX', 'Texas'),
	('UT', 'Utah'),
	('VT', 'Vermont'),
	('VA', 'Virginia'),
	('WA', 'Washington'),
	('WV', 'West Virginia'),
	('WI', 'Wisconsin'),
	('WY', 'Wyoming')
)

class Subscriber(models.Model):
	title = models.CharField(max_length=3, choices=TITLE_CHOICES, blank=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=254)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=2, choices=STATE_CHOICES)
	#zip_Code = models.IntegerField(max_length=5, null=True)
	subscribed_group = models.ForeignKey(Group)
	#subscribed_group.editable = False

	def __unicode__(self):
		return self.title + " " + self.first_name + " " + self.last_name

class SubscriberForm(ModelForm):
	class Meta:
		model = Subscriber
		exclude = ('subscribed_group')

