# Generated by Django 3.1 on 2020-08-13 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviename', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]