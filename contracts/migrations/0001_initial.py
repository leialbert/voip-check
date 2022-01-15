# Generated by Django 4.0 on 2022-01-15 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_alter_account_options_account_today_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_license', models.FileField(null=True, upload_to='contracts/company_license/', verbose_name='营业执照')),
                ('company_owner', models.FileField(null=True, upload_to='contracts/person/', verbose_name='法人')),
                ('contract_doc', models.FileField(null=True, upload_to='contracts/contract_doc/', verbose_name='合同附件')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='license', to='accounts.account', verbose_name='公司名称')),
            ],
            options={
                'verbose_name_plural': '合同管理',
            },
        ),
    ]