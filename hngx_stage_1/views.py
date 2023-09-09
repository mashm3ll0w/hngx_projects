from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime

# Create your views here.

def index(request):
  if request.method == "GET":
    param_username = request.GET['slack_name']
    param_track = request.GET['track']
    slack_name = "Charles Swaleh"

    if param_username.lower() == "swaleh" and param_track.lower() == "backend":
      data = {
      "slack_name": "Charles Swaleh",
      "current_day": datetime.datetime.today().strftime('%A'),
      "utc_time": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
      "track": "backend",
      "github_file_url": "https://github.com/mashm3ll0w/hngx_stage_1/blob/main/hngx_stage_1/views.py",
      "github_repo_url": "https://github.com/mashm3ll0w/hngx_stage_1",
      "status_code": HttpResponse.status_code
    }
      return JsonResponse(data, safe=False)
    else:
      return JsonResponse({"Error": "Wrong User/Track"}, safe=False)
  else:
    return JsonResponse({"Error": "Please use a GET request"}, safe=False)
