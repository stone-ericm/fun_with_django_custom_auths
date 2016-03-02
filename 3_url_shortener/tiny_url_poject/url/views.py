from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UrlForm
from .models import Url 
import uuid

# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, "url/index.html")

class UrlShorten(View):
    # pu.db
    template = "url/shorten.html"
    def get(self, request):
        form = UrlForm()
        context = {
            'url_form': form,}
        # using self is a fancy way to give a variable name to the template ...?
        return render(request, self.template, context)

    def post(self, request):
        form = UrlForm(data=request.POST)
        # If the forms is valid.
        if form.is_valid():

            form = form.save(commit=False)
            # shorten the UUID to last part 
            key = str(uuid.uuid4()).split('-')[:: -1][0] # REALY NICE!!!
            form.key = key
            form.save()

            new_link = "http://localhost:8000/url/" + str(key)
            url = Url.objects.order_by('-created_at')[0]

            context = {
                'new_link': new_link,
                'url': url,}
            return render(request, "url/index.html", context)

        else:
            context = {
                'url_form': form,}
            return render(request, self.template, context)

class UrlRedirect(View):
    def get(self, request, key=None):
        url = Url.objects.get(key=key)
        website = url.actual
        # print (website)
        return redirect(website)



