"""Integração com MercadoPago (esqueleto)."""
from backend.integrations.base import ExternalIntegration


class MercadoPagoIntegration(ExternalIntegration):
    def handle_event(self, payload):
        return {'status': 'received', 'source': 'mercadopago', 'payload': payload}
