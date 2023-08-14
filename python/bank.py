from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List
from uuid import UUID, uuid4


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


@dataclass
class Account:
    account_holder: str
    account_numer: UUID
    balance: int = 0
    transactions: List[Transaction] = field(default_factory=list)

    def __str__(self):
        return (
            f"----- Account Statement ----- \n"
            f"Account Number: {self.account_numer:>10} | "
            f"Account Holder: {self.account_holder:>10}\n"
            f"Balance: {self.balance:>10}\n"
        )

    def __lt__(self, other):
        if isinstance(other, Account):
            if self.balance < other.balance:
                return f"{self.account_numer}'s balance of ${self.balance} is less than {other.account_numer}'s balance of ${other.balance}"
            elif self.balance == other.balance:
                return f"{self.account_numer}'s balance of ${self.balance} is the same as {other.account_numer}'s balance of ${other.balance}"
            else:
                return f"{self.account_numer}'s balance of ${self.balance} is greater than {other.account_numer}'s balance of ${other.balance}"
        else:
            raise TypeError(
                f"{other} is of type: {type(other)}, does not match {type(self)}"
            )
