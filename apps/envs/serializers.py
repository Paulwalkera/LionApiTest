from rest_framework import serializers

from .models import Envs


class EnvsModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Envs
        exclude = ('update_time',)
        extra_kwargs = {
            'create_time': {
                'read_only': True,
                'format': '%Y-%m-%d %H:%M:%S'
            }
        }


class EnvsNamesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Envs
        fields = ('id', 'name')
