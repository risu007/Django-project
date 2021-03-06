# Generated by Django 3.0.5 on 2020-05-03 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orders_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.CharField(default='', max_length=9000),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=9000),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=9000),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=9000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.CharField(default='', max_length=1100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='city',
            field=models.CharField(default='', max_length=9000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='email',
            field=models.CharField(default='', max_length=9000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='items_json',
            field=models.CharField(max_length=9000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='name',
            field=models.CharField(default='', max_length=9000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=9000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='state',
            field=models.CharField(default='', max_length=9000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='zip_code',
            field=models.CharField(default='', max_length=9000),
        ),
        migrations.AlterField(
            model_name='orderupdate',
            name='update_desc',
            field=models.CharField(max_length=9000),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=9000),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=9000),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=9000),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='', max_length=9000),
        ),
    ]
