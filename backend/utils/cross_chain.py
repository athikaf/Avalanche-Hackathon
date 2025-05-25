from typing import Dict, List, Optional
from web3 import Web3
import json
import os
from .blockchain import get_web3_connection, get_chain_config
from datetime import datetime
import requests

"""
Cross-chain analysis utilities for TrustMesh AI Dashboard

- Primary chain: Avalanche C-Chain (AVAX)
- Cross-chain communication: Chainlink CCIP or Chainlink nodes (to Ethereum, Polygon, etc.)
- Signature verification: Multi-validator set
"""

# Bridge contract ABIs
BRIDGE_ABIS = {
    'avalanche': {
        'bridge': json.loads('''[
            {"inputs":[],"name":"bridge","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[],"name":"getBridgeStatus","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}
        ]'''),
        'router': json.loads('''[
            {"inputs":[{"internalType":"address","name":"target","type":"address"}],"name":"route","outputs":[],"stateMutability":"nonpayable","type":"function"}
        ]''')
    }
}

CHAINLINK_CROSSCHAIN_RPC = os.getenv("CHAINLINK_CROSSCHAIN_RPC")

class CrossChainAnalyzer:
    def __init__(self):
        self.supported_chains = {
            'avalanche_c': {
                'name': 'Avalanche C-Chain',
                'bridge_contract': os.getenv('AVAX_BRIDGE_CONTRACT'),
                'router_contract': os.getenv('AVAX_ROUTER_CONTRACT')
            },
            'avalanche_p': {
                'name': 'Avalanche P-Chain',
                'bridge_contract': os.getenv('AVAX_P_BRIDGE_CONTRACT'),
                'router_contract': os.getenv('AVAX_P_ROUTER_CONTRACT')
            },
            'avalanche_x': {
                'name': 'Avalanche X-Chain',
                'bridge_contract': os.getenv('AVAX_X_BRIDGE_CONTRACT'),
                'router_contract': os.getenv('AVAX_X_ROUTER_CONTRACT')
            }
        }

    def analyze_cross_chain_risk(self, address: str, source_chain: str, target_chains: List[str]) -> Dict:
        """
        Analyze cross-chain communication risks for a contract.
        """
        risks = []
        w3 = get_web3_connection(source_chain)
        
        # Check if contract interacts with bridge contracts
        bridge_interactions = self._check_bridge_interactions(w3, address, source_chain)
        if bridge_interactions:
            risks.extend(bridge_interactions)

        # Check for cross-chain message passing
        message_passing = self._check_message_passing(w3, address)
        if message_passing:
            risks.append(message_passing)

        # Check for cross-chain asset transfers
        asset_transfers = self._check_asset_transfers(w3, address)
        if asset_transfers:
            risks.extend(asset_transfers)

        # Check for security-related patterns
        security_issues = self._check_security_patterns(w3, address)
        if security_issues:
            risks.extend(security_issues)

        return {
            "address": address,
            "source_chain": source_chain,
            "target_chains": target_chains,
            "risks": risks,
            "risk_score": self._calculate_cross_chain_risk_score(risks),
            "analysis_timestamp": datetime.now().isoformat()
        }

    def _check_bridge_interactions(self, w3: Web3, address: str, chain: str) -> List[Dict]:
        """Check if contract interacts with bridge contracts."""
        interactions = []
        contract = w3.eth.contract(address=address, abi=BRIDGE_ABIS['avalanche']['bridge'])
        
        # Check for bridge function calls
        try:
            if contract.functions.getBridgeStatus().call():
                interactions.append({
                    "type": "bridge_status_check",
                    "contract": address
                })
        except Exception:
            pass

        # Add new bridge interaction checks
        try:
            # Check for bridge deposit events
            deposit_filter = contract.events.BridgeDeposit.create_filter(fromBlock='latest')
            if deposit_filter.get_all_entries():
                interactions.append({
                    "type": "bridge_deposit",
                    "severity": "High",
                    "details": "Contract has bridge deposit events"
                })
        except Exception:
            pass

        # Check for bridge withdrawal patterns
        try:
            withdrawal_filter = contract.events.BridgeWithdrawal.create_filter(fromBlock='latest')
            if withdrawal_filter.get_all_entries():
                interactions.append({
                    "type": "bridge_withdrawal",
                    "severity": "High",
                    "details": "Contract has bridge withdrawal events"
                })
        except Exception:
            pass

        return interactions

    def _check_message_passing(self, w3: Web3, address: str) -> Optional[Dict]:
        """Check for cross-chain message passing implementation."""
        message_patterns = []
        bytecode = w3.eth.get_code(address).hex()
        
        # Enhanced message passing detection
        patterns = {
            'crosschain': 'Cross-chain message pattern',
            'bridge': 'Bridge message pattern',
            'relay': 'Relay message pattern',
            'verify': 'Message verification pattern',
            'signature': 'Message signature pattern'
        }
        
        for pattern, description in patterns.items():
            if pattern in bytecode.lower():
                message_patterns.append({
                    "type": pattern,
                    "description": description,
                    "severity": "Medium"
                })
        
        if message_patterns:
            return {
                "type": "message_passing",
                "patterns": message_patterns,
                "severity": "Medium"
            }
        return None

    def _check_asset_transfers(self, w3: Web3, address: str) -> List[Dict]:
        """Check for cross-chain asset transfer patterns."""
        transfers = []
        bytecode = w3.eth.get_code(address).hex()
        
        # Enhanced transfer pattern detection
        transfer_patterns = {
            'transfer': 'Basic transfer',
            'bridge': 'Bridge transfer',
            'crosschain': 'Cross-chain transfer',
            'lock': 'Asset locking',
            'unlock': 'Asset unlocking',
            'mint': 'Cross-chain minting',
            'burn': 'Cross-chain burning'
        }
        
        for pattern, description in transfer_patterns.items():
            if pattern in bytecode.lower():
                transfers.append({
                    "type": f"{pattern}_transfer",
                    "description": description,
                    "severity": "High" if pattern in ['bridge', 'crosschain'] else "Medium"
                })
        
        return transfers

    def _check_security_patterns(self, w3: Web3, address: str) -> List[Dict]:
        """Check for security-related patterns in cross-chain contracts."""
        security_issues = []
        bytecode = w3.eth.get_code(address).hex()
        
        # Check for common security patterns
        security_patterns = {
            'reentrancy': 'Potential reentrancy vulnerability',
            'overflow': 'Potential integer overflow',
            'unchecked': 'Unchecked external calls',
            'selfdestruct': 'Self-destruct functionality',
            'delegatecall': 'Delegate call usage'
        }
        
        for pattern, description in security_patterns.items():
            if pattern in bytecode.lower():
                security_issues.append({
                    "type": pattern,
                    "description": description,
                    "severity": "High"
                })
        
        return security_issues

    def _calculate_cross_chain_risk_score(self, risks: List[Dict]) -> int:
        """Calculate risk score based on cross-chain risks."""
        base_score = 50
        for risk in risks:
            if risk["severity"] == "High":
                base_score += 25
            elif risk["severity"] == "Medium":
                base_score += 15
            elif risk["severity"] == "Low":
                base_score += 5
        return min(base_score, 100)

    def get_chain_communication_map(self, address: str) -> Dict:
        """Get a map of chain communication patterns for a contract."""
        communication_map = {}
        for chain in self.supported_chains:
            w3 = get_web3_connection(chain)
            try:
                # Check for contract existence on each chain
                code = w3.eth.get_code(address)
                if code:
                    communication_map[chain] = {
                        "exists": True,
                        "interactions": self._check_bridge_interactions(w3, address, chain)
                    }
                else:
                    communication_map[chain] = {
                        "exists": False,
                        "interactions": []
                    }
            except Exception:
                communication_map[chain] = {
                    "exists": False,
                    "interactions": []
                }
        return communication_map

def analyze_cross_chain_risk(address, source_chain, target_chains):
    """
    Analyze cross-chain risk for a contract on Avalanche C-Chain (AVAX) as the source chain.
    Cross-chain communication is performed via Chainlink to other L1s (Ethereum, Polygon, etc.).
    """
    # Example: Use Chainlink CCIP or node API for cross-chain status
    # This is a placeholder; replace with actual Chainlink API usage
    if not CHAINLINK_CROSSCHAIN_RPC:
        return {"error": "Chainlink CCIP endpoint not configured"}
    try:
        resp = requests.get(f"{CHAINLINK_CROSSCHAIN_RPC}/cross-chain-status?address={address}")
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

# Placeholder for multi-validator set status (if needed for frontend)
def get_validator_set_status():
    """
    Get the current multi-validator set status for cross-chain signature verification.
    """
    # This would call a contract or off-chain service to get validator set info
    return {
        "validators": [],
        "threshold": 0
    } 