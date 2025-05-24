import { ContractAuditForm } from '@/components/contract/ContractAuditForm'
import { ContractAuditResults } from '@/components/contract/ContractAuditResults'
import { useState } from 'react'

export default function ContractAuditPage() {
  const [auditResults, setAuditResults] = useState(null)
  const [isLoading, setIsLoading] = useState(false)

  const handleAudit = async (address: string) => {
    setIsLoading(true)
    try {
      const response = await fetch('/api/v1/audit/contract', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ address }),
      })
      const data = await response.json()
      setAuditResults(data)
    } catch (error) {
      console.error('Error analyzing contract:', error)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="space-y-8">
      <div>
        <h2 className="text-2xl font-bold text-gray-900">Contract Audit</h2>
        <p className="mt-2 text-gray-600">
          Analyze smart contracts for security vulnerabilities and best practices.
        </p>
      </div>

      <ContractAuditForm onSubmit={handleAudit} isLoading={isLoading} />

      {auditResults && (
        <ContractAuditResults results={auditResults} />
      )}
    </div>
  )
} 