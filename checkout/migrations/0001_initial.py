# Generated by Django 4.0 on 2021-12-12 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('apartment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=100)),
                ('fees', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_number', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('fees', models.FloatField(default=5)),
                ('status', models.CharField(choices=[('New', 'New'), ('Review', 'Review'), ('Accepted', 'Accepted')], default='New', max_length=10)),
                ('is_ordered', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('apartment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apartment.apartment')),
                ('transaction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.transaction')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.account')),
            ],
        ),
    ]
