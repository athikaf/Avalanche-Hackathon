import { useState } from 'react'
import { Button } from '@/components/ui/Button'

interface ContractAuditFormProps {
  onSubmit: (address: string) => Promise<void>
  isLoading: boolean
}

export function ContractAuditForm({ onSubmit, isLoading }: ContractAuditFormProps) {
  const [address, setAddress] = useState('')

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!address) return
    await onSubmit(address)
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label
          htmlFor="address"
          className="block text-sm font-medium text-gray-700"
        >
          Contract Address
        </label>
        <div className="mt-1">
          <input
            type="text"
            name="address"
            id="address"
            value={address}
            onChange={(e) => setAddress(e.target.value)}
            className="block w-full rounded-md border-gray-300 shadow-sm focus:border-primary-500 focus:ring-primary-500 sm:text-sm"
            placeholder="0x..."
            required
          />
        </div>
        <p className="mt-2 text-sm text-gray-500">
          Enter an Avalanche C-Chain contract address to analyze.
        </p>
      </div>

      <div>
        <Button
          type="submit"
          variant="primary"
          isLoading={isLoading}
          disabled={!address || isLoading}
        >
          Analyze Contract
        </Button>
      </div>
    </form>
  )
} 