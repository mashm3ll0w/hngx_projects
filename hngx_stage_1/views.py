from http import HTTPStatus
from django.http import HttpResponse, JsonResponse
from .models import Person
# Create your views here.

def index(request):
  if request.method == "GET":
    names = Person.objects.all()
    persons = [person.serialize() for person in names]
    return JsonResponse({"persons": persons}, safe=False)


def view_user(request, username):
  if type(username) != str:
    return JsonResponse({"Error": "Please enter a person's name as a string"}, safe=False)

  username = username.title()
  try:
    user = Person.objects.get(name=username)
    return JsonResponse(user.serialize(), safe=False)
  except Person.DoesNotExist:
    return JsonResponse({"Error": "Person not found"}, status=404, safe=False)
