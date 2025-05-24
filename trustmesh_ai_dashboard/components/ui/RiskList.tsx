import React from 'react';
import {
  ExclamationTriangleIcon,
  ExclamationCircleIcon,
  InformationCircleIcon,
} from '@heroicons/react/24/outline';

interface Risk {
  type: string;
  severity: string;
  description?: string;
  details?: string;
}

interface RiskListProps {
  risks: Risk[];
}

export function RiskList({ risks }: RiskListProps) {
  const getSeverityIcon = (severity: string) => {
    switch (severity.toLowerCase()) {
      case 'high':
        return <ExclamationTriangleIcon className="h-5 w-5 text-red-500" />;
      case 'medium':
        return <ExclamationCircleIcon className="h-5 w-5 text-yellow-500" />;
      case 'low':
        return <InformationCircleIcon className="h-5 w-5 text-green-500" />;
      default:
        return <InformationCircleIcon className="h-5 w-5 text-gray-500" />;
    }
  };

  const getSeverityColor = (severity: string) => {
    switch (severity.toLowerCase()) {
      case 'high':
        return 'bg-red-50 border-red-200';
      case 'medium':
        return 'bg-yellow-50 border-yellow-200';
      case 'low':
        return 'bg-green-50 border-green-200';
      default:
        return 'bg-gray-50 border-gray-200';
    }
  };

  return (
    <div className="space-y-4">
      {risks.map((risk, index) => (
        <div
          key={index}
          className={`p-4 rounded-lg border ${getSeverityColor(risk.severity)}`}
        >
          <div className="flex items-start">
            <div className="flex-shrink-0">{getSeverityIcon(risk.severity)}</div>
            <div className="ml-3">
              <h4 className="text-sm font-medium text-gray-900">
                {risk.type}
                <span className="ml-2 text-xs font-normal text-gray-500">
                  ({risk.severity} severity)
                </span>
              </h4>
              {risk.description && (
                <p className="mt-1 text-sm text-gray-600">{risk.description}</p>
              )}
              {risk.details && (
                <p className="mt-2 text-sm text-gray-500">{risk.details}</p>
              )}
            </div>
          </div>
        </div>
      ))}
    </div>
  );
} 