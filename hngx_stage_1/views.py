from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Person
import json
# Create your views here.

@csrf_exempt
def index(request):
  if request.method == "GET":
    names = Person.objects.all()
    persons = [person.serialize() for person in names]
    return JsonResponse({"persons": persons}, safe=False)
  elif request.method == "POST":
    data = json.loads(request.body)
    # add the person to the database
    new_user = Person(name=data.get("name").title())
    new_user.save()
    return JsonResponse(new_user.serialize(), status=201, safe=False)


def view_user(request, username):
  if type(username) != str:
    return JsonResponse({"Error": "Please enter a person's name as a string"}, safe=False)

  username = username.title()
  try:
    user = Person.objects.get(name=username)
    return JsonResponse(user.serialize(), safe=False)
  except Person.DoesNotExist:
    return JsonResponse({"Error": "Person not found"}, status=404, safe=False)
