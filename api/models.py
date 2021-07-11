from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)    # date_now_add引数でオブジェクト作成時の時間を記録してくれる
    updated_at = models.DateTimeField(auto_now=True)        # 更新があったときに自動で日付をつけてくれる

    def __str__(self):
        return self.title
