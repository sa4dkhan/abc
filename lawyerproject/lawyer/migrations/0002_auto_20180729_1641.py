# Generated by Django 2.0.7 on 2018-07-29 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawyer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawyer',
            name='lawyer_pic',
            field=models.ImageField(blank=True, upload_to='lawyer_img'),
        ),
    ]