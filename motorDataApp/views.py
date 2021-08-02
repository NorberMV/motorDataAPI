from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MotorDataSerializer
from .models import *

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

@api_view(['GET'])
def motorDataList(request):
    motors = MotorData.objects.all()
    serializer = MotorDataSerializer(motors, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def motorDetail(request, pk):
    motors = MotorData.objects.get(id=pk)
    serializer = MotorDataSerializer(motors, many=False)
    
    return Response(serializer.data)

@api_view(['POST'])
def motorCreate(request):
    serializer = MotorDataSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def motorUpdate(request, pk):
    motor = MotorData.objects.get(id=pk)
    serializer = MotorDataSerializer(instance=motor, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
    
@api_view(['DELETE'])
def motorDelete(request, pk):
    motor = MotorData.objects.get(id=pk)
    motor.delete()

    return Response('Item succesfully deleted!')