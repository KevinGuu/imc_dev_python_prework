from bank import Bank
import os
import random
import string


def generate_random_string(length: int = 10):
    """Generates random strings."""
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


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
    for _ in range(10000):
        random_accounts = random.sample(
            new_accounts_holders, 2
        )  # randomly choose 2 accounts from sample list
        try:
            bank.transfer(
                random_accounts[0], random_accounts[1], random.randint(1, 20000)
            )
        except ValueError as e:  # catch dis
            print(e)
            pass
        else:
            count += 1
    print(f"{count} valid transactions.")
    print(bank.find_inactive_accounts())


if __name__ == "__main__":
    main()
