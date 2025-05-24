# TrustMesh AI Dashboard

A comprehensive smart contract analysis and monitoring system for cross-chain communication and risk assessment.

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