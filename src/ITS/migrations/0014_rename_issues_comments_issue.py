# Generated by Django 4.1.7 on 2023-02-24 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITS', '0013_rename_issue_comments_issues'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='issues',
            new_name='issue',
        ),
    ]
