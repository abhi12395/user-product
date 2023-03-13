# Generated by Django 4.1.5 on 2023-03-13 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30, verbose_name='TITLE')),
                ('description', models.TextField()),
                ('Unique_id', models.CharField(max_length=30, unique=True, verbose_name='Unique id')),
                ('price', models.FloatField(verbose_name='price')),
            ],
        ),
        migrations.CreateModel(
            name='productImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='IMAGE')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productmain', verbose_name='Product Image')),
            ],
        ),
    ]