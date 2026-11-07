from decimal import Decimal

from billing_sdk import Charge, GatewayClientV1, GatewayClientV2


def test_v1_charge_returns_ok():
    client = GatewayClientV1()
    assert client.charge("ch_1", 100.0)["status"] == "ok"


def test_v2_charge_keeps_decimal_amount():
    client = GatewayClientV2()
    result = client.charge(Charge(id="ch_2", amount=Decimal("100.10")))
    assert result["amount"] == "100.10"
    assert result["idempotency_key"]


def test_v2_refund_returns_decimal_and_key():
    client = GatewayClientV2()
    result = client.refund("ch_2", Decimal("10.05"), idempotency_key="refund-1")
    assert result.status == "ok"
    assert result.amount == Decimal("10.05")
    assert isinstance(result.amount, Decimal)
    assert result.idempotency_key == "refund-1"
