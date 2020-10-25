# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings

UNIQUE_EMAIL = getattr(settings, "ACCOUNT_UNIQUE_EMAIL", True)
EMAIL_MAX_LENGTH = getattr(settings, "ACCOUNT_EMAIL_MAX_LENGTH", 254)
MAX_EMAIL_CONFIRMATION_ATTEMPTS = getattr(
    settings,
    "ACCOUNT_MAX_EMAIL_CONFIRMATION_ATTEMPTS",
    None,
)


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailaddress",
            name="email",
            field=models.EmailField(
                unique=UNIQUE_EMAIL,
                max_length=EMAIL_MAX_LENGTH,
                verbose_name="e-mail address",
            ),
        ),
    ]

    if not UNIQUE_EMAIL:
        operations += [
            migrations.AlterUniqueTogether(
                name="emailaddress",
                unique_together=set([("user", "email")]),
            ),
        ]

    if MAX_EMAIL_CONFIRMATION_ATTEMPTS:
        operations += [
            migrations.AddField(
                model_name="emailconfirmation",
                name="attempts_to_confirm",
                field=models.PositiveIntegerField(
                    verbose_name="attempts to confirm",
                    null=True,
                    default=0,
                )
            ),
        ]
