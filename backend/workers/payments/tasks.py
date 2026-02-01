"""Workers assíncronos para pagamentos."""
from typing import Any


def run_payment_job(payload: Any) -> dict:
    return {'status': 'queued', 'payload': payload}
