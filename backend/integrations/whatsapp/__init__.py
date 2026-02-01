"""Integração com WhatsApp (esqueleto)."""
from backend.integrations.base import ExternalIntegration


class WhatsAppIntegration(ExternalIntegration):
    def handle_event(self, payload):
        return {'status': 'received', 'source': 'whatsapp', 'payload': payload}
