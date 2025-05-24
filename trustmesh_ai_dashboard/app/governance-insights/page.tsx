import { useState } from 'react'
import { Button } from '@/components/ui/Button'

interface ProposalAnalysis {
  summary: string
  risk_analysis: {
    overall_risk: string
    details: string
  }
  recommendations: string[]
}

export default function GovernanceInsightsPage() {
  const [proposalId, setProposalId] = useState('')
  const [daoAddress, setDaoAddress] = useState('')
  const [result, setResult] = useState<ProposalAnalysis | null>(null)
  const [loading, setLoading] = useState(false)

  const handleAnalyze = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setResult(null)
    try {
      const res = await fetch('/api/v1/governance/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ proposal_id: proposalId, dao_address: daoAddress }),
      })
      const data = await res.json()
      setResult(data)
    } catch (err) {
      setResult(null)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="space-y-8">
      <div>
        <h2 className="text-2xl font-bold text-gray-900">Governance Insights</h2>
        <p className="mt-2 text-gray-600">
          Get AI-powered analysis of DAO proposals and governance decisions.
        </p>
      </div>
      <form onSubmit={handleAnalyze} className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-gray-700">DAO Address</label>
          <input
            type="text"
            className="block w-full rounded-md border-gray-300 shadow-sm focus:border-primary-500 focus:ring-primary-500 sm:text-sm"
            value={daoAddress}
            onChange={e => setDaoAddress(e.target.value)}
            placeholder="0x..."
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">Proposal ID</label>
          <input
            type="text"
            className="block w-full rounded-md border-gray-300 shadow-sm focus:border-primary-500 focus:ring-primary-500 sm:text-sm"
            value={proposalId}
            onChange={e => setProposalId(e.target.value)}
            placeholder="Proposal ID"
            required
          />
        </div>
        <Button type="submit" isLoading={loading} disabled={loading || !daoAddress || !proposalId}>
          Analyze Proposal
        </Button>
      </form>
      {result && (
        <div className="space-y-4">
          <div className="bg-white rounded-lg shadow p-4">
            <h3 className="font-semibold text-lg mb-2">Summary</h3>
            <p>{result.summary}</p>
          </div>
          <div className="bg-white rounded-lg shadow p-4">
            <h3 className="font-semibold text-lg mb-2">Risk Analysis</h3>
            <p><span className="font-bold">Overall Risk:</span> {result.risk_analysis.overall_risk}</p>
            <p>{result.risk_analysis.details}</p>
          </div>
          <div className="bg-white rounded-lg shadow p-4">
            <h3 className="font-semibold text-lg mb-2">Recommendations</h3>
            <ul className="list-disc pl-5">
              {result.recommendations.map((rec, i) => (
                <li key={i}>{rec}</li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </div>
  )
} 