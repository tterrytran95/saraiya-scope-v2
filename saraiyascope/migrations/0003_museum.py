# Generated by Django 4.0.5 on 2022-07-02 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saraiyascope', '0002_terrysmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Museum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
