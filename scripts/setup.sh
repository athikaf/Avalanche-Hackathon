#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${GREEN}Starting TrustMesh AI Dashboard setup...${NC}"

# Check prerequisites
echo -e "${YELLOW}Checking prerequisites...${NC}"

# Check Node.js
if ! command -v node &> /dev/null; then
    echo -e "${RED}Node.js is not installed. Please install Node.js v16+${NC}"
    exit 1
fi

# Check Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Python 3 is not installed. Please install Python 3.8+${NC}"
    exit 1
fi

# Check Solidity
if ! command -v solc &> /dev/null; then
    echo -e "${RED}Solidity compiler is not installed. Please install solc 0.8.19+${NC}"
    exit 1
fi

# Create project structure
echo -e "${YELLOW}Creating project structure...${NC}"
mkdir -p contracts test/mocks backend/{utils,reports,services,models} frontend/{components,pages,styles} docs

# Initialize git
echo -e "${YELLOW}Initializing git repository...${NC}"
git init

# Create .gitignore
echo -e "${YELLOW}Creating .gitignore...${NC}"
cat > .gitignore << EOL
# Dependencies
node_modules/
venv/
__pycache__/

# Environment
.env
.env.local
.env.*.local

# Build
dist/
build/
.next/

# Logs
logs/
*.log

# IDE
.vscode/
.idea/

# Testing
coverage/
.coverage
EOL

# Initialize npm project
echo -e "${YELLOW}Initializing npm project...${NC}"
npm init -y

# Install dependencies
echo -e "${YELLOW}Installing dependencies...${NC}"
npm install --save-dev hardhat @nomiclabs/hardhat-ethers @nomiclabs/hardhat-waffle @nomiclabs/hardhat-etherscan @openzeppelin/contracts chai dotenv ethereum-waffle ethers prettier prettier-plugin-solidity solhint solidity-coverage

# Create Python virtual environment
echo -e "${YELLOW}Setting up Python environment...${NC}"
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
echo -e "${YELLOW}Installing Python dependencies...${NC}"
pip install -r backend/requirements.txt

# Create environment files
echo -e "${YELLOW}Creating environment files...${NC}"
cat > .env << EOL
# Blockchain
PRIVATE_KEY=your_private_key_here
INFURA_API_KEY=your_infura_key_here
ETHERSCAN_API_KEY=your_etherscan_key_here

# Network RPCs
ETHEREUM_RPC=https://mainnet.infura.io/v3/your_infura_key
AVALANCHE_RPC=https://api.avax.network/ext/bc/C/rpc
POLYGON_RPC=https://polygon-rpc.com

# Database
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/trustmesh
REDIS_URL=redis://localhost:6379/0

# API
API_PORT=8000
API_HOST=0.0.0.0
CORS_ORIGINS=["http://localhost:3000"]

# Security
JWT_SECRET=your_jwt_secret_here
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
EOL

# Create frontend environment file
cat > frontend/.env.local << EOL
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_CONTRACT_ADDRESS=your_deployed_contract_address
EOL

# Initialize Next.js project
echo -e "${YELLOW}Setting up Next.js project...${NC}"
cd frontend
npx create-next-app@latest . --typescript
npm install @chakra-ui/react @emotion/react @emotion/styled framer-motion ethers axios
cd ..

# Create initial documentation
echo -e "${YELLOW}Creating documentation...${NC}"
cp docs/DETAILED_IMPLEMENTATION_GUIDE.md docs/README.md

echo -e "${GREEN}Setup completed successfully!${NC}"
echo -e "${YELLOW}Next steps:${NC}"
echo "1. Update .env files with your API keys and configuration"
echo "2. Review the implementation guide in docs/DETAILED_IMPLEMENTATION_GUIDE.md"
echo "3. Start development by running:"
echo "   - Backend: cd backend && uvicorn main:app --reload"
echo "   - Frontend: cd frontend && npm run dev"
echo "   - Smart contracts: npx hardhat node" 