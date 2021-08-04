from rest_framework import serializers as sz
from users.models import User
from diaries.serializers import MyDiarySerializer, ReadDiarySerializer


class UserSerializer(sz.ModelSerializer):
    has_voucher = sz.BooleanField(source="in_voucher", read_only=True)
    diaries = MyDiarySerializer(many=True, read_only=True)
    password = sz.CharField(max_length=20, write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "avatar",
            "gender",
            "birth",
            "end_of_voucher",
            "has_voucher",
            "diaries",
            "password",
        )
        read_only_fields = [
            "id",
            "has_voucher",
            "end_of_voucher",
            "diaries",
        ]

    def create(self, validated_data):
        password = validated_data.get("password")
        print(password)
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class SmallUserSerializer(sz.ModelSerializer):
    diaries = ReadDiarySerializer(many=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "avatar", "diaries")
