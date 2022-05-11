from django.db import models





class detaform(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    emali = models.EmailField()


    def __str__(self):
        return f"{self.name}, {self.password}, {self.emali},"

