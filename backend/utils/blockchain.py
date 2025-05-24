from web3 import Web3
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

# Avalanche C-Chain RPC URL
AVALANCHE_RPC = os.getenv("AVALANCHE_RPC", "https://api.avax.network/ext/bc/C/rpc")

def get_web3_connection() -> Web3:
    """
    Get a Web3 connection to Avalanche C-Chain.
    """
    w3 = Web3(Web3.HTTPProvider(AVALANCHE_RPC))
    if not w3.is_connected():
        raise ConnectionError("Failed to connect to Avalanche C-Chain")
    return w3

def get_contract_source(address: str) -> Optional[str]:
    """
    Get contract source code if verified on Snowtrace.
    This is a placeholder - implement actual Snowtrace API integration.
    """
    # TODO: Implement Snowtrace API integration
    return None

def is_contract(address: str) -> bool:
    """
    Check if an address is a contract.
    """
    w3 = get_web3_connection()
    code = w3.eth.get_code(address)
    return len(code) > 0 