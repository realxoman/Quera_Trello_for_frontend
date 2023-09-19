# Generated by Django 4.2.4 on 2023-09-19 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workspace', '0006_taskcomment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='name',
            field=models.CharField(max_length=200, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='board',
            name='order',
            field=models.BigIntegerField(default=0, verbose_name='ترتیب'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=255, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(auto_now_add=True, verbose_name='ددلاین'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, max_length=500, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=255, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='task',
            name='order',
            field=models.BigIntegerField(default=0, verbose_name='ترتیب'),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.BigIntegerField(default=0, verbose_name='اولویت'),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='text',
            field=models.TextField(blank=True, max_length=500, verbose_name='متن'),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='color',
            field=models.CharField(default='#000', max_length=256, verbose_name='رنگ'),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='name',
            field=models.CharField(max_length=255, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='workspacemember',
            name='role',
            field=models.CharField(max_length=350, verbose_name='نقش\u200cکاربری'),
        ),
        migrations.AlterField(
            model_name='workspacemember',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
