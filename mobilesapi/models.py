from django.db import models

# Mobile Phones models

class MobilePhone(models.Model):

    CHOICE_COLOR = (
        ('black', 'black'),
        ('white', 'white'),
        ('silver', 'silver'),
        ('gold', 'gold'),
        ('red', 'red'),
    )

    made = models.CharField(max_length=20)
    modelname = models.CharField(max_length=20, unique=True)
    color = models.CharField(max_length=20, choices=CHOICE_COLOR)
    release_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.modelname
