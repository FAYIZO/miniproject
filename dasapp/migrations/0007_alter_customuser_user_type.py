# Generated by Django 4.1.7 on 2024-10-21 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0006_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'admin'), (2, 'doc')], default=1, max_length=50),
        ),
    ]