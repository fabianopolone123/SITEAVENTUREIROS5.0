"""Rotinas de retenção para os eventos de diagnóstico."""
from datetime import timedelta

from django.utils import timezone


def cleanup_events(model):
    threshold = timezone.now() - timedelta(days=30)
    model.objects.filter(ts__lt=threshold).delete()
