from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here
@api_view(['GET'])
def apiOverview(request):
    api_urls = {

        "List":"/motorData-List",
        "Detail View":"/motor-detail/<str:pk>/",
        "Create":"/motor-create/",
        "Update":"/motor-update/<str:pk>/",
        "Delete":"/motor-delete/<str:pk>/",

    }
    return Response(api_urls)