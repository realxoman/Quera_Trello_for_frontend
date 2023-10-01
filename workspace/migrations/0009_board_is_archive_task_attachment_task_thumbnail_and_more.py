# Generated by Django 4.2.4 on 2023-09-26 11:38

from django.db import migrations, models
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0008_tasklog'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='is_archive',
            field=models.BooleanField(default=False, verbose_name='آیا بورد آرشیو شده است؟'),
        ),
        migrations.AddField(
            model_name='task',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='attachments', validators=[utils.validators.validate_file_size], verbose_name='فایل ضمیمه'),
        ),
        migrations.AddField(
            model_name='task',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics', validators=[utils.validators.validate_file_size], verbose_name='تصویر پروفایل'),
        ),
        migrations.AddField(
            model_name='taskcomment',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='attachments', validators=[utils.validators.validate_file_size], verbose_name='فایل ضمیمه'),
        ),
    ]