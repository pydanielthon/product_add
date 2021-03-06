# Generated by Django 3.0.3 on 2020-02-09 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.RenameField(
            model_name='products',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='products',
            name='stock',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10000),
        ),
        migrations.AddField(
            model_name='products',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10000),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=99999),
        ),
        migrations.AddField(
            model_name='products',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.categories'),
        ),
    ]
