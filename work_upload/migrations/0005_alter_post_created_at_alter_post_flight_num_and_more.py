# Generated by Django 4.1.3 on 2023-01-31 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_upload', '0004_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='flight_num',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='post',
            name='tspi_ch',
            field=models.CharField(max_length=4),
        ),
    ]
