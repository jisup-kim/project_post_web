from django.db import models

class Post(models.Model):

    xfa_num = (('Number1', 'Number1'),('Number2', 'Number2'),('Number3', 'Number3'),('Number4', 'Number4'),('Number5', 'Number5'),('Number6', 'Number6'))
    tspi_yn = (('Y', 'Y'), ('N', 'N'))
    

    flight_name = models.CharField(max_length=30)
    flight_date = models.DateField()
    flight_num = models.CharField(max_length=10, choices=xfa_num)

    inetx_ver = models.CharField(max_length=5)
    cal_ver = models.CharField(max_length=5)

    tspi_ch = models.CharField(max_length=4, choices=tspi_yn)

    created_at = models.DateTimeField()
    writer_name = models.CharField(max_length=10)

    def __str__(self):
        return f'[{self.pk}] {self.flight_name}'

    def get_absolute_url(self):
        return f'/work_upload/{self.pk}/'

# Create your models here.

