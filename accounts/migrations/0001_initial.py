# Generated by Django 4.0 on 2022-01-15 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zhanghao', models.CharField(max_length=40, unique=True, verbose_name='账号')),
                ('zhanghu', models.CharField(max_length=40, verbose_name='账户名称')),
                ('balance', models.FloatField(verbose_name='账户余额')),
                ('credit_amount', models.FloatField(verbose_name='透支额度')),
            ],
        ),
    ]