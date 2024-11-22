import os
from decimal import Decimal
from web3 import Web3

def load_config():
    return {
        'min_profit_threshold': Decimal(os.getenv('MIN_PROFIT_THRESHOLD', '0.001')),
        'max_slippage': Decimal(os.getenv('MAX_SLIPPAGE', '0.005')),
        'gas_price_limit': Web3.to_wei(os.getenv('GAS_PRICE_LIMIT', '100'), 'gwei'),
        'max_retries': int(os.getenv('MAX_RETRIES', '3')),
        'delay_between_trades': float(os.getenv('DELAY_BETWEEN_TRADES', '1.5')),
        'flashbots_rpc_url': os.getenv('FLASHBOTS_RPC_URL'),
        'eth_node_url': os.getenv('ETH_NODE_URL'),
        'private_key': os.getenv('PRIVATE_KEY'),
    }
