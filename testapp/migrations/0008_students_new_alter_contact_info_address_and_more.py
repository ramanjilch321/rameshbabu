# Generated by Django 4.1.7 on 2023-05-04 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0007_contact_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students_new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('t1', models.CharField(max_length=200)),
                ('t2', models.CharField(max_length=200)),
                ('img', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='contact_info',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact_info',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
