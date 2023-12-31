# Generated by Django 4.2.4 on 2023-10-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0012_alter_projectmember_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmember',
            name='role',
            field=models.IntegerField(choices=[(4, 'Full'), (3, 'Editor'), (2, 'Commentor'), (1, 'Viewer')], default=1, verbose_name='نقش\u200cکاربری'),
        ),
        migrations.AlterField(
            model_name='task',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='attachments', verbose_name='فایل ضمیمه'),
        ),
        migrations.AlterField(
            model_name='task',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics', verbose_name='تصویر پروفایل'),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='attachments', verbose_name='فایل ضمیمه'),
        ),
    ]
