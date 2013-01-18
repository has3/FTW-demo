# Create your views here.

from django.shortcuts import render_to_response
from performance_groups.models import Group, Subscriber, SubscriberForm
from django.forms.models import modelform_factory
from django.template import RequestContext

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def index(request):
	latest_group_list = Group.objects.all().order_by('name')
	return render_to_response('groups/index.html', {'latest_group_list': latest_group_list})

def detail(request, group_id):
	try:
		g = Group.objects.get(pk=group_id)
	except Group.DoesNotExist:
		raise Http404
	return render_to_response('groups/detail.html', {'group': g})

# def index(request):
#     return HttpResponse("Hello, world. You're at the Performance Group index.")

# def detail(request, group_id):
#     return HttpResponse("You're looking at group %s." % group_id)

def subbed(request, group_id):
	try:
		g = Group.objects.get(pk=group_id)
	except Group.DoesNotExist:
		raise Http404
	return render_to_response("groups/subbed.html", {'group': g})

def subscribe(request, group_id):
	try:
		g = Group.objects.get(pk=group_id)
	except Group.DoesNotExist:
		raise Http404
	#SubscriberForm = modelform_factory(Subscriber) #, exclude=("subscribed_group",))
	if request.method == 'POST':
		form = SubscriberForm(request.POST, request.FILES)
		if form.is_valid():
			f = form.save(commit=False)
			f.subscribed_group = g
			f.save()
			# do something.
			return HttpResponseRedirect('subbed')
	else:
		form = SubscriberForm()
		# form.fields['subscribed_group'].initial=group_id
		# form.fields['subscribed_group'].widget.attrs['readonly'] = True
		# form.fields['subscribed_group'].widget.attrs['label'] = "Subscribing to"
	return render_to_response("groups/sub.html", {"form": form,'group': g}, context_instance=RequestContext(request))
	#return HttpResponse("You're looking at the subscription page for group %s." % group_id)