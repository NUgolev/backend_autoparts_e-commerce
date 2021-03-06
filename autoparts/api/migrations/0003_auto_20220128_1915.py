# Generated by Django 2.2.19 on 2021-12-01 09:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_auto_20220128_1913"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sessions", "0001_initial"),
        ("auth", "0011_update_proxy_permissions"),
        ("contenttypes", "0002_remove_content_type_name"),
        ("admin", "0003_logentry_add_action_flag_choices"),
    ]

    operations = [
        # create django, account schema
        migrations.RunSQL("CREATE SCHEMA IF NOT EXISTS django;"),
        migrations.RunSQL("CREATE SCHEMA IF NOT EXISTS account;"),
        migrations.RunSQL("SET search_path TO public, account, django;"),
        # move tables
        migrations.RunSQL("ALTER TABLE django_admin_log SET SCHEMA django;"),
        migrations.RunSQL("ALTER TABLE django_content_type SET SCHEMA django;"),
        migrations.RunSQL("ALTER TABLE django_migrations SET SCHEMA django;"),
        migrations.RunSQL("ALTER TABLE django_session SET SCHEMA django;"),
        migrations.RunSQL("ALTER TABLE auth_group SET SCHEMA account;"),
        migrations.RunSQL("ALTER TABLE auth_group_permissions SET SCHEMA account;"),
        migrations.RunSQL("ALTER TABLE auth_permission SET SCHEMA account;"),
        migrations.RunSQL("ALTER TABLE auth_user SET SCHEMA account;"),
        migrations.RunSQL("ALTER TABLE auth_user_groups SET SCHEMA account;"),
        migrations.RunSQL("ALTER TABLE auth_user_user_permissions SET SCHEMA account;"),
    ]
