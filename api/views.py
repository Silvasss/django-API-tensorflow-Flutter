from rest_framework.decorators import api_view
from rest_framework.response import Response

from . serializers import NoteSerializer
from .models import array
from PIL import Image, ImageOps
import numpy as np
import tensorflow as tf


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
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                   'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    image = Image.open(request.FILES['file'])

    image = ImageOps.grayscale(image)

    # retorne uma matriz ou qualquer sequência
    matrix = np.array(image)

    # Expanda a forma de uma matriz. Insere um novo eixo que aparecerá na posição do eixo na forma de matriz expandida.
    matrix = (np.expand_dims(matrix, 0))

    model = tf.keras.models.load_model('api/modelo/my_model.h5')

    resultado = model.predict(matrix)

    # Retorna os índices dos valores máximos ao longo de um eixo.
    predicted = class_names[np.argmax(resultado[0]) + 1]

    arrays = array.objects.create(boby= predicted)

    serializer = NoteSerializer(arrays, many=False)

    # Isso não funciona aqui!
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteAll(request):
    arrays = array.objects.all()

    arrays.delete()

    return Response('All was deleted!')

