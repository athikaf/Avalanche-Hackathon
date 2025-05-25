# TrustMesh AI Dashboard

A comprehensive smart contract analysis and monitoring system for cross-chain communication and risk assessment.

## Supported Networks
- Avalanche C-Chain (primary)
- Cross-chain analysis via Chainlink (Ethereum, Polygon, etc.)

## Cross-Chain Communication
- Chainlink CCIP or Chainlink nodes are used for secure cross-chain messaging and data.
- Infura is NOT used; all cross-chain data is fetched via Chainlink.

## Signature Verification
- Multi-validator set: Cross-chain messages and actions require signatures from a threshold of trusted validators, not a simple multisig from user accounts.
- Validator set is managed on-chain and can be updated by the contract owner.

## Features

### Cross-Chain Analysis
- Bridge interaction detection and monitoring
- Message passing pattern analysis
- Cross-chain transaction tracking
- Risk assessment and scoring
- Chain communication visualization

### Risk Assessment
- Bridge security analysis
- Message verification checks
- Value transfer monitoring
- Security vulnerability detection
- Risk score calculation

### Security Features
- Reentrancy protection
- Access control
- Pausable functionality
- Whitelisted analyzers
- Signature verification

### Monitoring
- Real-time transaction tracking
- Bridge interaction monitoring
- Message passing verification
- Risk score updates
- Event logging

## Project Structure

```
trustmesh-ai-dashboard/
├── backend/
│   ├── audit/
│   ├── governance/
│   ├── monitor/
│   ├── reports/
│   ├── utils/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── contracts/
│   ├── CrossChainAnalyzer.sol
│   ├── CrossChainBridge.sol
│   └── CrossChainMessage.sol
├── docs/
│   └── API.md
├── scripts/
│   ├── deploy.js
│   └── setup.sh
├── test/
│   ├── mocks/
│   │   ├── MockBridge.sol
│   │   └── MockMessage.sol
│   └── CrossChainAnalyzer.test.js
├── trustmesh_ai_dashboard/
│   ├── app/
│   │   ├── activity-monitor/
│   │   ├── contract-audit/
│   │   ├── cross-chain-analysis/
│   │   ├── governance-insights/
│   │   ├── reports/
│   │   ├── globals.css
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── components/
│   ├── next.config.mjs
│   ├── package.json
│   ├── tailwind.config.ts
│   └── tsconfig.json
├── docker-compose.yml
├── hardhat.config.js
├── package.json
├── README.md
└── requirements.txt
```

> **Note:**
> - The frontend is in `trustmesh_ai_dashboard/` (not `frontend/`).
> - The backend has additional submodules: `audit/`, `governance/`, `monitor/`.
> - Root includes scripts, configs, and documentation.

## Setup

### Prerequisites
- Node.js v16+
- Python 3.8+
- Solidity 0.8.19+
- Hardhat
- FastAPI
- React/Next.js

### Backend Setup
1. Install Python dependencies:
```bash
cd backend
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. Start the backend server:
```bash
uvicorn main:app --reload
```

### Frontend Setup
1. Install Node.js dependencies:
```bash
cd trustmesh_ai_dashboard
npm install
```

2. Set up environment variables:
```bash
cp .env.example .env.local
# Edit .env.local with your configuration
```

3. Start the development server:
```bash
npm run dev
```

### Smart Contract Setup
1. Install dependencies:
```bash
npm install --save-dev hardhat @nomiclabs/hardhat-ethers ethers @openzeppelin/contracts
```

2. Compile contracts:
```bash
npx hardhat compile
```

3. Run tests:
```bash
npx hardhat test
```

## API Endpoints

### Contract Analysis
- `POST /api/v1/analyze` - Analyze a contract
- `GET /api/v1/analysis/{address}` - Get analysis results
- `GET /api/v1/risks/{address}` - Get risk assessment

### Monitoring
- `GET /api/v1/monitor/bridge/{address}` - Monitor bridge interactions
- `GET /api/v1/monitor/messages/{address}` - Monitor message passing
- `GET /api/v1/monitor/risks/{address}` - Monitor risk changes

## Smart Contracts

### CrossChainAnalyzer
- Analyzes cross-chain interactions
- Calculates risk scores
- Identifies security vulnerabilities
- Tracks bridge and message events

### CrossChainBridge
- Handles bridge transactions
- Manages cross-chain transfers
- Verifies bridge interactions
- Tracks transaction status

### CrossChainMessage
- Manages cross-chain messages
- Verifies message authenticity
- Tracks message status
- Handles message processing

## Security

### Access Control
- Owner-only functions
- Whitelisted analyzers
- Pausable functionality
- Reentrancy protection

### Risk Management
- Bridge security checks
- Message verification
- Value transfer monitoring
- Vulnerability detection

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - see LICENSE file for details

## Support

For support, please open an issue in the GitHub repository or contact the development team.

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