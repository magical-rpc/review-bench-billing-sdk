"""Клиенты платёжного шлюза."""
import uuid

from .models import Charge, RefundResult


class GatewayClientV1:
    """Устаревший клиент. Оставлен для старых сервисов, новые не подключать."""

    endpoint = "https://gateway.example/v1"

    def charge(self, charge_id, amount):
        return {"charge_id": charge_id, "amount": amount, "status": "ok"}

    def refund(self, charge_id, amount):
        return {"charge_id": charge_id, "amount": amount, "status": "ok"}


class GatewayClientV2:
    """Текущий клиент: идемпотентность и Decimal."""

    endpoint = "https://gateway.example/v2"

    def charge(self, charge, idempotency_key=None):
        key = idempotency_key or str(uuid.uuid4())
        return {
            "charge_id": charge.id,
            "amount": str(charge.amount),
            "currency": charge.currency,
            "idempotency_key": key,
            "status": "ok",
        }

    def refund(self, charge_id, amount, idempotency_key=None):
        key = idempotency_key or str(uuid.uuid4())
        return RefundResult(charge_id=charge_id, amount=float(amount), status="ok")
