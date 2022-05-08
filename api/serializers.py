from rest_framework.serializers import ModelSerializer
from .models import array


class NoteSerializer(ModelSerializer):
    class Meta:
        model = array
        fields = ('boby', 'foto')
