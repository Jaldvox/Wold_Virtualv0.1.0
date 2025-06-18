class TokenContract:
    def __init__(self, web3, contract_address):
        self.web3 = web3
        self.contract_address = contract_address
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=self.get_abi())

    def get_abi(self):
        # Define the ABI for the token contract
        return [
            {
                "constant": True,
                "inputs": [],
                "name": "name",
                "outputs": [{"name": "", "type": "string"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            },
            {
                "constant": True,
                "inputs": [],
                "name": "symbol",
                "outputs": [{"name": "", "type": "string"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            },
            {
                "constant": True,
                "inputs": [],
                "name": "decimals",
                "outputs": [{"name": "", "type": "uint8"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            },
            {
                "constant": True,
                "inputs": [],
                "name": "totalSupply",
                "outputs": [{"name": "", "type": "uint256"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            },
            {
                "constant": True,
                "inputs": [{"name": "owner", "type": "address"}],
                "name": "balanceOf",
                "outputs": [{"name": "", "type": "uint256"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            },
            {
                "constant": False,
                "inputs": [{"name": "to", "type": "address"}, {"name": "value", "type": "uint256"}],
                "name": "transfer",
                "outputs": [{"name": "", "type": "bool"}],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function",
            },
            {
                "constant": False,
                "inputs": [{"name": "from", "type": "address"}, {"name": "to", "type": "address"}, {"name": "value", "type": "uint256"}],
                "name": "transferFrom",
                "outputs": [{"name": "", "type": "bool"}],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function",
            },
            {
                "constant": False,
                "inputs": [{"name": "spender", "type": "address"}, {"name": "value", "type": "uint256"}],
                "name": "approve",
                "outputs": [{"name": "", "type": "bool"}],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function",
            },
            {
                "constant": True,
                "inputs": [{"name": "owner", "type": "address"}, {"name": "spender", "type": "address"}],
                "name": "allowance",
                "outputs": [{"name": "", "type": "uint256"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            },
        ]

    def name(self):
        return self.contract.functions.name().call()

    def symbol(self):
        return self.contract.functions.symbol().call()

    def decimals(self):
        return self.contract.functions.decimals().call()

    def total_supply(self):
        return self.contract.functions.totalSupply().call()

    def balance_of(self, owner):
        return self.contract.functions.balanceOf(owner).call()

    def transfer(self, to, value, account):
        tx = self.contract.functions.transfer(to, value).buildTransaction({
            'from': account,
            'nonce': self.web3.eth.getTransactionCount(account),
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei')
        })
        signed_tx = self.web3.eth.account.signTransaction(tx, private_key='YOUR_PRIVATE_KEY')
        return self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)

    def transfer_from(self, from_address, to, value, account):
        tx = self.contract.functions.transferFrom(from_address, to, value).buildTransaction({
            'from': account,
            'nonce': self.web3.eth.getTransactionCount(account),
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei')
        })
        signed_tx = self.web3.eth.account.signTransaction(tx, private_key='YOUR_PRIVATE_KEY')
        return self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)

    def approve(self, spender, value, account):
        tx = self.contract.functions.approve(spender, value).buildTransaction({
            'from': account,
            'nonce': self.web3.eth.getTransactionCount(account),
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei')
        })
        signed_tx = self.web3.eth.account.signTransaction(tx, private_key='YOUR_PRIVATE_KEY')
        return self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)

    def allowance(self, owner, spender):
        return self.contract.functions.allowance(owner, spender).call()