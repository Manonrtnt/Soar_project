from django.db import models

# class CaptureRequest(models.Model):
#   requestName = models.CharField(max_length=50)
#   requestUser = models.CharField(max_length=50)
#   requestDate = models.DateTimeField("date published")
#   requestCode = models.IntegerField()
#   def __str__(self):
#     return self.requestName

class CaptureRequest(models.Model):
    
    REQUEST_CHOICES = [
        (1, 'Option 1 : Capturer tous les paquets'),
        (2, 'Option 2 : Capturer les paquets de la couche Ethernet'),
        (3, 'Option 3 : Capturer les paquets de la couche IP'),
        (4, 'Option 4 : Capturer les paquets de la couche TCP'),
    ]

    requestName = models.CharField(max_length=255)
    requestUser = models.CharField(max_length=255)
    requestDate = models.DateTimeField(auto_now_add=True)
    requestCode = models.IntegerField(choices=REQUEST_CHOICES, default=1)

    def __str__(self):
        return self.requestName

# class RequestCode(models.Model):
#     captureRequest = models.ForeignKey(CaptureRequest, on_delete=models.CASCADE)
#     requestCode = models.IntegerField()
    
#     def __str__(self):
#       return self.requestCode