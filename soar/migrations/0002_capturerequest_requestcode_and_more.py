# Generated by Django 4.2 on 2023-06-21 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='capturerequest',
            name='requestCode',
            field=models.IntegerField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')], default=1),
        ),
        migrations.AlterField(
            model_name='capturerequest',
            name='requestDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='RequestCode',
        ),
    ]