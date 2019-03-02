# Generated by Django 2.1.4 on 2019-03-02 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretalx_utils', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talkextraproperties',
            name='slug',
            field=models.SlugField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='talkextraproperties',
            name='speaker_twitter_handle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]