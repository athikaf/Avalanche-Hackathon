from typing import Dict, List
from datetime import datetime
from utils.cross_chain import CrossChainAnalyzer

class CrossChainReportGenerator:
    def __init__(self):
        self.analyzer = CrossChainAnalyzer()

    def generate_report(self, address: str, source_chain: str, target_chains: List[str]) -> Dict:
        """
        Generate a comprehensive report for cross-chain contract analysis.
        """
        # Get analysis results
        analysis = self.analyzer.analyze_cross_chain_risk(
            address=address,
            source_chain=source_chain,
            target_chains=target_chains
        )

        # Get chain communication map
        chain_map = self.analyzer.get_chain_communication_map(address)

        # Generate report sections
        report = {
            "report_id": f"ccr_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "generated_at": datetime.now().isoformat(),
            "contract_address": address,
            "source_chain": source_chain,
            "target_chains": target_chains,
            "risk_score": analysis["risk_score"],
            "risk_level": self._get_risk_level(analysis["risk_score"]),
            "sections": {
                "executive_summary": self._generate_executive_summary(analysis),
                "risk_analysis": self._generate_risk_analysis(analysis["risks"]),
                "chain_communication": self._generate_chain_communication(chain_map),
                "recommendations": self._generate_recommendations(analysis["risks"])
            }
        }

        return report

    def _get_risk_level(self, score: int) -> str:
        """Convert risk score to risk level."""
        if score >= 80:
            return "Critical"
        elif score >= 60:
            return "High"
        elif score >= 40:
            return "Medium"
        else:
            return "Low"

    def _generate_executive_summary(self, analysis: Dict) -> Dict:
        """Generate executive summary section."""
        return {
            "overview": f"Cross-chain analysis of contract {analysis['address']}",
            "risk_score": analysis["risk_score"],
            "key_findings": [
                {
                    "type": risk["type"],
                    "severity": risk["severity"],
                    "description": risk.get("description", "")
                }
                for risk in analysis["risks"]
                if risk["severity"] == "High"
            ],
            "timestamp": analysis["analysis_timestamp"]
        }

    def _generate_risk_analysis(self, risks: List[Dict]) -> Dict:
        """Generate detailed risk analysis section."""
        return {
            "risk_categories": {
                "high": [r for r in risks if r["severity"] == "High"],
                "medium": [r for r in risks if r["severity"] == "Medium"],
                "low": [r for r in risks if r["severity"] == "Low"]
            },
            "risk_distribution": {
                "high": len([r for r in risks if r["severity"] == "High"]),
                "medium": len([r for r in risks if r["severity"] == "Medium"]),
                "low": len([r for r in risks if r["severity"] == "Low"])
            }
        }

    def _generate_chain_communication(self, chain_map: Dict) -> Dict:
        """Generate chain communication analysis section."""
        return {
            "chain_presence": {
                chain: {
                    "exists": data["exists"],
                    "interaction_count": len(data["interactions"])
                }
                for chain, data in chain_map.items()
            },
            "communication_patterns": {
                chain: [
                    {
                        "type": interaction["type"],
                        "severity": interaction.get("severity", "Unknown")
                    }
                    for interaction in data["interactions"]
                ]
                for chain, data in chain_map.items()
                if data["exists"]
            }
        }

    def _generate_recommendations(self, risks: List[Dict]) -> List[Dict]:
        """Generate recommendations based on identified risks."""
        recommendations = []
        
        for risk in risks:
            if risk["severity"] == "High":
                recommendations.append({
                    "risk_type": risk["type"],
                    "priority": "High",
                    "recommendation": self._get_recommendation_for_risk(risk)
                })
            elif risk["severity"] == "Medium":
                recommendations.append({
                    "risk_type": risk["type"],
                    "priority": "Medium",
                    "recommendation": self._get_recommendation_for_risk(risk)
                })

        return recommendations

    def _get_recommendation_for_risk(self, risk: Dict) -> str:
        """Get specific recommendation for a risk type."""
        recommendations = {
            "bridge_interaction": "Implement additional security checks for bridge interactions and consider using a time-lock mechanism for large transfers.",
            "message_passing": "Add message verification and replay protection mechanisms for cross-chain messages.",
            "asset_transfer": "Implement a gradual release mechanism for cross-chain asset transfers and add emergency pause functionality.",
            "reentrancy": "Implement reentrancy guards and follow the checks-effects-interactions pattern.",
            "overflow": "Use SafeMath or similar libraries for arithmetic operations.",
            "unchecked": "Add proper error handling and validation for external calls.",
            "selfdestruct": "Consider implementing a multi-signature requirement for self-destruct operations.",
            "delegatecall": "Limit delegatecall usage and implement proper access controls."
        }
        
        return recommendations.get(risk["type"], "Review and implement appropriate security measures based on the specific risk.") 