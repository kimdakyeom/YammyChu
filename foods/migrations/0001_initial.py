# Generated by Django 3.2.13 on 2022-11-10 02:38


from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('address', models.TextField()),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
