def analyze_contract(address: str) -> dict:
    # ... existing code ...
    # Check for access control issues
    if _check_access_control(bytecode, source):
        findings.append({
            "title": "Access Control Issues",
            "details": "Contract has public/unprotected functions or missing access modifiers.",
            "severity": "High",
            "severity_score_impact": 25
        })
    # Check for upgradeable/proxy pattern
    if _check_upgradeable_pattern(bytecode, source):
        findings.append({
            "title": "Upgradeable/Proxy Pattern Detected",
            "details": "Contract uses a proxy/upgradeable pattern. Review upgrade logic for security.",
            "severity": "Medium",
            "severity_score_impact": 15
        })
    # Check for economic security issues
    if _check_economic_security(bytecode, source):
        findings.append({
            "title": "Economic Security Issues",
            "details": "Contract has fee logic, inflation, or economic risks.",
            "severity": "Medium",
            "severity_score_impact": 20
        })
    # Check for cross-contract interaction
    if _check_cross_contract_interaction(bytecode):
        findings.append({
            "title": "Cross-Contract Interaction",
            "details": "Contract makes external calls to other contracts. Review for security.",
            "severity": "Medium",
            "severity_score_impact": 15
        })
    # ... existing code ...

def _check_access_control(bytecode: str, source: str = None) -> bool:
    # Naive check: look for 'public' functions in source or lack of 'onlyOwner' in bytecode
    if source and 'public' in source and 'onlyOwner' not in source:
        return True
    if 'onlyOwner' not in bytecode:
        return True
    return False

def _check_upgradeable_pattern(bytecode: str, source: str = None) -> bool:
    # Look for 'delegatecall' or 'proxy' in bytecode/source
    if 'delegatecall' in bytecode.lower() or (source and 'proxy' in source.lower()):
        return True
    return False

def _check_economic_security(bytecode: str, source: str = None) -> bool:
    # Look for 'fee', 'mint', 'burn', 'inflation' in source/bytecode
    keywords = ['fee', 'mint', 'burn', 'inflation']
    if source and any(k in source.lower() for k in keywords):
        return True
    if any(k in bytecode.lower() for k in keywords):
        return True
    return False

def _check_cross_contract_interaction(bytecode: str) -> bool:
    # Look for CALL, DELEGATECALL, CALLCODE, STATICCALL opcodes
    opcodes = ['f1', 'f4', 'fa', 'fd']
    return any(op in bytecode.lower() for op in opcodes)
# ... existing code ... 