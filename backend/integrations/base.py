"""Classes base para integrações externas."""
from abc import ABC, abstractmethod


class ExternalIntegration(ABC):
    """Interface mínima para integrações externas."""

    @abstractmethod
    def handle_event(self, payload):
        raise NotImplementedError
