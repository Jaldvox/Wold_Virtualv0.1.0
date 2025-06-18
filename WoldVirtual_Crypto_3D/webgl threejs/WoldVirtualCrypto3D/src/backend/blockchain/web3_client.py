from web3 import Web3

class Web3Client:
    def __init__(self, provider_url):
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        self.check_connection()

    def check_connection(self):
        if not self.web3.isConnected():
            raise Exception("Failed to connect to the Ethereum network")

    def get_balance(self, address):
        """Retrieve the balance of an Ethereum address."""
        balance_wei = self.web3.eth.get_balance(address)
        return self.web3.fromWei(balance_wei, 'ether')

    def send_transaction(self, from_address, to_address, amount, private_key):
        """Send Ether from one address to another."""
        nonce = self.web3.eth.get_transaction_count(from_address)
        transaction = {
            'to': to_address,
            'value': self.web3.toWei(amount, 'ether'),
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei'),
            'nonce': nonce,
        }
        signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key)
        txn_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return txn_hash.hex()

    def get_transaction_receipt(self, txn_hash):
        """Retrieve the receipt of a transaction."""
        return self.web3.eth.get_transaction_receipt(txn_hash)

    def get_block(self, block_identifier):
        """Retrieve a block by its identifier."""
        return self.web3.eth.get_block(block_identifier)

    def get_latest_block(self):
        """Retrieve the latest block."""
        return self.get_block('latest')