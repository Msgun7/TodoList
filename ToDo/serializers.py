from rest_framework import serializers

from ToDo.models import Todos


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = '__all__'


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = ("title", )


class TodoListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email
        # 시리얼라이즈에 email을 불러줄 수 있게 하기 위해

    class Meta:
        model = Todos
        fields = ("pk", "title", "user", "is_complete",
                  "created_at", "updated_at", "completion_at")
