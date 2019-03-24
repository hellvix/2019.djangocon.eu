# Generated by Django 2.1.4 on 2019-03-24 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretalx_utils', '0006_remove_talkextraproperties_employer_sponsor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='talkextraproperties',
            name='ticket_voucher',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='talkextraproperties',
            name='voucher_sent',
            field=models.BooleanField(default=False),
        ),
    ]
