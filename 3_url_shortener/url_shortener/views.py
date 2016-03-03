from django.shortcuts import render, redirect, get_object_or_404
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.generic import View
from url_shortener.forms import UrlForm
from base64 import urlsafe_b64encode
from url_shortener.models import Url
from django.http.response import HttpResponseRedirect
# Create your views here.
class Index(View):
	template = 'url_shortener/index.html'

	def get(self, request):
		context = {
			'forms': UrlForm()
		}
		return render(request, self.template, context)

	def post(self, request):
		if URLValidator(request.POST):
			# take request.POST['original']
			original = request.POST['original']
			# get a key for the url
			# attach original url and key to model
			key = str(urlsafe_b64encode(original.encode('ascii')))[2:12]
			# save to model
			# take key string and concatinate key with localhost stuff
			# pass shortened url back to template
			request.session['key'] = key
			url = Url(original = original, short = key)
			try: 
				Url.objects.get(short = key)
			except Url.DoesNotExist:
				url.save()
			context = {
				'forms': UrlForm(),
				'key': key,
			}
			return render(request, self.template, context)

def short_link(request, key):
	print ('rfhirfrfnrfn')
	# key = 'localhost:8000:' + key
	# foo = get_object_or_404(Url, short=key)
	# print (foo)
	print (key)
	original = Url.objects.get(short=key)
	# original=original.original
	# original = str(original)
	# original.replace(key, '')
	# print (original)
	# original = original
	return HttpResponseRedirect(original)