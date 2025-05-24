import React from 'react';

interface ChainMapProps {
  sourceChain: string;
  targetChains: string[];
  risks: Array<{
    type: string;
    severity: string;
    description?: string;
  }>;
}

export function ChainMap({ sourceChain, targetChains, risks }: ChainMapProps) {
  const getRiskColor = (severity: string) => {
    switch (severity.toLowerCase()) {
      case 'high':
        return 'text-red-600';
      case 'medium':
        return 'text-yellow-600';
      case 'low':
        return 'text-green-600';
      default:
        return 'text-gray-600';
    }
  };

  return (
    <div className="relative">
      <div className="flex items-center justify-center space-x-8">
        {/* Source Chain */}
        <div className="flex flex-col items-center">
          <div className="w-16 h-16 rounded-full bg-blue-100 flex items-center justify-center">
            <span className="text-blue-600 font-medium">{sourceChain}</span>
          </div>
          <div className="mt-2 text-sm text-gray-500">Source</div>
        </div>

        {/* Arrows */}
        <div className="flex-1 flex items-center justify-center">
          {targetChains.map((chain, index) => (
            <div key={chain} className="relative">
              <div className="w-24 h-0.5 bg-gray-300" />
              <div className="absolute top-1/2 right-0 transform translate-x-1/2 -translate-y-1/2">
                <div className="w-0 h-0 border-t-4 border-t-transparent border-b-4 border-b-transparent border-l-4 border-l-gray-300" />
              </div>
            </div>
          ))}
        </div>

        {/* Target Chains */}
        <div className="flex space-x-4">
          {targetChains.map((chain) => (
            <div key={chain} className="flex flex-col items-center">
              <div className="w-16 h-16 rounded-full bg-green-100 flex items-center justify-center">
                <span className="text-green-600 font-medium">{chain}</span>
              </div>
              <div className="mt-2 text-sm text-gray-500">Target</div>
            </div>
          ))}
        </div>
      </div>

      {/* Risk Indicators */}
      <div className="mt-8">
        <h4 className="text-sm font-medium text-gray-900 mb-2">Risk Indicators</h4>
        <div className="grid grid-cols-2 gap-4">
          {risks.map((risk, index) => (
            <div
              key={index}
              className={`p-3 rounded-lg border ${getRiskColor(risk.severity)}`}
            >
              <div className="font-medium">{risk.type}</div>
              {risk.description && (
                <div className="text-sm mt-1">{risk.description}</div>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
} 