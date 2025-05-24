from typing import Dict, List

def compute_risk_score(vulnerabilities: Dict[str, int]) -> int:
    """
    Compute total risk score from vulnerability weights.
    
    Args:
        vulnerabilities: Dict mapping vulnerability names to their weights
        
    Returns:
        int: Total risk score (0-100)
    """
    if not vulnerabilities:
        return 0
        
    total_weight = sum(vulnerabilities.values())
    # Normalize to 0-100 scale
    normalized_score = min(100, total_weight)
    
    return normalized_score

def get_severity_level(score: int) -> str:
    """
    Convert numerical score to severity level.
    
    Args:
        score: Risk score (0-100)
        
    Returns:
        str: "Low", "Medium", or "High"
    """
    if score < 30:
        return "Low"
    elif score < 70:
        return "Medium"
    else:
        return "High" 