"""Buster World Admin Configuration."""

from django.contrib import admin
from . import models

admin.site.register(models.PlayerStats)