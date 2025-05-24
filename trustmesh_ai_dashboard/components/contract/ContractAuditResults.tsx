import { Card } from '@/components/ui/Card'

interface Finding {
  title: string
  details: string
  severity: 'High' | 'Medium' | 'Low'
  severity_score_impact: number
}

interface AuditResults {
  risk_score: number
  findings: Finding[]
}

interface ContractAuditResultsProps {
  results: AuditResults
}

export function ContractAuditResults({ results }: ContractAuditResultsProps) {
  const getSeverityColor = (severity: string) => {
    switch (severity) {
      case 'High':
        return 'text-red-600'
      case 'Medium':
        return 'text-yellow-600'
      case 'Low':
        return 'text-green-600'
      default:
        return 'text-gray-600'
    }
  }

  return (
    <div className="space-y-6">
      <Card>
        <div className="flex items-center justify-between">
          <h3 className="text-lg font-medium text-gray-900">Risk Score</h3>
          <div className="text-2xl font-bold text-primary-600">
            {results.risk_score}/100
          </div>
        </div>
      </Card>

      <div className="space-y-4">
        <h3 className="text-lg font-medium text-gray-900">Findings</h3>
        {results.findings.map((finding, index) => (
          <Card key={index}>
            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <h4 className="text-base font-medium text-gray-900">
                  {finding.title}
                </h4>
                <span className={`text-sm font-medium ${getSeverityColor(finding.severity)}`}>
                  {finding.severity}
                </span>
              </div>
              <p className="text-sm text-gray-500">{finding.details}</p>
              <div className="text-xs text-gray-400">
                Impact Score: {finding.severity_score_impact}
              </div>
            </div>
          </Card>
        ))}
      </div>
    </div>
  )
} 