import json
from tkinter.font import names

from Decrypto_DB.models import Cryptocurrency, Wallet, Asset, Transaction
import init_django_orm


def main():

    with open("wallets.json", "r") as file:
        wallets = json.load(file)

        cryptos = wallets.get("crypto", [])
        for crypto in cryptos:
            Cryptocurrency.objects.get_or_create(
                symbol=crypto["symbol"],
                name=crypto["name"],
                defaults={"description": crypto.get("description", "")}
            )










if __name__ == '__main__':
    main()