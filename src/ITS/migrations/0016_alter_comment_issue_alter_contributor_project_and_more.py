# Generated by Django 4.1.7 on 2023-03-04 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ITS', '0015_rename_comments_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='ITS.issue'),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contributor', to='ITS.project'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issue', to='ITS.project'),
        ),
    ]
