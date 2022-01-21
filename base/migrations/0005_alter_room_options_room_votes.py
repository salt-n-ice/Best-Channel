# Generated by Django 4.0.1 on 2022-01-12 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_message_options_alter_room_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['votes', '-updated', '-created']},
        ),
        migrations.AddField(
            model_name='room',
            name='votes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
