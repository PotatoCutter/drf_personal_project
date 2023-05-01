from rest_framework import serializers

from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.name

    class Meta:
        model = Todo
        fields = "__all__"


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("pk", "title", "is_complete", "created_at",
                  "updated_at", "completion_at", "user")
