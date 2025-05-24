import React from 'react';
import { CrossChainAnalysis } from '@/components/analysis/CrossChainAnalysis';
import { Card } from '@/components/ui/Card';

export default function CrossChainAnalysisPage() {
  // This would typically fetch data from the API
  const mockData = {
    address: '0x1234...5678',
    source_chain: 'avalanche_c',
    target_chains: ['avalanche_p', 'avalanche_x'],
    risks: [
      {
        type: 'Bridge Interaction',
        severity: 'High',
        description: 'Contract interacts with bridge contracts',
        details: 'Multiple bridge deposit and withdrawal events detected'
      },
      {
        type: 'Message Passing',
        severity: 'Medium',
        description: 'Cross-chain message passing implementation detected',
        details: 'Uses relay pattern for message verification'
      },
      {
        type: 'Asset Transfer',
        severity: 'High',
        description: 'Cross-chain asset transfer functionality',
        details: 'Implements lock/unlock mechanism for cross-chain transfers'
      }
    ],
    risk_score: 75,
    analysis_timestamp: new Date().toISOString()
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900">Cross-Chain Analysis</h1>
        <p className="mt-2 text-gray-600">
          Analyze cross-chain communication patterns and risks for smart contracts
        </p>
      </div>

      <div className="grid grid-cols-1 gap-6">
        <Card>
          <div className="p-6">
            <h2 className="text-xl font-semibold text-gray-900 mb-4">
              Analysis Results
            </h2>
            <CrossChainAnalysis data={mockData} />
          </div>
        </Card>
      </div>
    </div>
  );
} 