class BlockchainState:
    """Class to manage blockchain-related state and interactions."""

    def __init__(self):
        self.blockchain_data = {}
        self.transactions = []

    def add_transaction(self, transaction):
        """Add a new transaction to the blockchain."""
        self.transactions.append(transaction)

    def get_transactions(self):
        """Retrieve all transactions."""
        return self.transactions

    def update_blockchain_data(self, data):
        """Update the blockchain data."""
        self.blockchain_data.update(data)

    def get_blockchain_data(self):
        """Retrieve the current blockchain data."""
        return self.blockchain_data

    def clear_transactions(self):
        """Clear all transactions."""
        self.transactions.clear()