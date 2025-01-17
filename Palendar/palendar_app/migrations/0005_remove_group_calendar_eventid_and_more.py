# Generated by Django 5.1.4 on 2025-01-10 14:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palendar_app', '0004_alter_users_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group_calendar',
            name='eventID',
        ),
        migrations.RemoveField(
            model_name='group_calendar',
            name='members',
        ),
        migrations.RemoveField(
            model_name='user_calendar',
            name='userID',
        ),
        migrations.AlterField(
            model_name='users',
            name='account_name',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=16),
        ),
        migrations.CreateModel(
            name='EventDetails',
            fields=[
                ('eventID', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=24)),
                ('event_desc', models.CharField(max_length=128)),
                ('event_date', models.DateTimeField()),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='palendar_app.users')),
            ],
        ),
        migrations.CreateModel(
            name='GroupCalendar',
            fields=[
                ('groupID', models.AutoField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=24)),
                ('eventID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='palendar_app.eventdetails')),
                ('members', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='palendar_app.users')),
            ],
        ),
        migrations.DeleteModel(
            name='Event_Details',
        ),
        migrations.DeleteModel(
            name='Group_Calendar',
        ),
        migrations.DeleteModel(
            name='User_Calendar',
        ),
    ]
