from django.db import models

# Create your models here.
class Votes(models.Model):

    # candidate_name = models.ForeignKey(Candidates, on_delete=models.CASCADE)
    no_of_votes = models.IntegerField(null=True)

    def __str__(self):
        return str(self.candidate_name)

class Candidates(models.Model):

    name = models.CharField(max_length=25, unique=True, null=True)
    symbol = models.CharField(max_length=20, null=True)
    constituency = models.CharField(max_length=25, null=True)  # voting place

    def __str__(self):
        return str(self.name)


class Votes(models.Model):

    candidate_name = models.OneToOneField(Candidates, on_delete=models.CASCADE)
    no_of_votes = models.IntegerField(null=True)

    def __str__(self):
        return str(self.candidate_name)
