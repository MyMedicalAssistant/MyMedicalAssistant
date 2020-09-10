# Generated by Django 3.1 on 2020-09-10 22:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MedSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication', models.CharField(max_length=64)),
                ('hours', models.IntegerField()),
                ('dosage', models.CharField(max_length=256)),
                ('inventory', models.IntegerField()),
                ('start', models.DateTimeField()),
                ('last', models.DateTimeField()),
                ('next_dosage', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('user_id_medication', models.CharField(max_length=64)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='username')),
            ],
        ),
    ]