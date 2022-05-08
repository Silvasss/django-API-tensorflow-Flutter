from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json

from . serializers import NoteSerializer
from .models import array
from PIL import Image, ImageOps
import numpy as np
import tensorflow as tf


# https://www.youtube.com/watch?v=VnztChBw7Og


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint' : '/array/id',
            'method' : 'GET',
            'body' : None,
            'description' : 'Returns a single array'
        },
        {
            'Endpoint': '/array/create',
            'method': 'POST',
            'body': {'body' : ''},
            'description': 'Creates new array with data sent in post request'
        },
        {
            'Endpoint': '/array/id/delete',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete a exiting note'
        }

    ]

    return Response(routes)


@api_view(['GET'])
def getArrayFull(request):
    arrays = array.objects.all()

    serializer = NoteSerializer(arrays, many = True)

    return Response(serializer.data)


@api_view(['GET'])
def getArrayId(request, pid):
    arrays = array.objects.get(id = pid)

    serializer = NoteSerializer(arrays, many = False)

    return Response(serializer.data)


@api_view(['POST'])
def createTeste(request):
    data = request.data

    arrays = array.objects.create(boby = data['body'])

    serializer = NoteSerializer(arrays, many = False)

    return Response(serializer.data)


@api_view(['POST'])
def uploadImage(request):
    #data = request.get['foto']
    #print(data)
    print("Entrou na função")
    # Numpy vai se chamado aqui e tratar a matriz e salvar ela.

    image = Image.open(request.FILES['file'])

    image = ImageOps.grayscale(image)
    print("Entrou na função2")

    im2array = np.array(image)

    im2array = (np.expand_dims(im2array, 0))
    print("Entrou na função3")

    data = im2array

    #array.objects.create(foto = data['body'])
    print("Entrou na função5")

    #array.objects.create(boby = im2array['file'])

    print(im2array)

    #array.objects.create(arrayImagem = im2array)

    return Response('Image uploaded')


@api_view(['POST'])
def uploadImage4(request):
    image = Image.open(request.FILES['file'])

    image = ImageOps.grayscale(image)

    matrix = np.array(image)

    matrix = (np.expand_dims(matrix, 0))

    model = tf.keras.models.load_model('api/modelo/my_model.h5')

    resultado = model.predict(matrix)

    print(resultado)

    return Response('Image feita')


@api_view(['DELETE'])
def deleteAll(request):
    arrays = array.objects.all()

    arrays.delete()

    return Response('All was deleted!')

