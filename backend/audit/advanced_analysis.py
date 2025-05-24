from typing import List, Dict, Any
from web3 import Web3
from utils.blockchain import get_web3_connection

# Transaction History Analysis
def get_transaction_history(address: str, max_blocks: int = 500) -> List[Dict[str, Any]]:
    w3 = get_web3_connection()
    latest_block = w3.eth.block_number
    txs = []
    for block_num in range(max(latest_block - max_blocks, 0), latest_block + 1):
        block = w3.eth.get_block(block_num, full_transactions=True)
        for tx in block.transactions:
            if tx.get('to', '').lower() == address.lower() or tx.get('from', '').lower() == address.lower():
                txs.append({
                    'hash': tx['hash'].hex(),
                    'from': tx['from'],
                    'to': tx['to'],
                    'value': float(w3.from_wei(tx['value'], 'ether')),
                    'block_number': block_num,
                    'timestamp': block['timestamp'],
                })
    return txs

# Token Flow Tracking (ERC20 transfers)
def get_token_flows(address: str, max_blocks: int = 500) -> List[Dict[str, Any]]:
    w3 = get_web3_connection()
    latest_block = w3.eth.block_number
    transfer_topic = w3.keccak(text='Transfer(address,address,uint256)').hex()
    logs = w3.eth.get_logs({
        'fromBlock': max(latest_block - max_blocks, 0),
        'toBlock': latest_block,
        'topics': [transfer_topic, None, None],
    })
    flows = []
    for log in logs:
        if len(log['topics']) < 3:
            continue
        from_addr = '0x' + log['topics'][1].hex()[-40:]
        to_addr = '0x' + log['topics'][2].hex()[-40:]
        if address.lower() in [from_addr.lower(), to_addr.lower()]:
            flows.append({
                'tx_hash': log['transactionHash'].hex(),
                'from': from_addr,
                'to': to_addr,
                'value': int(log['data'], 16),
                'block_number': log['blockNumber'],
            })
    return flows

# Gas Usage Optimization (basic)
def analyze_gas_usage(address: str) -> Dict[str, Any]:
    w3 = get_web3_connection()
    txs = get_transaction_history(address, max_blocks=200)
    if not txs:
        return {'average_gas': 0, 'max_gas': 0, 'min_gas': 0, 'tx_count': 0}
    gas_used = []
    for tx in txs:
        try:
            receipt = w3.eth.get_transaction_receipt(tx['hash'])
            gas_used.append(receipt['gasUsed'])
        except Exception:
            continue
    if not gas_used:
        return {'average_gas': 0, 'max_gas': 0, 'min_gas': 0, 'tx_count': len(txs)}
    return {
        'average_gas': sum(gas_used) / len(gas_used),
        'max_gas': max(gas_used),
        'min_gas': min(gas_used),
        'tx_count': len(gas_used),
    }

# Contract Interaction Patterns
def get_interaction_patterns(address: str, max_blocks: int = 500) -> Dict[str, int]:
    w3 = get_web3_connection()
    latest_block = w3.eth.block_number
    interactions = {}
    for block_num in range(max(latest_block - max_blocks, 0), latest_block + 1):
        block = w3.eth.get_block(block_num, full_transactions=True)
        for tx in block.transactions:
            if tx.get('to', '').lower() == address.lower():
                sender = tx['from'].lower()
                interactions[sender] = interactions.get(sender, 0) + 1
    return interactions 