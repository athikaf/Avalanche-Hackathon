# TrustMesh AI Dashboard Environment Configuration Guide

This document contains all the necessary environment variables for the TrustMesh AI Dashboard project. Copy these configurations into their respective `.env` files in each component directory.

## Backend (.env)

```env
# Server Configuration
PORT=8000
HOST=0.0.0.0
DEBUG=True
ENVIRONMENT=development

# Database Configuration
DATABASE_URL=postgresql://trustmesh:trustmesh_password@localhost:5432/trustmesh_db
DATABASE_TEST_URL=postgresql://trustmesh:trustmesh_password@localhost:5432/trustmesh_test_db

# JWT Configuration
JWT_SECRET_KEY=your_jwt_secret_key_here
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# Chainlink Configuration
CHAINLINK_ACCESS_KEY=your_chainlink_access_key
CHAINLINK_SECRET_KEY=your_chainlink_secret_key

# RPC Endpoints
AVALANCHE_RPC=https://api.avax.network/ext/bc/C/rpc
ETHEREUM_RPC=https://mainnet.infura.io/v3/your_infura_key
POLYGON_RPC=https://polygon-rpc.com
ARBITRUM_RPC=https://arb1.arbitrum.io/rpc
OPTIMISM_RPC=https://mainnet.optimism.io
BASE_RPC=https://mainnet.base.org

# Testnet RPC Endpoints
AVALANCHE_TESTNET_RPC=https://api.avax-test.network/ext/bc/C/rpc
ETHEREUM_TESTNET_RPC=https://goerli.infura.io/v3/your_infura_key
POLYGON_TESTNET_RPC=https://rpc-mumbai.maticvigil.com
ARBITRUM_TESTNET_RPC=https://goerli-rollup.arbitrum.io/rpc
OPTIMISM_TESTNET_RPC=https://goerli.optimism.io
BASE_TESTNET_RPC=https://goerli.base.org

# Chainlink CCIP Configuration
CCIP_ROUTER_ADDRESS=0x0000000000000000000000000000000000000000  # Replace with actual address
CCIP_LINK_TOKEN_ADDRESS=0x0000000000000000000000000000000000000000  # Replace with actual address

# Validator Configuration
VALIDATOR_PRIVATE_KEY=your_validator_private_key
VALIDATOR_ADDRESS=your_validator_address
MIN_VALIDATORS=3
VALIDATOR_THRESHOLD=2

# Monitoring Configuration
PROMETHEUS_PORT=9090
GRAFANA_PORT=3000

# External Services
SENTRY_DSN=your_sentry_dsn
NEW_RELIC_LICENSE_KEY=your_new_relic_key

# API Keys
ETHERSCAN_API_KEY=your_etherscan_key
SNOWTRACE_API_KEY=your_snowtrace_key
POLYGONSCAN_API_KEY=your_polygonscan_key
ARBISCAN_API_KEY=your_arbiscan_key
OPTIMISTIC_ETHERSCAN_API_KEY=your_optimistic_etherscan_key
BASESCAN_API_KEY=your_basescan_key

# Security
CORS_ORIGINS=["http://localhost:3000", "https://your-production-domain.com"]
RATE_LIMIT_REQUESTS=100
RATE_LIMIT_WINDOW=3600

# Logging
LOG_LEVEL=INFO
LOG_FILE=trustmesh.log
```

## Frontend (.env.local)

