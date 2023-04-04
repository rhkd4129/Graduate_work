from django.db import models



class Advice(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    keywords = models.CharField(max_length=10)
    age = models.IntegerField()
    # gender = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} - {self.keywords}"
        # return f"{self.user.username} - {self.keywords}"

class AdviceImage(models.Model):
    advice = models.ForeignKey(Advice, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='advice_images/')

    def __str__(self):
        # return f"{self.advice.user.username} - {self.advice.keywords} - {self.id}"
        return f"{self.advice.keywords} - {self.id}"
