"""Serializers para o diagnóstico."""
from rest_framework import serializers


class DiagnosticEventSerializer(serializers.Serializer):
    event_name = serializers.CharField()
    level = serializers.ChoiceField(choices=['debug', 'info', 'warn', 'error'])
    source = serializers.CharField()
    payload = serializers.JSONField(required=False)
