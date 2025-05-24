import { useAccount, useConnect, useDisconnect } from 'wagmi'
import { injected } from 'wagmi/connectors'
import { Button } from './ui/Button'

export default function WalletConnectButton() {
  const { address, isConnected } = useAccount()
  const { connect } = useConnect({
    connector: injected(),
  })
  const { disconnect } = useDisconnect()

  if (isConnected) {
    return (
      <div className="flex items-center space-x-4">
        <span className="text-sm text-gray-500">
          {address?.slice(0, 6)}...{address?.slice(-4)}
        </span>
        <Button
          onClick={() => disconnect()}
          variant="outline"
          size="sm"
        >
          Disconnect
        </Button>
      </div>
    )
  }

  return (
    <Button
      onClick={() => connect()}
      variant="primary"
      size="sm"
    >
      Connect Wallet
    </Button>
  )
} 