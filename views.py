from django.shortcuts import render
from django.http import JsonResponse
import pickle
from .models import PredResults



def predict(request):
	return render(request, 'predict.html')

def predict_chances(request):
	#file = open("lr_model.pickle",encoding="utf8")
	with open('lr_model.pickle', 'rb') as handle:
		model = pickle.load(handle)

	if request.POST.get('action') == 'post':
		age = float(request.POST.get('age'))
		workclass = str(request.POST.get('workclass'))
		education_years = float(request.POST.get('education_years'))
		marital_status = str(request.POST.get('marital_status'))
		relationship = str(request.POST.get('relationship'))
		race = str(request.POST.get('race'))
		sex = str(request.POST.get('sex'))
		hours_per_week = float(request.POST.get('hours_per_week'))

	pred_lst = []
	pred_lst.extend([age,education_years,hours_per_week])

	if workclass == 'Federal-gov':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if workclass == 'Local-gov':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if workclass == 'Private':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if workclass == 'Self-emp-inc':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if workclass == 'Self-emp-not-inc':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if workclass == 'State-gov':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if workclass == 'Without-pay':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if marital_status == 'Divorced':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if marital_status == 'Married-AF-spouse':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if marital_status == 'Married-civ-spouse':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if marital_status == 'Married-spouse-absent':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if marital_status == 'Never-married':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if marital_status == 'Separated':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if marital_status == 'Widowed':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if relationship == 'Husband':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if relationship == 'Not-in-family':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if relationship == 'Other-relative':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if relationship == 'Own-child':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if relationship == 'Unmarried':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if relationship == 'Wife':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if race == 'Amer-Indian-Eskimo':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if race == 'Asian-Pac-Islander':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if race == 'Black':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if race == 'Other':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if race == 'White':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if sex == 'Female':
		pred_lst.append(1)
	else:
		pred_lst.append(0)

	if sex == 'Male':
		pred_lst.append(1)
	else:
		pred_lst.append(0)


	result = model.predict([pred_lst])

	classification = result[0]

	if classification == 0:
		result = 'Income < 50k'
	elif classification == 1:
		result = 'Income > 50k'


	PredResults.objects.create(age=age, workclass=workclass, education_years=education_years,
		marital_status =marital_status, relationship=relationship, race=race, sex=sex, hours_per_week=hours_per_week, result=result)

	return JsonResponse({'result':result,'age':age,'workclass':workclass, 'education_years':education_years,
		'marital_status':marital_status, 'relationship':relationship, 'race':race,'sex':sex,'hours_per_week':hours_per_week})



def view_results(request):
	data = {"dataset": PredResults.objects.all()}
	return render(request, "results.html", data)