# Generated by Django 5.2 on 2025-04-24 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_alter_lendborrow_lend_date'),
        ('user_authintication', '0004_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField(auto_now=True)),
                ('request_status', models.BooleanField(default=False)),
                ('request_duration', models.IntegerField(default=0)),
                ('request_message', models.TextField(blank=True, null=True)),
                ('borrower', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='requestedBorrower', to='user_authintication.profile')),
                ('lendBorrow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lendBorrow', to='pages.lendborrow')),
            ],
        ),
    ]
