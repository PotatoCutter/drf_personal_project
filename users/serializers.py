from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance = super().update(validated_data)
        password = instance.password
        instance.set_password(password)
        instance.save()
        return instance


class UserUpdate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "name", "gender", "age", "desc", "password")


class TokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email
        token['name'] = user.name
        token['gender'] = user.gender
        token['age'] = user.age

        return token
