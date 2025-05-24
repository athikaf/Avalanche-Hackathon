import React from 'react';

interface RiskScoreProps {
  score: number;
}

export function RiskScore({ score }: RiskScoreProps) {
  const getScoreColor = (score: number) => {
    if (score >= 80) return 'text-red-600';
    if (score >= 60) return 'text-orange-600';
    if (score >= 40) return 'text-yellow-600';
    return 'text-green-600';
  };

  return (
    <div className="flex items-center space-x-4">
      <div className="relative">
        <svg className="w-24 h-24">
          <circle
            className="text-gray-200"
            strokeWidth="8"
            stroke="currentColor"
            fill="transparent"
            r="40"
            cx="48"
            cy="48"
          />
          <circle
            className={getScoreColor(score)}
            strokeWidth="8"
            strokeDasharray={251.2}
            strokeDashoffset={251.2 - (251.2 * score) / 100}
            strokeLinecap="round"
            stroke="currentColor"
            fill="transparent"
            r="40"
            cx="48"
            cy="48"
          />
        </svg>
        <div className="absolute inset-0 flex items-center justify-center">
          <span className={`text-2xl font-bold ${getScoreColor(score)}`}>
            {score}
          </span>
        </div>
      </div>
      <div>
        <h4 className="text-sm font-medium text-gray-900">Risk Score</h4>
        <p className="text-sm text-gray-500">
          {score >= 80
            ? 'High Risk'
            : score >= 60
            ? 'Medium-High Risk'
            : score >= 40
            ? 'Medium Risk'
            : 'Low Risk'}
        </p>
      </div>
    </div>
  );
} 