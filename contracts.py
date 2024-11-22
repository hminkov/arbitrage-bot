from web3 import Web3

class ContractManager:
    def __init__(self, w3, config):
        self.w3 = w3
        self.config = config
        self.contracts = self._load_contracts()
        
    def _load_contracts(self):
        return {
            'weth': self._load_contract('WETH_ADDRESS', 'abi/weth.json'),
            'uniswap_v3': self._load_contract('UNISWAP_V3_ROUTER', 'abi/uniswap_v3_router.json'),
            'sushiswap': self._load_contract('SUSHISWAP_ROUTER', 'abi/sushiswap_router.json')
        }
        
    def _load_contract(self, address_key, abi_path):
        with open(abi_path, 'r') as f:
            abi = f.read()
        return self.w3.eth.contract(
            address=self.config.get(address_key),
            abi=abi
        )
