# Generated by Django 2.0.8 on 2019-08-27 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvote', models.IntegerField(default=0)),
                ('funny', models.IntegerField(default=0)),
                ('love', models.IntegerField(default=0)),
            ],
        ),
    ]
