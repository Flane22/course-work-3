from datetime import datetime

def repair_date(receipt: dict):
    temp_date = datetime.strptime(receipt["date"][0:-7], '%Y-%m-%dT%H:%M:%S')
    receipt["date"] = temp_date.strftime("%d.%m.%Y")
    return receipt


def check_and_repair_from(receipt: dict):
    if not receipt.get("from"):
        receipt.update({"from": "Наличные средства"})
    return receipt


def hide_account_number(receipt: dict):
    if receipt.get("from")[0:4] == "Счет":
        receipt.update({"from": "Счет **"+receipt.get("from")[-4:]})
    elif receipt.get("from")[0:3] != "Нал":
        receipt.update({"from": f"{receipt.get("from")[:-12]} "
                                f"{receipt.get("from")[-12:-10]}** **** "
                                f"{receipt.get("from")[-4:]}"})

    if receipt.get("to")[0:4] == "Счет":
        receipt.update({"to": "Счет **"+receipt.get("to")[-4:]})
    else:
        receipt.update({"to": f"{receipt.get("to")[:-12]} "
                              f"{receipt.get("to")[-12:-10]}** **** "
                              f"{receipt.get("to")[-4:]}"})
    return receipt


def get_preformatted_receipt(receipt: dict):
    receipt = repair_date(receipt)
    receipt = check_and_repair_from(receipt)
    receipt = hide_account_number(receipt)
    return receipt


def get_formatted_receipt(receipt: dict):
    return (f"{receipt["date"]} {receipt["description"]}\n"
        f"{receipt["from"]} -> {receipt["to"]}\n"
        f"{receipt["operationAmount"]["amount"]} {receipt["operationAmount"]["currency"]["name"]}\n")


def get_executed_receipts(receipt_list: list):
    result_list = []
    for i in receipt_list:
        if i.get("state") == "EXECUTED":
            result_list.append(i)
    return result_list


def get_latest_receipts(count: int, receipt_list: list):
    result_list = sorted(receipt_list, key=lambda receipt: receipt["date"], reverse=True)[0:count]
    return result_list
