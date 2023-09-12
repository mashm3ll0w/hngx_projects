from django.http import JsonResponse
from .models import Person
import ast
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def index(request):
  if request.method == "GET":
    names = Person.objects.all()
    persons = [person.serialize() for person in names]
    return JsonResponse({"persons": persons}, safe=False)
  elif request.method == "POST":
    data = ast.literal_eval(request.body.decode("UTF-8"))
    # add the person to the database
    new_user = Person(name=data.get("name").title())
    new_user.save()
    return JsonResponse(new_user.serialize(), status=201, safe=False)

@csrf_exempt
def update_user(request, user_id):
  if request.method == "PATCH" or request.method == "PUT":
    if type(user_id) != int:
      return JsonResponse({"Error": "Please enter a person's id"}, safe=False)

    try:
      user = Person.objects.get(pk=user_id)
      data = ast.literal_eval(request.body.decode("UTF-8"))
      user.name = data.get("name")
      user.save()
      return JsonResponse(user.serialize(), safe=False)
    except Person.DoesNotExist:
      return JsonResponse({"Error": "Person not found"}, status=404, safe=False)

  elif request.method == "DELETE":
    try:
      user = Person.objects.get(pk=user_id)
      user.delete()
      return JsonResponse({}, status=204, safe=False)
    except Person.DoesNotExist:
      return JsonResponse({"Error": "Person not found"}, status=404, safe=False)

def view_user(request, username):
  if request.method == "GET":
    if type(username) != str:
      return JsonResponse({"Error": "Please enter a person's name as a string"}, safe=False)

    username = username.title()
    try:
      user = Person.objects.get(name=username)
      return JsonResponse(user.serialize(), safe=False)
    except Person.DoesNotExist:
      return JsonResponse({"Error": "Person not found"}, status=404, safe=False)
