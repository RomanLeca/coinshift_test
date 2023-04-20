"""
This module contains api tests that verify payload details.
Tests receive a prepared indexer payload from the conftest module scoped fixture.
"""
from settings import HASH_VALUE, TO_ADDRESS, FROM_ADDRESS


def test_hash(indexer_payload):
    assert indexer_payload["hash"] == HASH_VALUE


def test_token(indexer_payload):
    assert indexer_payload["token"] == "WETH"


def test_amount(indexer_payload):
    assert indexer_payload["amount"] == 2.4029381585039946


def test_type(indexer_payload):
    assert indexer_payload["type"] == "ERC20_TRANSFER"


def test_to_address(indexer_payload):
    assert indexer_payload["to_address"] == TO_ADDRESS


def test_from_address(indexer_payload):
    assert indexer_payload["from_address"] == FROM_ADDRESS
