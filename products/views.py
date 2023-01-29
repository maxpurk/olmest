from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import SellForm
from sellers.models import Seller
from django.http import HttpResponse


# Create your views here.

class SellFormView(FormView):
    form_class = SellForm
    template_name= "create.html"
    success_url = reverse_lazy("confirmupload")

    def form_valid(self, form):
        #logic
        profile = Seller.objects.get(user=self.request.user)
        instance = form.save(commit= False)
        instance.profile =profile
        form.save()
        return super().form_valid(form)

def test_view(request, *args, **kwargs):
	return HttpResponse("<h1>Hello World</hi>") #string of html code
	#return render(request, "home.html", {})

def confirmupload_view(request, *args, **kwargs):
	return render(request, "confirmupload.html", {})