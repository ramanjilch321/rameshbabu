# Generated by Django 4.1.7 on 2023-05-04 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_logo_image_contentp1'),
    ]

    operations = [
        migrations.AddField(
            model_name='logo_image',
            name='contentp2',
            field=models.CharField(default='optio numquam totam placeat animi site.', max_length=250),
        ),
        migrations.AlterField(
            model_name='logo_image',
            name='contentp1',
            field=models.CharField(default='Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus repellat repellendus', max_length=250),
        ),
    ]
