from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Userモデルに対するSerializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # レスポンスで表示するフィールド
        fields = ['id', 'username', 'password']
        # passwordはwrite onlyにし、入力必須にします
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    ## ユーザ作る際のcreateをオーバーライドする
    ## ユーザ要求のパスワードをハッシュ化してDBに保存したいのでオーバーライドする
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        # ユーザを新規作成したときにTokenを作成し、DBに登録する
        Token.objects.create(user=user)
        return user

# Taskモデルに対するSerializer
class TaskSerializer(serializers.ModelSerializer):

    # DjangoのDataTimeFieldの表記は長いので、フォーマットを変更し、かつ読み取り専用とする
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'created_at', 'updated_at']

