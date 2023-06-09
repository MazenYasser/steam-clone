# Generated by Django 4.2.1 on 2023-07-02 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='isStaff',
            new_name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='isSuperUser',
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
