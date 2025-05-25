"""
TrustMesh AI Dashboard Backend

This backend is built for Avalanche C-Chain (AVAX) as the primary network.
All contract analysis, monitoring, and reporting are performed on AVAX by default.
Cross-chain communication and analysis (to Ethereum, Polygon, etc.) are performed via Chainlink CCIP or Chainlink nodes.
"""
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional
from audit.risk_engine import analyze_contract
from monitor.whale_monitor import get_whale_alerts
from reports.report_generator import generate_report
from governance.proposal_agent import analyze_proposal
from audit.advanced_analysis import (
    get_transaction_history,
    get_token_flows,
    analyze_gas_usage,
    get_interaction_patterns,
)
from utils.cross_chain import CrossChainAnalyzer
from reports.cross_chain_report import CrossChainReportGenerator
from datetime import datetime, timedelta

app = FastAPI(title="TrustMesh AI Dashboard API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response Models
class ContractAuditRequest(BaseModel):
    address: str

class ContractAuditResponse(BaseModel):
    risk_score: int
    findings: List[Dict]

class WhaleAlertResponse(BaseModel):
    alerts: List[Dict]

class ReportRequest(BaseModel):
    contract_address: str
    report_type: str  # e.g., "security", "governance", "activity"

class ReportResponse(BaseModel):
    report_id: str
    content: str
    generated_at: str

class ProposalRequest(BaseModel):
    proposal_id: str
    dao_address: str

class ProposalResponse(BaseModel):
    summary: str
    risk_analysis: Dict
    recommendations: List[str]

class AddressRequest(BaseModel):
    address: str

class ChainRequest(BaseModel):
    address: str
    chain: str = "avalanche"  # Default to Avalanche

class CrossChainRequest(BaseModel):
    address: str
    source_chain: str
    target_chains: List[str]

# API Routes
@app.post("/api/v1/audit/contract", response_model=ContractAuditResponse)
async def audit_contract(request: ChainRequest):
    """
    Analyze a smart contract for security risks and vulnerabilities.
    """
    try:
        result = analyze_contract(request.address, request.chain)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/monitor/whale-alerts", response_model=WhaleAlertResponse)
async def get_alerts():
    """
    Get recent whale activity alerts.
    """
    try:
        alerts = get_whale_alerts()
        return {"alerts": alerts}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/report/generate", response_model=ReportResponse)
async def generate_llm_report(request: ReportRequest):
    """
    Generate an LLM-based report for a contract.
    """
    try:
        report = generate_report(
            contract_address=request.contract_address,
            report_type=request.report_type
        )
        return report
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/governance/analyze", response_model=ProposalResponse)
async def analyze_dao_proposal(request: ProposalRequest):
    """
    Analyze a DAO proposal using LLM.
    """
    try:
        analysis = analyze_proposal(
            proposal_id=request.proposal_id,
            dao_address=request.dao_address
        )
        return analysis
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Optional: AI Voting Endpoint
@app.post("/api/v1/governance/vote")
async def submit_ai_vote(proposal_id: str, dao_address: str):
    """
    Submit an AI-generated vote for a DAO proposal.
    Note: This is an optional feature and should be implemented with caution.
    """
    raise HTTPException(
        status_code=501,
        detail="AI voting not implemented yet"
    )

@app.post("/api/v1/analysis/transactions")
async def transaction_history(request: ChainRequest, max_blocks: int = Query(500, ge=1, le=5000)):
    """Get transaction history for an address/contract."""
    try:
        txs = get_transaction_history(request.address, request.chain, max_blocks=max_blocks)
        return {"transactions": txs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/analysis/token-flows")
async def token_flows(request: ChainRequest, max_blocks: int = Query(500, ge=1, le=5000)):
    """Get token flow (ERC20 transfers) for an address/contract."""
    try:
        flows = get_token_flows(request.address, request.chain, max_blocks=max_blocks)
        return {"token_flows": flows}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/analysis/gas-usage")
async def gas_usage(request: ChainRequest):
    """Analyze gas usage for an address/contract."""
    try:
        result = analyze_gas_usage(request.address, request.chain)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/analysis/interactions")
async def interaction_patterns(request: ChainRequest, max_blocks: int = Query(500, ge=1, le=5000)):
    """Get contract interaction patterns (who interacts with this contract)."""
    try:
        patterns = get_interaction_patterns(request.address, request.chain, max_blocks=max_blocks)
        return {"interaction_patterns": patterns}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/analysis/cross-chain")
async def analyze_cross_chain(request: CrossChainRequest):
    """Analyze cross-chain communication risks for a contract."""
    try:
        analyzer = CrossChainAnalyzer()
        result = analyzer.analyze_cross_chain_risk(
            request.address,
            request.source_chain,
            request.target_chains
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/analysis/chain-map/{address}")
async def get_chain_communication_map(address: str):
    """Get a map of chain communication patterns for a contract."""
    try:
        analyzer = CrossChainAnalyzer()
        result = analyzer.get_chain_communication_map(address)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/reports/cross-chain")
async def generate_cross_chain_report(request: CrossChainRequest):
    """Generate a comprehensive cross-chain analysis report."""
    try:
        generator = CrossChainReportGenerator()
        report = generator.generate_report(
            address=request.address,
            source_chain=request.source_chain,
            target_chains=request.target_chains
        )
        return report
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/api/v1/analysis/aggregate')
def get_aggregate_analysis():
    # Example: Replace with real DB/analysis aggregation
    return {
        "contract_types": [
            {"type": "ERC20", "count": 12},
            {"type": "Bridge", "count": 5},
            {"type": "Governance", "count": 3},
            {"type": "Other", "count": 2}
        ],
        "risk_categories": [
            {"category": "Bridge Risks", "count": 8},
            {"category": "Message Risks", "count": 6},
            {"category": "Security Risks", "count": 10},
            {"category": "Value Risks", "count": 4}
        ],
        "disclaimer": "Aggregate data is based on analyzed contracts and may not represent the entire ecosystem."
    }

@app.get('/api/v1/analysis/timeline')
def get_risk_timeline():
    # Example: Replace with real DB/timeseries aggregation
    today = datetime.utcnow().date()
    data = []
    for i in range(7):
        day = today - timedelta(days=6-i)
        data.append({
            "date": day.isoformat(),
            "riskScore": 60 + i*2,  # Example data
            "findings": 3 + (i % 2)
        })
    return {
        "timeline": data,
        "disclaimer": "Timeline data is based on available analysis and may not capture all events."
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 