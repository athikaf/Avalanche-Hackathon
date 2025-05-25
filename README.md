# TrustMesh AI Dashboard

A comprehensive smart contract auditing and cross-chain risk analysis platform built with FastAPI, Next.js, and Solidity.

## Features

- **Multi-Chain Support**: Primary on Avalanche (AVAX) with cross-chain capabilities via Chainlink CCIP
- **Smart Contract Auditing**: AI-powered analysis of smart contracts
- **Cross-Chain Risk Analysis**: Monitor and analyze risks across multiple chains
- **Governance Integration**: DAO governance and proposal analysis
- **Whale Monitoring**: Track large transactions and wallet movements
- **Real-time Alerts**: Instant notifications for critical events
- **Comprehensive Reporting**: Detailed analysis and risk assessment reports

## Architecture

### Backend (FastAPI)
- RESTful API with WebSocket support
- Multi-validator signature verification
- Chainlink CCIP integration
- Real-time monitoring and alerts
- Advanced caching with Redis
- Queue processing with Celery
- Comprehensive logging and monitoring

### Frontend (Next.js)
- Modern, responsive UI
- Real-time updates via WebSocket
- Multi-chain wallet integration
- Dark/Light mode support
- Internationalization
- PWA support
- Advanced analytics

### Smart Contracts
- Multi-validator set for cross-chain communication
- Governance contracts
- Monitoring contracts
- Cross-chain message contracts

## Prerequisites

- Python 3.9+
- Node.js 16+
- PostgreSQL 13+
- Redis 6+
- Docker and Docker Compose
- Chainlink Node
- Access to RPC endpoints for supported chains

## Supported Chains

### Mainnet
- Avalanche (Primary)
- Ethereum
- Polygon
- Arbitrum
- Optimism
- Base

### Testnet
- Avalanche Fuji
- Ethereum Goerli
- Polygon Mumbai
- Arbitrum Goerli
- Optimism Goerli
- Base Goerli

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/your-org/trustmesh-ai-dashboard.git
   cd trustmesh-ai-dashboard
   ```

2. Set up environment variables:
   ```bash
   # Copy example environment files
   cp env_examples/backend.env backend/.env
   cp env_examples/frontend.env frontend/.env.local
   cp env_examples/hardhat.env .env
   cp env_examples/docker-compose.env .env
   
   # Update the values in each .env file
   ```

3. Start the development environment:
   ```bash
   docker-compose up -d
   ```

4. Initialize the database:
   ```bash
   docker-compose exec backend alembic upgrade head
   ```

5. Start the development servers:
   ```bash
   # Backend
   cd backend
   uvicorn main:app --reload

   # Frontend
   cd frontend
   npm run dev
   ```

## Configuration

### Backend Configuration
- Server settings
- Database connection
- JWT authentication
- Chainlink integration
- RPC endpoints
- Validator configuration
- Monitoring setup
- Security settings
- Logging configuration
- Cache settings
- Queue configuration
- Backup settings

### Frontend Configuration
- API endpoints
- Chain configuration
- RPC endpoints
- Contract addresses
- Analytics integration
- Feature flags
- Security settings
- Performance optimization
- Error tracking
- UI/UX settings
- Social media integration
- Documentation links

### Smart Contract Configuration
- Network settings
- Contract addresses
- Validator configuration
- Chainlink settings
- Gas optimization
- Security settings
- Testing configuration
- Documentation generation
- Monitoring setup
- Backup configuration

### Docker Configuration
- Database tuning
- Redis optimization
- Monitoring setup
- Chainlink node configuration
- Backup system
- Security settings

## Development

### Backend Development
1. Set up Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   ```

2. Run tests:
   ```bash
   pytest
   ```

3. Start development server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Development
1. Install dependencies:
   ```bash
   npm install
   ```

2. Run tests:
   ```bash
   npm test
   ```

3. Start development server:
   ```bash
   npm run dev
   ```

### Smart Contract Development
1. Install dependencies:
   ```bash
   npm install
   ```

