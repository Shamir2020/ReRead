# Generated by Django 5.2 on 2025-05-08 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_alter_borrowrequest_borrower_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='condition',
            field=models.CharField(choices=[('New', 'New'), ('Used', 'Used'), ('Used but like new', 'Used but like new')], default='New', max_length=50),
        ),
    ]
