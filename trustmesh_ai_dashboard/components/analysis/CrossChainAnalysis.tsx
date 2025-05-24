import React from 'react';
import { Card } from '@/components/ui/Card';
import { RiskScore } from '@/components/ui/RiskScore';
import { ChainMap } from '@/components/ui/ChainMap';
import { RiskList } from '@/components/ui/RiskList';

interface CrossChainAnalysisProps {
  data: {
    address: string;
    source_chain: string;
    target_chains: string[];
    risks: Array<{
      type: string;
      severity: string;
      description?: string;
      details?: string;
    }>;
    risk_score: number;
    analysis_timestamp: string;
  };
}

export function CrossChainAnalysis({ data }: CrossChainAnalysisProps) {
  return (
    <div className="space-y-6">
      <Card>
        <div className="p-6">
          <h2 className="text-2xl font-bold text-gray-900">Cross-Chain Analysis</h2>
          <div className="mt-4 grid grid-cols-1 gap-6 sm:grid-cols-2">
            <div>
              <h3 className="text-lg font-medium text-gray-900">Contract Details</h3>
              <dl className="mt-2 space-y-2">
                <div>
                  <dt className="text-sm font-medium text-gray-500">Address</dt>
                  <dd className="text-sm text-gray-900">{data.address}</dd>
                </div>
                <div>
                  <dt className="text-sm font-medium text-gray-500">Source Chain</dt>
                  <dd className="text-sm text-gray-900">{data.source_chain}</dd>
                </div>
                <div>
                  <dt className="text-sm font-medium text-gray-500">Target Chains</dt>
                  <dd className="text-sm text-gray-900">{data.target_chains.join(', ')}</dd>
                </div>
                <div>
                  <dt className="text-sm font-medium text-gray-500">Analysis Time</dt>
                  <dd className="text-sm text-gray-900">
                    {new Date(data.analysis_timestamp).toLocaleString()}
                  </dd>
                </div>
              </dl>
            </div>
            <div>
              <h3 className="text-lg font-medium text-gray-900">Risk Assessment</h3>
              <div className="mt-2">
                <RiskScore score={data.risk_score} />
              </div>
            </div>
          </div>
        </div>
      </Card>

      <Card>
        <div className="p-6">
          <h3 className="text-lg font-medium text-gray-900">Chain Communication Map</h3>
          <div className="mt-4">
            <ChainMap
              sourceChain={data.source_chain}
              targetChains={data.target_chains}
              risks={data.risks}
            />
          </div>
        </div>
      </Card>

      <Card>
        <div className="p-6">
          <h3 className="text-lg font-medium text-gray-900">Risk Analysis</h3>
          <div className="mt-4">
            <RiskList risks={data.risks} />
          </div>
        </div>
      </Card>
    </div>
  );
} 