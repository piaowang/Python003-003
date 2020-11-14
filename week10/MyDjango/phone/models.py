from django.db import models


class T1(models.Model):
    index = models.BigAutoField(primary_key=True)
    rank = models.IntegerField()
    commnet_text = models.CharField(max_length=400)
    sentiment = models.FloatField()
    is_good = models.FloatField()

    class Meta:
        managed = False
        db_table = 'phone_sentiment'