import csv
import os.path
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


class Bank:
    def __init__(self, name: str, transactions_file_dir: str):
        self.name = name
        # can add additional map of account_number : account_holder to ensure uniqueness
        self.ledger = {}  # account_holder(str):Account(object)

        # create dir if needed and generate file name
        if not os.path.exists(transactions_file_dir):
            os.mkdir(transactions_file_dir)
        self.transactions_file_name = f"{transactions_file_dir}{name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"

        # create file with headers on bank creation
        with open(self.transactions_file_name, "w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(
                ["Datetime", "Account Number", "Credit", "Debit", "Balance"]
            )

    def get_account_info(self, account_holder: str) -> Account:
        if (account_object := self.ledger.get(account_holder, None)) is None:
            raise ValueError(f"{account_holder} isn't a valid account holder.")
        return account_object

    def create_accounts_from_list(self, account_list: List[str]) -> None:
        self.ledger.update(
            {
                account_holder: Account(account_holder, uuid4())
                for account_holder in account_list
            }
        )

    def deposit(self, account_holder: str, amount: int) -> None:
        if (account_object := self.ledger.get(account_holder, None)) is None:
            raise ValueError(f"{account_holder} isn't a valid account holder.")
        account_object.balance += amount

    def withdraw(self, account_holder: str, amount: int) -> None:
        if (account_object := self.ledger.get(account_holder, None)) is None:
            raise ValueError(f"{account_holder} isn't a valid account holder.")
        if account_object.balance < amount:
            raise ValueError(
                f"{account_holder}'s balance: ${account_object.balance} is less than the requested withdrawal amount of: ${amount}"
            )
        account_object.balance -= amount

    def transfer(self, from_account: str, to_account: str, amount: int):
        # check for existence
        if (from_account_object := self.ledger.get(from_account, None)) is None:
            raise ValueError(f"{from_account} isn't a valid account holder.")
        if (to_account_object := self.ledger.get(to_account, None)) is None:
            raise ValueError(f"{to_account} isn't a valid account holder.")

        # check if account has sufficient balance
        if from_account_object.balance < amount:
            raise ValueError(
                f"               {from_account:}'s balance: ${from_account_object.balance} is less than the requested amount: ${amount}"
            )

        timestamp = datetime.now()

        # modify balance
        self.withdraw(from_account, amount)
        self.deposit(to_account, amount)

        # # add transaction to lists
        # from_account_object.transactions.append(
        #     Transaction(
        #         timestamp, TransactionType.DEBIT, amount, from_account, to_account
        #     )
        # )
        # to_account_object.transactions.append(
        #     Transaction(
        #         timestamp, TransactionType.CREDIT, amount, from_account, to_account
        #     )
        # )
        #
        # # write transactions to file, open in "append" mode
        # with open(self.transactions_file_name, "a", newline="") as file:
        #     csv_writer = csv.writer(file)
        #
        #     # from_account
        #     csv_writer.writerow(
        #         [timestamp, from_account, "", amount, from_account_object.balance]
        #     )
        #     # to_account
        #     csv_writer.writerow(
        #         [timestamp, to_account, amount, "", to_account_object.balance]
        #     )

    def find_inactive_accounts(self, count: int = 10) -> str:
        """Finds and returns accounts with transactions less than the given argument."""

        accounts = filter(
            lambda acc: len(acc.transactions) < count, self.ledger.values()
        )
        return f"{len(list(accounts))} have less than {count} transactions."
