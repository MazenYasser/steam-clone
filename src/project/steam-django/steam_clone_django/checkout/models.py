from django.db import models
from games.models import Games
from users.models import User
# Create your models here.
class Order(models.Model):
    user_id = models.ForeignKey(to= User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    game = models.ForeignKey(to= Games, on_delete=models.DO_NOTHING)
    # game = models.OneToOneField(to= Games, on_delete=models.DO_NOTHING)
    cost = models.FloatField(default=0)
    
    # def __str__(self) -> str:
    #     return 'Order ' + str(self.id)