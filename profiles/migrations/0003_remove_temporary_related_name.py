from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Drop the temporary related_name used while oc_lettings_site.Profile still existed."""

    dependencies = [
        ('profiles', '0002_copy_data_from_oc_lettings_site'),
        ('oc_lettings_site', '0002_delete_moved_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
