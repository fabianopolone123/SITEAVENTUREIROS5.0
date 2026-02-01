"""Máscaras para dados sensíveis."""
from typing import Dict, Any


def mask_sensitive(payload: Dict[str, Any]) -> Dict[str, Any]:
    masked = payload.copy()
    for key in ('password', 'token', 'authorization'):
        if key in masked:
            masked[key] = '***'
    return masked
