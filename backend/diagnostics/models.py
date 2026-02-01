"""Modelos para armazenar eventos de diagnóstico."""
from django.db import models


class DiagnosticEvent(models.Model):
    LEVEL_CHOICES = [
        ('debug', 'Debug'),
        ('info', 'Info'),
        ('warn', 'Warn'),
        ('error', 'Error'),
    ]

    ts = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='info')
    source = models.CharField(max_length=32)
    event_name = models.CharField(max_length=64)
    message = models.TextField(blank=True, null=True)
    session_id = models.CharField(max_length=64, blank=True, null=True)
    trace_id = models.CharField(max_length=64, blank=True, null=True)
    request_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    route = models.CharField(max_length=128, blank=True, null=True)
    action = models.CharField(max_length=128, blank=True, null=True)
    duration_ms = models.PositiveIntegerField(blank=True, null=True)
    http_method = models.CharField(max_length=6, blank=True, null=True)
    http_status = models.PositiveSmallIntegerField(blank=True, null=True)
    tags = models.JSONField(blank=True, null=True)
    payload = models.JSONField(blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['-ts']),
            models.Index(fields=['session_id', 'ts']),
            models.Index(fields=['trace_id', 'ts']),
            models.Index(fields=['request_id']),
            models.Index(fields=['level', 'ts']),
        ]
