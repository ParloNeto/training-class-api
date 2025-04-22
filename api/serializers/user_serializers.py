from rest_framework import serializers
from api.models.user import User

class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    firstName = serializers.CharField()
    lastName = serializers.CharField()
    birthday = serializers.DateField(input_formats=['%d/%m/%Y'], format='%d/%m/%Y')
    goal = serializers.CharField()
    height = serializers.FloatField()
    weight = serializers.FloatField()
    age = serializers.IntegerField(read_only=True)

    def get_age(self, obj):
        return obj.age

    def create(self, validated_data):
        validated_data['age'] = validated_data.get('birthday', None)
        return User(**validated_data).save()

    def update(self, instance, validated_data):
        if 'birthday' in validated_data:
            validated_data['age'] = validated_data['birthday']
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
