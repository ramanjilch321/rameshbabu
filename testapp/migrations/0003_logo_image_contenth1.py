# Generated by Django 4.1.7 on 2023-05-04 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_logo_image_n1_logo_image_n2_logo_image_n3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='logo_image',
            name='contenth1',
            field=models.CharField(default='Design your website', max_length=100),
        ),
    ]
