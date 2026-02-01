"""Workers assíncronos para notificações."""
from typing import Any


def send_notification(payload: Any) -> dict:
    return {'status': 'handled', 'payload': payload}
