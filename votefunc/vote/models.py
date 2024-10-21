from django.db import models
from django.contrib.auth.models import User
import hashlib

class Election(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    choice = models.CharField(max_length=100)
    encrypted_choice = models.CharField(max_length=256, blank=True)

    def save(self, *args, **kwargs):
        self.encrypted_choice = hashlib.sha256(self.choice.encode('utf8')).hexdigest()
        super(Vote, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} voted for {self.choice} in {self.election.title}"

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

