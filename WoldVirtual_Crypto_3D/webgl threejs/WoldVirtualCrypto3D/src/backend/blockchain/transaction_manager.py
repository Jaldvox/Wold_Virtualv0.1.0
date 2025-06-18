from web3 import Web3

class TransactionManager:
    def __init__(self, web3_provider_url):
        self.web3 = Web3(Web3.HTTPProvider(web3_provider_url))

    def send_transaction(self, from_address, to_address, value, private_key):
        transaction = {
            'to': to_address,
            'value': self.web3.toWei(value, 'ether'),
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei'),
            'nonce': self.web3.eth.getTransactionCount(from_address),
        }

        signed_txn = self.web3.eth.account.signTransaction(transaction, private_key)
        txn_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return txn_hash.hex()

    def get_transaction_receipt(self, txn_hash):
        return self.web3.eth.getTransactionReceipt(txn_hash)

    def check_transaction_status(self, txn_hash):
        receipt = self.get_transaction_receipt(txn_hash)
        if receipt is None:
            return 'Pending'
        return 'Success' if receipt.status == 1 else 'Failed'