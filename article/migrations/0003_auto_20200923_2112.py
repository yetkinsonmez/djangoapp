# Generated by Django 3.1.1 on 2020-09-23 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20200923_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_author',
            field=models.CharField(max_length=120, null=True, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_content',
            field=models.CharField(max_length=180, null=True, verbose_name='Content'),
        ),
    ]
