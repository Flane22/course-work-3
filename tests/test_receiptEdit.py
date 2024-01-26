from utils.receiptEdit import *


def test_repair_date(latest):
    source, result = latest
    assert repair_date(source[0]).get("date") == result[0].get("date")
    assert repair_date(source[1]).get("date") == result[1].get("date")


def test_check_and_repair_from(latest):
    source, result = latest
    assert check_and_repair_from(source[0]).get("from") == result[0].get("from")


def test_hide_account_number(latest):
    source, result = latest
    assert (hide_account_number(source[1]).get("from") == result[1].get("from")
            and hide_account_number(source[1]).get("to") == result[1].get("to"))
    assert (hide_account_number(source[3]).get("from") == result[3].get("from")
            and hide_account_number(source[3]).get("to") == result[3].get("to"))


def test_get_preformatted_receipt(latest):
    source, result = latest
    print("source - >", source[0])
    print("result - >", result[0])
    assert get_preformatted_receipt(source[0]) == result[0]


def test_get_formatted_receipt(receipts):
    source, result = receipts
    assert get_formatted_receipt(source[0]) == result[0]
    assert get_formatted_receipt(source[1]) == result[1]


def test_get_latest_receipts(source_list):
    assert get_latest_receipts(3, source_list) == source_list[:3]


def test_get_executed_receipts(source_list):
    assert get_executed_receipts(source_list) == source_list[:5]
