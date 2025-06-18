class NFTContract:
    def __init__(self, web3, contract_address):
        self.web3 = web3
        self.contract_address = contract_address
        self.contract = self.load_contract()

    def load_contract(self):
        # Load the contract ABI and create a contract instance
        with open('path/to/NFTContractABI.json') as f:
            abi = json.load(f)
        return self.web3.eth.contract(address=self.contract_address, abi=abi)

    def mint_nft(self, recipient, token_id, metadata_uri):
        # Mint a new NFT
        tx_hash = self.contract.functions.mint(recipient, token_id, metadata_uri).transact()
        self.web3.eth.waitForTransactionReceipt(tx_hash)
        return tx_hash

    def transfer_nft(self, from_address, to_address, token_id):
        # Transfer an NFT from one address to another
        tx_hash = self.contract.functions.transferFrom(from_address, to_address, token_id).transact()
        self.web3.eth.waitForTransactionReceipt(tx_hash)
        return tx_hash

    def get_nft_metadata(self, token_id):
        # Retrieve metadata for a specific NFT
        return self.contract.functions.tokenURI(token_id).call()