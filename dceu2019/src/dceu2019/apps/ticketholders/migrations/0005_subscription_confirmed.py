# Generated by Django 2.1.4 on 2019-03-30 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketholders', '0004_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]