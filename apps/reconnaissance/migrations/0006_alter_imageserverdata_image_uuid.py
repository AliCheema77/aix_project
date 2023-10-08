# Generated by Django 4.0.5 on 2023-06-08 10:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reconnaissance', '0005_reconnaissanceaiservices_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageserverdata',
            name='image_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
