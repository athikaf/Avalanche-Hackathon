from typing import List, Dict
from web3 import Web3
from utils.blockchain import get_web3_connection
import time
from datetime import datetime, timedelta

# Minimum transaction value to consider as whale activity (in AVAX)
MIN_WHALE_AMOUNT = 1000

def get_whale_alerts() -> List[Dict]:
    """
    Get recent whale activity alerts from Avalanche C-Chain.
    
    Returns:
        List[Dict]: List of whale activity alerts
    """
    w3 = get_web3_connection()
    
    # Get latest block
    latest_block = w3.eth.block_number
    
    # Look at last 100 blocks
    start_block = latest_block - 100
    
    alerts = []
    
    for block_num in range(start_block, latest_block + 1):
        block = w3.eth.get_block(block_num, full_transactions=True)
        
        for tx in block.transactions:
            # Skip contract creation
            if not tx.get('to'):
                continue
                
            # Convert value from wei to AVAX
            value_in_avax = w3.from_wei(tx['value'], 'ether')
            
            if value_in_avax >= MIN_WHALE_AMOUNT:
                alerts.append({
                    'tx_hash': tx['hash'].hex(),
                    'from': tx['from'],
                    'to': tx['to'],
                    'value_avax': float(value_in_avax),
                    'timestamp': datetime.fromtimestamp(block['timestamp']).isoformat(),
                    'block_number': block_num
                })
    
    return alerts

def monitor_whale_activity(callback=None):
    """
    Continuously monitor for whale activity.
    
    Args:
        callback: Optional callback function to handle new alerts
    """
    w3 = get_web3_connection()
    last_block = w3.eth.block_number
    
    while True:
        try:
            current_block = w3.eth.block_number
            
            if current_block > last_block:
                alerts = get_whale_alerts()
                if alerts and callback:
                    callback(alerts)
                    
            last_block = current_block
            time.sleep(1)  # Poll every second
            
        except Exception as e:
            print(f"Error monitoring whale activity: {e}")
            time.sleep(5)  # Wait longer on error 