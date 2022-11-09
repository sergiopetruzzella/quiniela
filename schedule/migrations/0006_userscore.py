# Generated by Django 4.1.3 on 2022-11-07 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('schedule', '0005_remove_realscore_match_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserScore',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('points', models.IntegerField()),
            ],
        ),
    ]