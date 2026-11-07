"""Модели платежей и возвратов."""
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Charge:
    id: str
    amount: Decimal
    currency: str = "RUB"
    merchant_id: str = ""


@dataclass
class RefundResult:
    charge_id: str
    amount: Decimal
    status: str
    idempotency_key: str = ""
