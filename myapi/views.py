# API view endpoints
from django.http import JsonResponse
from .models import Provider
from .models import ServiceArea
from .serializers import ProviderSerializer
from .serializers import ServiceAreaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# API endpoint accepted methods
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Provider_list(request, format=None):
    
    # if GET (retrieve data)
    if request.method == 'GET':
        # get all the providers
        providers = Provider.objects.all()
        # serialize them
        serializer = ProviderSerializer(providers, many=True) # many=True for batch
        # return as json
        return JsonResponse({"Providers": serializer.data}, safe=False)
    
    # if POST (post data)
    elif request.method == 'POST':
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTPP_201_CREATED)

    # if PUT
    elif request.method == 'PUT':
        serializer = ProviderSerializer(providers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    # if DELETE
    elif request.method == 'DELETE':
        providers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Provider_ServiceArea(request, format=None):
    if request.method == 'GET':
        # get all the providers
        serviceareas = ServiceArea.objects.all()
        # serialize them
        serializer = ServiceAreaSerializer(serviceareas, many=True)
        return JsonResponse({"Provider Service Areas": serializer.data}, safe=False)
    
    elif request.method == 'POST':
        serializer = ServiceAreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'PUT':
        serializer = ProviderSerializer(serviceareas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        serviceareas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# d3.geoContains(object, point)