2. Compile contracts:
   ```bash
   npx hardhat compile
   ```

3. Run tests:
   ```bash
   npx hardhat test
   ```

## Deployment

### Production Deployment
1. Set up production environment variables
2. Configure SSL/TLS certificates
3. Set up monitoring and alerting
4. Configure backup systems
5. Deploy using Docker Compose:
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

### Vercel Deployment
1. Connect your GitHub repository to Vercel
2. Configure environment variables
3. Deploy:
   ```bash
   vercel --prod
   ```

## Security

### Security Features
- Multi-validator signature verification
- Rate limiting
- CORS protection
- CSRF protection
- HSTS
- Content Security Policy
- Secure cookie settings
- Input validation
- SQL injection protection
- XSS protection
- Regular security audits

### Security Best Practices
1. Use strong, unique passwords
2. Enable 2FA where available
3. Regularly rotate API keys and secrets
4. Use environment-specific configurations
5. Implement proper access controls
6. Monitor and log all access attempts
7. Keep dependencies updated
8. Use HTTPS for all communications
9. Implement proper CORS policies
10. Use secure session management

## Monitoring

### Monitoring Setup
- Prometheus metrics
- Grafana dashboards
- AlertManager configuration
- Log aggregation
- Performance monitoring
- Error tracking
- Chain monitoring
- Validator monitoring
- Cross-chain monitoring

### Alerting
- Email notifications
- Slack integration
- Discord integration
- Telegram integration
- Custom webhook support
- Alert thresholds
- Alert grouping
- Alert routing
- Alert silencing

## Backup

### Backup Configuration
- Automated backups
- Backup scheduling
- Retention policies
- Encryption
- Cross-region replication
- Backup verification
- Restore testing
- Disaster recovery

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- Documentation: [docs.trustmesh.com](https://docs.trustmesh.com)
- API Documentation: [api-docs.trustmesh.com](https://api-docs.trustmesh.com)
- Support: [support.trustmesh.com](https://support.trustmesh.com)
- Discord: [discord.gg/trustmesh](https://discord.gg/trustmesh)
- Telegram: [t.me/trustmesh](https://t.me/trustmesh)
- Twitter: [@trustmesh](https://twitter.com/trustmesh)

# Agents Implemented

The TrustMesh AI Dashboard includes the following agents (automation/AI modules):

1. **Contract Analysis Agent**
   - Analyzes smart contracts for security risks, vulnerabilities, and risk scoring.
2. **Cross-Chain Analysis Agent**
   - Detects and analyzes cross-chain interactions, bridge usage, message passing, and associated risks.
3. **Governance/Proposal Analysis Agent**
   - Analyzes DAO proposals using LLMs, providing summaries, risk analysis, and recommendations.
4. **Monitoring/Whale Monitoring Agent**
   - Monitors large transactions, whale activity, and abnormal contract interactions.
5. **Report Generation Agent**
   - Generates structured reports for contract and cross-chain analysis, including executive summaries, risk breakdowns, and recommendations.

## Agent Output Reliability & Limitations
- All agents provide recommendations and summaries based on actual on-chain data, contract bytecode, or proposal text.
- LLM-based agents include a disclaimer: _"This analysis is based on available data and may not capture all risks. Please verify findings independently."_
- No agent guarantees detection of all vulnerabilities or risks. All outputs are for informational purposes only.

## Example Output (Contract Analysis)
```json
{
  "contractAddress": "0x...",
  "riskScore": 72,
  "riskCategories": [
    {"category": "Bridge Risks", "score": 20, "details": ["Unverified bridge interaction"]},
    {"category": "Message Risks", "score": 15, "details": ["Unverified message passing"]},
    {"category": "Security Risks", "score": 30, "details": ["Potential reentrancy vulnerability"]},
    {"category": "Value Risks", "score": 7, "details": []}
  ],
  "timestamp": "2024-05-01T12:00:00Z",
  "disclaimer": "This analysis is based on available data and may not capture all risks. Please verify findings independently."
}
``` 