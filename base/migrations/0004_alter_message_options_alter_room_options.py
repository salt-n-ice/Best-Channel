# Generated by Django 4.0.1 on 2022-01-12 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_room_host'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
    ]