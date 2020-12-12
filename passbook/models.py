from django.db import models

from pdj.models import BigAutoField, EnumField
from account.models import User


class PassbookTypeChoices(models.TextChoices):
    USE = 'USE', '使用'
    GET = 'GET', '取得'


class Passbook(models.Model):

    passbook_id = BigAutoField(primary_key=True, help_text="通帳ID")
    user = models.ForeignKey(User, help_text="ユーザー", on_delete=models.CASCADE)
    passbook_type = EnumField(max_length=3, choices=PassbookTypeChoices.choices, help_text="")
    amount = models.IntegerField(help_text="金額")
    recording_date = models.DateField(help_text="記録日")
    
    class Meta:
        db_table = "passbook"
