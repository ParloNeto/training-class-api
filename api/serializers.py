# # api/serializers.py
# from rest_framework import serializers
# from .models import Item
#
# class ItemSerializer(serializers.Serializer):
#     id = serializers.CharField(read_only=True)
#     nome = serializers.CharField()
#     preco = serializers.FloatField()
#
#     def create(self, validated_data):
#         return Item(**validated_data).save()
#
#     def update(self, instance, validated_data):
#         instance.nome = validated_data.get('nome', instance.nome)
#         instance.preco = validated_data.get('preco', instance.preco)
#         instance.save()
#         return instance
