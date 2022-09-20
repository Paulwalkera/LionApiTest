from rest_framework import serializers

from interfaces.models import Interfaces
from utils.validators import ManualValidateIsExist
from .models import Configures
from testcases.serializers import InterfaceProjectModelSerializer

# class InterfacesAnotherSerializer(serializers.ModelSerializer):
#     project = serializers.StringRelatedField(help_text='项目名称')
#     # 项目ID
#     pid = serializers.IntegerField(write_only=True, validators=[ManualValidateIsExist('project')], help_text='项目ID')
#     # 接口ID
#     iid = serializers.IntegerField(write_only=True, validators=[ManualValidateIsExist('interface')], help_text='接口ID')
#
#     class Meta:
#         model = Interfaces
#         fields = ('iid', 'name', 'project', 'pid')
#         extra_kwargs = {
#             'name': {
#                 'read_only': True
#             }
#         }
#
#     def validate(self, attrs):
#         """
#         校验项目ID是否与接口ID一致
#         :param attrs:
#         :return:
#         """
#         if not Interfaces.objects.filter(id=attrs['iid'], project_id=attrs['pid']).exists():
#             raise serializers.ValidationError("项目和接口信息不对应!")
#         return attrs


class ConfiguresSerializer(serializers.ModelSerializer):
    """
    配置序列化器
    """
    interface = InterfaceProjectModelSerializer(help_text='所属项目和接口信息', label='所属项目和接口信息')

    class Meta:
        model = Configures
        fields = ('id', 'name', 'interface', 'author', 'request')
        extra_kwargs = {
            'request': {
                'write_only': True
            }
        }

    def to_internal_value(self, data):
        result = super().to_internal_value(data)
        iid = result.pop('interface').get('iid')
        result['interface_id'] = iid
        return result
