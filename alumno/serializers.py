from rest_framework import serializers
from alumno.models import alumno 

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = alumno
        fields = ('__all__')