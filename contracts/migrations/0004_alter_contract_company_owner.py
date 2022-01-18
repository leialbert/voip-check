# Generated by Django 4.0 on 2022-01-18 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0003_contract_created_at_contract_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='company_owner',
            field=models.FileField(blank=True, null=True, upload_to='contracts/person/', verbose_name='法人'),
        ),
    ]