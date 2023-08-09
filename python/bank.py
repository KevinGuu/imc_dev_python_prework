from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class TransactionType(Enum):
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"


@dataclass
class Transaction:
    date: datetime
    transaction_type: TransactionType
    amount: int
    from_acc: str = None
    to_acc: str = None
