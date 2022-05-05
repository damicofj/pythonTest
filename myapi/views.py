# API view endpoints
from django.http import JsonResponse
from .models import Provider
from .serializers import ProviderSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# API endpoint accepted methods
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Provider_list(request):
    
    # if GET (retrieve data)
    if request.method == 'GET':
        # get all the providers
        providers = Provider.objects.all()
        # serialize them
        serializer = ProviderSerializer(providers, many=True)
        # return as json
        return JsonResponse({"Providers": serializer.data}, safe=False)
    
    # if POST (post data)
    if request.method == 'POST':
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTPP_201_CREATED)

    # if PUT
    if request.method == 'PUT':
        pass
    
    # if DELETE
    if request.method == 'DELETE':
        pass
    
