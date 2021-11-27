# Generated by Django 3.2.9 on 2021-11-25 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('name_en', models.CharField(blank=True, max_length=100, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('desc_uz', models.TextField(blank=True, null=True)),
                ('desc_ru', models.TextField(blank=True, null=True)),
                ('desc_en', models.TextField(blank=True, null=True)),
                ('media', models.FileField(blank=True, null=True, upload_to='')),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('number', models.IntegerField(blank=True, default=0, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=80, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=80, null=True)),
                ('name_en', models.CharField(blank=True, max_length=80, null=True)),
                ('img', models.ImageField(upload_to='')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_created=True)),
                ('user_id', models.BigIntegerField(default=0, unique=True)),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=200)),
                ('bonus', models.IntegerField(default=0)),
                ('active', models.DateTimeField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cr_on', models.DateTimeField(auto_created=True)),
                ('name_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('name_en', models.CharField(blank=True, max_length=100, null=True)),
                ('img', models.ImageField(upload_to='')),
                ('desc_uz', models.TextField(blank=True, null=True)),
                ('desc_ru', models.TextField(blank=True, null=True)),
                ('desc_en', models.TextField(blank=True, null=True)),
                ('price', models.ImageField(default=0, upload_to='')),
                ('unit', models.CharField(max_length=20)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('active', models.BooleanField(default=True)),
                ('cr_up', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.categories')),
            ],
        ),
    ]