# Generated by Django 4.0.5 on 2022-07-13 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saraiyascope', '0003_museum'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentFrame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]