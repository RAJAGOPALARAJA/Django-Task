# Generated by Django 3.0.5 on 2020-05-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
