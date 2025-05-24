from typing import Dict
import openai
from datetime import datetime
import os
from dotenv import load_dotenv
from utils.blockchain import get_contract_source

load_dotenv()

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_report(contract_address: str, report_type: str) -> Dict:
    """
    Generate an LLM-based report for a contract.
    
    Args:
        contract_address: The contract address to analyze
        report_type: Type of report ("security", "governance", "activity")
        
    Returns:
        Dict: Generated report with ID, content, and timestamp
    """
    # Get contract source if available
    source_code = get_contract_source(contract_address)
    
    # Prepare prompt based on report type
    if report_type == "security":
        prompt = f"""
        Analyze the following smart contract for security vulnerabilities:
        {source_code if source_code else f"Contract at {contract_address}"}
        
        Focus on:
        1. Common vulnerabilities (reentrancy, overflow, etc.)
        2. Access control issues
        3. Gas optimization opportunities
        4. Best practices compliance
        """
    elif report_type == "governance":
        prompt = f"""
        Analyze the following smart contract for governance aspects:
        {source_code if source_code else f"Contract at {contract_address}"}
        
        Focus on:
        1. Voting mechanisms
        2. Proposal handling
        3. Access control
        4. Upgradeability
        """
    else:  # activity
        prompt = f"""
        Analyze the following contract's on-chain activity:
        {source_code if source_code else f"Contract at {contract_address}"}
        
        Focus on:
        1. Transaction patterns
        2. User interactions
        3. Value flow
        4. Notable events
        """
    
    # Generate report using OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a blockchain security expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=2000
    )
    
    report_id = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    return {
        "report_id": report_id,
        "content": response.choices[0].message.content,
        "generated_at": datetime.now().isoformat()
    } 