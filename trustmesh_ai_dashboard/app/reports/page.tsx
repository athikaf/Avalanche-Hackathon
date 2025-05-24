import { useEffect, useState } from 'react'
import { Card } from '@/components/ui/Card'

interface Report {
  report_id: string
  content: string
  generated_at: string
}

export default function ReportsPage() {
  const [reports, setReports] = useState<Report[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Placeholder: In a real app, fetch from backend or database
    setLoading(false)
    setReports([])
  }, [])

  return (
    <div className="space-y-8">
      <div>
        <h2 className="text-2xl font-bold text-gray-900">Reports</h2>
        <p className="mt-2 text-gray-600">
          View and manage generated reports for contracts and protocols.
        </p>
      </div>
      {loading ? (
        <div>Loading reports...</div>
      ) : reports.length === 0 ? (
        <div>No reports generated yet.</div>
      ) : (
        <div className="space-y-4">
          {reports.map((report) => (
            <Card key={report.report_id}>
              <div className="flex flex-col space-y-2">
                <div className="flex justify-between">
                  <span className="font-mono text-xs text-gray-500">{report.report_id}</span>
                  <span className="text-xs text-gray-400">{new Date(report.generated_at).toLocaleString()}</span>
                </div>
                <div className="text-sm text-gray-700 whitespace-pre-line">
                  {report.content}
                </div>
              </div>
            </Card>
          ))}
        </div>
      )}
    </div>
  )
} 