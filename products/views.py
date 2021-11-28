from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from products.models import Products
from products.serializers import ProductsSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET','POST'])
def productslist(request):
    '''
    Get all Products
    '''
    if request.method == 'GET':
        productss = Products.objects.all()
        pserializer = ProductsSerializer(productss,many=True)
        return JsonResponse(pserializer.data,safe=False,status=status.HTTP_200_OK)

    elif request.method == 'POST':  
        data = JSONParser().parse(request)
        pserializer = ProductsSerializer(data = data)
        if pserializer.is_valid():
            pserializer.save()
            return JsonResponse(pserializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(pserializer.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def get_products(request, pk):
    """
    Retrieve, update or delete a Product.
    """
    try:
        product = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductsSerializer(product)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductsSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)