```env
# API Configuration
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_WS_URL=ws://localhost:8000

# Chain Configuration
NEXT_PUBLIC_DEFAULT_CHAIN=avalanche
NEXT_PUBLIC_SUPPORTED_CHAINS=["avalanche", "ethereum", "polygon", "arbitrum", "optimism", "base"]

# RPC Endpoints
NEXT_PUBLIC_AVALANCHE_RPC=https://api.avax.network/ext/bc/C/rpc
NEXT_PUBLIC_ETHEREUM_RPC=https://mainnet.infura.io/v3/your_infura_key
NEXT_PUBLIC_POLYGON_RPC=https://polygon-rpc.com
NEXT_PUBLIC_ARBITRUM_RPC=https://arb1.arbitrum.io/rpc
NEXT_PUBLIC_OPTIMISM_RPC=https://mainnet.optimism.io
NEXT_PUBLIC_BASE_RPC=https://mainnet.base.org

# Testnet RPC Endpoints
NEXT_PUBLIC_AVALANCHE_TESTNET_RPC=https://api.avax-test.network/ext/bc/C/rpc
NEXT_PUBLIC_ETHEREUM_TESTNET_RPC=https://goerli.infura.io/v3/your_infura_key
NEXT_PUBLIC_POLYGON_TESTNET_RPC=https://rpc-mumbai.maticvigil.com
NEXT_PUBLIC_ARBITRUM_TESTNET_RPC=https://goerli-rollup.arbitrum.io/rpc
NEXT_PUBLIC_OPTIMISM_TESTNET_RPC=https://goerli.optimism.io
NEXT_PUBLIC_BASE_TESTNET_RPC=https://goerli.base.org

# Contract Addresses
NEXT_PUBLIC_CROSS_CHAIN_MESSAGE_ADDRESS=0x0000000000000000000000000000000000000000
NEXT_PUBLIC_GOVERNANCE_ADDRESS=0x0000000000000000000000000000000000000000
NEXT_PUBLIC_MONITOR_ADDRESS=0x0000000000000000000000000000000000000000

# Analytics
NEXT_PUBLIC_GA_TRACKING_ID=your_ga_tracking_id
NEXT_PUBLIC_MIXPANEL_TOKEN=your_mixpanel_token

# Feature Flags
NEXT_PUBLIC_ENABLE_TESTNET=true
NEXT_PUBLIC_ENABLE_CROSS_CHAIN=true
NEXT_PUBLIC_ENABLE_GOVERNANCE=true
```

## Hardhat (.env)

```env
# Network Configuration
PRIVATE_KEY=your_deployer_private_key
INFURA_API_KEY=your_infura_key

# Contract Addresses
CROSS_CHAIN_MESSAGE_ADDRESS=0x0000000000000000000000000000000000000000
GOVERNANCE_ADDRESS=0x0000000000000000000000000000000000000000
MONITOR_ADDRESS=0x0000000000000000000000000000000000000000

# Validator Configuration
VALIDATOR_PRIVATE_KEY=your_validator_private_key
VALIDATOR_ADDRESS=your_validator_address

# Chainlink Configuration
CHAINLINK_ACCESS_KEY=your_chainlink_access_key
CHAINLINK_SECRET_KEY=your_chainlink_secret_key

# API Keys
ETHERSCAN_API_KEY=your_etherscan_key
SNOWTRACE_API_KEY=your_snowtrace_key
POLYGONSCAN_API_KEY=your_polygonscan_key
ARBISCAN_API_KEY=your_arbiscan_key
OPTIMISTIC_ETHERSCAN_API_KEY=your_optimistic_etherscan_key
BASESCAN_API_KEY=your_basescan_key
```

## Docker Compose Environment Variables

```env
# Database
POSTGRES_USER=trustmesh
POSTGRES_PASSWORD=trustmesh_password
POSTGRES_DB=trustmesh_db

# Redis
REDIS_PASSWORD=your_redis_password

# Monitoring
PROMETHEUS_PASSWORD=your_prometheus_password
GRAFANA_PASSWORD=your_grafana_password

# Chainlink Node
CHAINLINK_EMAIL=your_chainlink_email
CHAINLINK_PASSWORD=your_chainlink_password
```

## Important Notes

1. Replace all placeholder values (starting with `your_`) with actual secure values.
2. Keep all `.env` files secure and never commit them to version control.
3. Use different values for development, staging, and production environments.
4. Regularly rotate sensitive keys and passwords.
5. Store production secrets in a secure vault or secret management system.

## Security Best Practices

1. Use strong, unique passwords for all services.
2. Enable 2FA where available.
3. Regularly rotate API keys and secrets.
4. Use environment-specific configurations.
5. Implement proper access controls and rate limiting.
6. Monitor and log all access attempts.
7. Keep all dependencies updated.
8. Use HTTPS for all external communications.
9. Implement proper CORS policies.
10. Use secure session management.

## Deployment Checklist

1. [ ] Set up all environment variables
2. [ ] Configure RPC endpoints
3. [ ] Set up Chainlink nodes
4. [ ] Configure validator set
5. [ ] Set up monitoring
6. [ ] Configure security settings
7. [ ] Test all integrations
8. [ ] Verify cross-chain functionality
9. [ ] Set up backup systems
10. [ ] Configure logging and alerts 