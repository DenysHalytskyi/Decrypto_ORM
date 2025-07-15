import init_django_orm
from Decrypto_DB.models import Cryptocurrency, Wallet, Asset, Transaction
import json


def main():

    with open("wallets.json", "r") as file:
        crypto_portfolio = json.load(file)

        cryptos_info = crypto_portfolio.get("crypto", [])
        crypto_map = {}
        for crypto_info in cryptos_info:
            crypto, _ = Cryptocurrency.objects.get_or_create(
                symbol=crypto_info["symbol"],
                name=crypto_info["name"],
                defaults={"description": crypto_info.get("description", "")}
            )
            crypto_map[crypto.symbol] = crypto


        wallets_data = crypto_portfolio.get("wallets", [])
        for wallet_data in wallets_data:
            wallet, _ = Wallet.objects.get_or_create(
                address=wallet_data["address"],
                owner=wallet_data["owner"],
            )

            assets_info = wallet_data.get("asset", [])
            for asset_info in assets_info:
                symbol = asset_info["symbol"]
                crypto = crypto_map.get(symbol, None)

                asset, _ = Asset.objects.get_or_create(
                    crypto=crypto,
                    wallet=wallet,
                    defaults={"amount": assets_info["amount"]}
                )

            transactions_info = wallet_data.get("transactions", [])
            for transaction_info in transactions_info:
                symbol = transaction_info["symbol"]
                crypto = crypto_map.get(symbol, None)

                transaction, _ = Transaction.objects.get_or_create(
                    tx_id=transaction_info["tx_id"],
                    wallet=wallet,
                    crypto=crypto,
                    amount=transaction_info["amount"],
                    note=transaction_info["note"]
                )







if __name__ == '__main__':
    main()