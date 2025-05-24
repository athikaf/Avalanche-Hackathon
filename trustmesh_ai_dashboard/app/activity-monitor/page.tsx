import { useEffect, useState } from 'react'
import { Card } from '@/components/ui/Card'

interface WhaleAlert {
  tx_hash: string
  from: string
  to: string
  value_avax: number
  timestamp: string
  block_number: number
}

export default function ActivityMonitorPage() {
  const [alerts, setAlerts] = useState<WhaleAlert[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('/api/v1/monitor/whale-alerts')
      .then((res) => res.json())
      .then((data) => setAlerts(data.alerts || []))
      .finally(() => setLoading(false))
  }, [])

  return (
    <div className="space-y-8">
      <div>
        <h2 className="text-2xl font-bold text-gray-900">Activity Monitor</h2>
        <p className="mt-2 text-gray-600">
          Track whale movements and significant on-chain activities on Avalanche C-Chain.
        </p>
      </div>
      {loading ? (
        <div>Loading whale alerts...</div>
      ) : alerts.length === 0 ? (
        <div>No whale activity detected in recent blocks.</div>
      ) : (
        <div className="space-y-4">
          {alerts.map((alert) => (
            <Card key={alert.tx_hash}>
              <div className="flex flex-col space-y-2">
                <div className="flex justify-between">
                  <span className="font-mono text-xs text-gray-500">Block #{alert.block_number}</span>
                  <span className="text-xs text-gray-400">{new Date(alert.timestamp).toLocaleString()}</span>
                </div>
                <div className="text-sm">
                  <span className="font-semibold">From:</span> {alert.from}
                </div>
                <div className="text-sm">
                  <span className="font-semibold">To:</span> {alert.to}
                </div>
                <div className="text-sm">
                  <span className="font-semibold">Value:</span> {alert.value_avax} AVAX
                </div>
                <div className="text-xs text-blue-600">
                  <a
                    href={`https://snowtrace.io/tx/${alert.tx_hash}`}
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    View on Snowtrace
                  </a>
                </div>
              </div>
            </Card>
          ))}
        </div>
      )}
    </div>
  )
} 