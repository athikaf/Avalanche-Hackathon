from typing import Dict, List
import openai
import os
from dotenv import load_dotenv
from utils.blockchain import get_web3_connection

load_dotenv()

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")
#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

def analyze_proposal(proposal_id: str, dao_address: str) -> Dict:
    """
    Analyze a DAO proposal using LLM.
    
    Args:
        proposal_id: The proposal ID to analyze
        dao_address: The DAO contract address
        
    Returns:
        Dict: Analysis results including summary, risk analysis, and recommendations
    """
    w3 = get_web3_connection()
    
    # TODO: Implement actual proposal data fetching from the DAO contract
    # This is a placeholder that would need to be implemented based on the specific DAO
    proposal_data = {
        "title": "Sample Proposal",
        "description": "This is a placeholder for the actual proposal data",
        "actions": ["Action 1", "Action 2"],
        "voting_period": "7 days",
        "quorum": "1000 tokens"
    }
    
    # Prepare prompt for LLM analysis
    prompt = f"""
    Analyze the following DAO proposal:
    
    Title: {proposal_data['title']}
    Description: {proposal_data['description']}
    Actions: {', '.join(proposal_data['actions'])}
    Voting Period: {proposal_data['voting_period']}
    Quorum: {proposal_data['quorum']}
    
    Please provide:
    1. A concise summary
    2. Risk analysis
    3. Specific recommendations
    """
    
    # Generate analysis using OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a DAO governance expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1500
    )
    
    # Parse the response into structured format
    analysis = response.choices[0].message.content
    
    # Split analysis into sections (this is a simple implementation)
    sections = analysis.split('\n\n')
    summary = sections[0] if len(sections) > 0 else ""
    risk_analysis = sections[1] if len(sections) > 1 else ""
    recommendations = sections[2].split('\n') if len(sections) > 2 else []
    
    return {
        "summary": summary,
        "risk_analysis": {
            "overall_risk": "Medium",  # This would be computed based on analysis
            "details": risk_analysis
        },
        "recommendations": recommendations
    } 