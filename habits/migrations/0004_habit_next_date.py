# Generated by Django 5.0.2 on 2024-03-15 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_habit_time_to_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='next_date',
            field=models.DateField(blank=True, null=True, verbose_name='дата следующего действия'),
        ),
    ]