import { Card } from '@/components/ui/Card'
import {
  DocumentMagnifyingGlassIcon,
  ChartBarIcon,
  DocumentTextIcon,
  ClipboardDocumentListIcon,
} from '@heroicons/react/24/outline'

const features = [
  {
    name: 'Contract Audit',
    description: 'Analyze smart contracts for security vulnerabilities and best practices.',
    icon: DocumentMagnifyingGlassIcon,
    href: '/contract-audit',
  },
  {
    name: 'Activity Monitor',
    description: 'Track whale movements and significant on-chain activities.',
    icon: ChartBarIcon,
    href: '/activity-monitor',
  },
  {
    name: 'Governance Insights',
    description: 'Get AI-powered analysis of DAO proposals and governance decisions.',
    icon: DocumentTextIcon,
    href: '/governance-insights',
  },
  {
    name: 'Reports',
    description: 'Generate comprehensive reports for contracts and protocols.',
    icon: ClipboardDocumentListIcon,
    href: '/reports',
  },
]

export default function Home() {
  return (
    <div className="space-y-8">
      <div>
        <h2 className="text-2xl font-bold text-gray-900">Welcome to TrustMesh AI</h2>
        <p className="mt-2 text-gray-600">
          Your comprehensive blockchain analytics and security platform for Avalanche C-Chain.
        </p>
      </div>

      <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
        {features.map((feature) => (
          <Card
            key={feature.name}
            href={feature.href}
            className="relative group"
          >
            <div className="flex items-center space-x-4">
              <div className="flex-shrink-0">
                <feature.icon
                  className="h-6 w-6 text-primary-600"
                  aria-hidden="true"
                />
              </div>
              <div>
                <h3 className="text-lg font-medium text-gray-900">
                  {feature.name}
                </h3>
                <p className="mt-1 text-sm text-gray-500">
                  {feature.description}
                </p>
              </div>
            </div>
          </Card>
        ))}
      </div>
    </div>
  )
} 