# Generated by Django 4.1.7 on 2023-02-22 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITS', '0010_alter_comments_author_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributors',
            name='permission',
            field=models.CharField(choices=[('USER', 'USER'), ('SUPERUSER', 'SUPERUSER')], default='USER', max_length=20),
        ),
    ]
