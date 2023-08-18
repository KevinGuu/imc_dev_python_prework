import os
import random
import signal
import string
import sys

import mysql.connector

from bank import Bank

db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "localhost"),
    port=os.getenv("MYSQL_PORT", 3306),
    user=os.getenv("MYSQL_USER", "kevin"),
    password=os.getenv("MYSQL_PASSWORD", "ftw"),
    database=os.getenv("MYSQL_DATABASE", "prework"),
)
print(db)


def generate_random_string(length: int = 10):
    """Generates random strings."""
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


def handle_kill_signal():
    print("Received kill signal, terminating script.")
    sys.exit(0)


signal.signal(signal.SIGTERM, handle_kill_signal)


def main():
    # create the bank
    bank = Bank(
        name="Kevin's Bank", transactions_file_dir=f"{os.getcwd()}/transactions/"
    )
    # generate 100 random users names
    new_accounts_holders = [generate_random_string() for _ in range(1000)]

    # populate bank with 100 random users
    bank.create_accounts_from_list(new_accounts_holders)

    # deposit random amount into each account
    for key, _ in bank.ledger.items():
        bank.deposit(key, random.randint(50, 50000))

    # simulate 1000 random transactions
    count = 0
    amount = 0
    try:
        while True:
            # randomly choose 2 accounts from sample list
            random_accounts = random.sample(new_accounts_holders, 2)
            try:
                tmp = random.randint(1, 20000)
                amount += tmp
                bank.transfer(random_accounts[0], random_accounts[1], tmp)
            except ValueError as e:  # catch dis
                print(e)
                pass
            else:
                print(
                    f"{count:>10} - {random_accounts[0]} -> {random_accounts[1]}, new balances ${bank.get_account_info(random_accounts[0]).balance}, ${bank.get_account_info(random_accounts[1]).balance}"
                )
                count += 1
    except KeyboardInterrupt:
        print(f"Processed {count} transactions, volume ${amount}")
        # print(bank.find_inactive_accounts())
        sys.exit(0)


if __name__ == "__main__":
    main()
