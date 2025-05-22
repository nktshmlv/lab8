from django.db import models

class Client(models.Model):
    phone = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.phone})"

class Reason(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Operator(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Call(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    reason = models.ForeignKey(Reason, on_delete=models.CASCADE)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    call_date = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"Call #{self.id} by {self.client}"