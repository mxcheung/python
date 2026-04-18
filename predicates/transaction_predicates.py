"""Predicates and validators for transaction dictionaries.

Provide small, composable predicate functions that check expected structure and
semantics of a transaction represented as a Python dict, and a top-level
`assert_transaction` function that raises AssertionError with a helpful message
when validation fails.

Example transaction shape expected:
{
    "id": "tx-123",
    "amount": 12.34,
    "currency": "USD",
    "date": "2023-01-01T12:34:56",
    "sender": {"id": "alice", "account": "AC123"},
    "receiver": {"id": "bob", "account": "AC456"},
    "status": "completed"
}
"""
from __future__ import annotations

from decimal import Decimal, InvalidOperation
from datetime import datetime
import re
from typing import Any, Dict, Optional, Tuple

REQUIRED_KEYS = {"id", "amount", "currency", "date", "sender", "receiver", "status"}
ALLOWED_STATUSES = {"pending", "completed", "failed", "cancelled"}
_CURRENCY_RE = re.compile(r"^[A-Z]{3}$")


def is_dict(obj: Any) -> bool:
    return isinstance(obj, dict)


def has_required_keys(tx: Dict[str, Any]) -> bool:
    return REQUIRED_KEYS.issubset(set(tx.keys()))


def is_amount_valid(tx: Dict[str, Any]) -> bool:
    """Amount should be convertible to Decimal and non-negative."""
    if "amount" not in tx:
        return False
    try:
        amt = Decimal(str(tx["amount"]))
    except (InvalidOperation, ValueError, TypeError):
        return False
    return amt >= 0


def is_currency_valid(tx: Dict[str, Any]) -> bool:
    v = tx.get("currency")
    return isinstance(v, str) and bool(_CURRENCY_RE.match(v))


def is_date_valid(tx: Dict[str, Any]) -> bool:
    """Accept ISO-8601-like timestamps parseable by datetime.fromisoformat."""
    v = tx.get("date")
    if not isinstance(v, str):
        return False
    try:
        # datetime.fromisoformat handles many ISO-8601 variants (py3.7+)
        datetime.fromisoformat(v)
        return True
    except (ValueError, TypeError):
        return False


def is_party_valid(p: Any) -> bool:
    """A valid party is a dict with at least one identifier (id or name).

    If `account` is present it must be a string.
    """
    if not isinstance(p, dict):
        return False
    if not (isinstance(p.get("id"), str) or isinstance(p.get("name"), str)):
        return False
    if "account" in p and not isinstance(p["account"], str):
        return False
    return True


def is_status_valid(tx: Dict[str, Any]) -> bool:
    return isinstance(tx.get("status"), str) and tx.get("status") in ALLOWED_STATUSES


def validate_transaction(tx: Any) -> Tuple[bool, Optional[str]]:
    """Validate transaction and return (is_valid, error_message).

    This is a non-raising variant useful for conditional checks.
    """
    if not is_dict(tx):
        return False, "transaction must be a dict"
    if not has_required_keys(tx):
        missing = REQUIRED_KEYS.difference(set(tx.keys()))
        return False, f"missing required keys: {sorted(missing)}"
    if not is_amount_valid(tx):
        return False, "invalid amount: must be a number (convertible to Decimal) and non-negative"
    if not is_currency_valid(tx):
        return False, "invalid currency: expected 3-letter ISO currency code (e.g. USD)"
    if not is_date_valid(tx):
        return False, "invalid date: expected ISO-8601 string parseable by datetime.fromisoformat"
    if not is_party_valid(tx.get("sender")):
        return False, "invalid sender: expected dict with at least 'id' or 'name', optional 'account' as string"
    if not is_party_valid(tx.get("receiver")):
        return False, "invalid receiver: expected dict with at least 'id' or 'name', optional 'account' as string"
    if not is_status_valid(tx):
        return False, f"invalid status: must be one of {sorted(ALLOWED_STATUSES)}"
    return True, None


def assert_transaction(tx: Any) -> None:
    """Assert that `tx` is a valid transaction dict.

    Raises AssertionError with a helpful message on failure. Use this when you
    want immediate feedback in tests or runtime checks.
    """
    ok, err = validate_transaction(tx)
    if not ok:
        raise AssertionError(err)


__all__ = [
    "is_dict",
    "has_required_keys",
    "is_amount_valid",
    "is_currency_valid",
    "is_date_valid",
    "is_party_valid",
    "is_status_valid",
    "validate_transaction",
    "assert_transaction",
]
