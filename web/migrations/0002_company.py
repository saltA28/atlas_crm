# Generated by Django 2.2.1 on 2019-12-09 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='企业名')),
                ('money', models.CharField(max_length=32, verbose_name='注册资本')),
                ('money_true', models.CharField(max_length=32, verbose_name='实缴资本')),
                ('flag_date', models.CharField(max_length=32, verbose_name='成立日期')),
                ('state', models.CharField(max_length=32, verbose_name='经营状态')),
                ('code', models.CharField(max_length=64, verbose_name='统一社会信用代码')),
                ('register_code', models.CharField(max_length=64, verbose_name='工商注册号')),
                ('user_number', models.CharField(max_length=64, verbose_name='纳税人识别号')),
                ('company_code', models.CharField(max_length=64, verbose_name='组织机构代码')),
                ('company_type', models.CharField(max_length=64, verbose_name='公司类型')),
                ('industry', models.CharField(max_length=64, verbose_name='行业')),
                ('check_date', models.CharField(max_length=64, verbose_name='核准日期')),
                ('registration_authority', models.CharField(max_length=64, verbose_name='登记机关')),
                ('business_term', models.CharField(max_length=64, verbose_name='营业期限')),
                ('taxpayer_qualification', models.CharField(max_length=64, verbose_name='纳税人资质')),
                ('people', models.CharField(max_length=64, verbose_name='人员规模')),
                ('registrations_people', models.CharField(max_length=64, verbose_name='参保人数')),
                ('once_name', models.CharField(max_length=64, verbose_name='曾用名')),
                ('english_name', models.CharField(max_length=64, verbose_name='英文名称')),
                ('address', models.CharField(max_length=64, verbose_name='注册地址')),
                ('text', models.CharField(max_length=10000, verbose_name='经营范围')),
            ],
        ),
    ]
