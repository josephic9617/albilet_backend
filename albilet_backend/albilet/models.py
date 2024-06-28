from django.db import models

class User(models.Model):
    fullname = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    user_type = models.IntegerField(default=3) # { 1 == admin }, { 2 == moderator }, { 3 == user }

    def __str__(self):
        return self.fullname

class Place(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Concert(models.Model):
    name = models.CharField(max_length=500)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='concerts')
    ticket_total_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    code = models.IntegerField()
    ticket_type = models.IntegerField(default=1) # { 1 == booked }, { 2 == sold }, { 3 == free }
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')

    def __str__(self):
        return str(self.code)