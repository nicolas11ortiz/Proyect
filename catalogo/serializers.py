from rest_framework import serializers
from .models import Juego


class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = ['title','Desarrolladora','Plataforma','genre']
