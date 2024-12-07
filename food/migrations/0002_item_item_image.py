# Generated by Django 5.1.2 on 2024-12-04 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='data:image/png;base64,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', max_length=2000),
        ),
    ]
