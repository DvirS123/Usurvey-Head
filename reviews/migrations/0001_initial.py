# Generated by Django 2.2 on 2020-05-12 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Source', models.URLField(max_length=100)),
                ('Date', models.DateTimeField()),
                ('Body', models.TextField()),
                ('Votes', models.PositiveIntegerField(default=1)),
                ('Uploaded', models.DateField(auto_now_add=True)),
                ('Image', models.ImageField(upload_to='product_images/')),
                ('Icon', models.ImageField(upload_to='product_icons/')),
                ('User_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
