from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Account
from django.db.models import Q
import json



@login_required
def addView(request):
	if request.method == 'POST':
		new_iban = request.POST['iban']
		current_user = request.user
		newAccount = Account.objects.create(owner=current_user, iban=new_iban)
	return redirect('/')


@login_required
def homePageView(request):
	current_user = request.user
	accounts_list = Account.objects.filter(owner=current_user)
	accounts_ibans = [x.iban for x in accounts_list]
	print(accounts_ibans)
	return render(request, 'pages/index.html', {'accounts': accounts_ibans})
