# Generated by Django 4.1.7 on 2023-05-04 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_logo_image_contentp2_alter_logo_image_contentp1'),
    ]

    operations = [
        migrations.AddField(
            model_name='logo_image',
            name='button1',
            field=models.CharField(default='Contact', max_length=250),
        ),
        migrations.AddField(
            model_name='logo_image',
            name='button2',
            field=models.CharField(default='More', max_length=250),
        ),
    ]
