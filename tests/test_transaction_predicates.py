import copy
import pytest

from predicates.transaction_predicates import validate_transaction, assert_transaction


VALID_TX = {
    "id": "tx-123",
    "amount": "12.34",
    "currency": "USD",
    "date": "2023-01-01T12:34:56",
    "sender": {"id": "alice", "account": "AC123"},
    "receiver": {"id": "bob", "account": "AC456"},
    "status": "completed",
}


def test_validate_valid_transaction():
    ok, err = validate_transaction(VALID_TX)
    assert ok is True
    assert err is None


def test_assert_transaction_does_not_raise():
    # should not raise for a valid transaction
    assert_transaction(VALID_TX)


@pytest.mark.parametrize(
    "mutator, expected_substr",
    [
        (lambda t: t.pop("id"), "missing required keys"),
        (lambda t: t.update({"amount": "-5"}), "invalid amount"),
        (lambda t: t.update({"currency": "usd"}), "invalid currency"),
        (lambda t: t.update({"date": "not-a-date"}), "invalid date"),
        (lambda t: t.update({"sender": None}), "invalid sender"),
        (lambda t: t.update({"receiver": {}}), "invalid receiver"),
        (lambda t: t.update({"status": "unknown"}), "invalid status"),
    ],
)
def test_validate_invalid_transactions(mutator, expected_substr):
    tx = copy.deepcopy(VALID_TX)
    mutator(tx)
    ok, err = validate_transaction(tx)
    assert ok is False
    assert err is not None
    assert expected_substr in err
