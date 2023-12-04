from django.db import models

class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    login_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username} - {self.id}"
    
class Note(models.Model):
    content = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s note - {self.id}"
    
    def is_longer_than(self, min_lenght):
        return len(self.content) >= min_lenght

