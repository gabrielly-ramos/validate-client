from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, request):
        serializer = ClienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if len(request.data("CPF")) != 11:
            raise serializers.ValidationError("O cpf deve conter 11 digitos")
        return request.data