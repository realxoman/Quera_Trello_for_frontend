# Generated by Django 4.2.4 on 2023-09-26 11:38

from django.db import migrations, models
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_customuser_email_alter_customuser_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics', validators=[utils.validators.validate_file_size], verbose_name='تصویر پروفایل'),
        ),
    ]