from rest_framework import serializers

from .models import Envs


class EnvsModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Envs
        exclude = ('update_time',)
        extra_kwargs = {
            'create_time': {
                'read_only': True,
                'format': '%Y年%m月%d日 %H:%M:%S'.encode('unicode_escape').decode('utf8')
            }
        }


class EnvsNamesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Envs
        fields = ('id', 'name')
