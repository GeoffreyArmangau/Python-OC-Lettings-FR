from django.db import migrations


def copy_profiles_data(apps, schema_editor):
    """Copy existing Profile rows from oc_lettings_site into profiles."""
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')

    for old_profile in OldProfile.objects.all():
        NewProfile.objects.create(
            id=old_profile.id,
            user_id=old_profile.user_id,
            favorite_city=old_profile.favorite_city,
        )


def remove_profiles_data(apps, schema_editor):
    """Reverse migration: empty the profiles table."""
    NewProfile = apps.get_model('profiles', 'Profile')
    NewProfile.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_profiles_data, remove_profiles_data),
    ]
