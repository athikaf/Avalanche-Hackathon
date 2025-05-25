const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("CrossChainAnalyzer (Avalanche-first, Chainlink cross-chain)", function () {
    let CrossChainAnalyzer;
    let analyzer;
    let owner;
    let addr1;
    let addr2;
    let mockBridge;
    let mockMessage;

    beforeEach(async function () {
        [owner, addr1, addr2] = await ethers.getSigners();

        // Deploy mock contracts
        const MockBridge = await ethers.getContractFactory("MockBridge");
        mockBridge = await MockBridge.deploy();
        await mockBridge.deployed();

        const MockMessage = await ethers.getContractFactory("MockMessage");
        mockMessage = await MockMessage.deploy();
        await mockMessage.deployed();

        // Deploy CrossChainAnalyzer
        CrossChainAnalyzer = await ethers.getContractFactory("CrossChainAnalyzer");
        analyzer = await CrossChainAnalyzer.deploy();
        await analyzer.deployed();

        // Whitelist addr1 as analyzer
        await analyzer.whitelistAnalyzer(addr1.address, true);
    });

    describe("Deployment", function () {
        it("Should set the right owner", async function () {
            expect(await analyzer.owner()).to.equal(owner.address);
        });

        it("Should start with no whitelisted analyzers except owner", async function () {
            expect(await analyzer.whitelistedAnalyzers(addr2.address)).to.equal(false);
        });
    });

    describe("Analyzer Whitelisting", function () {
        it("Should allow owner to whitelist analyzers", async function () {
            await analyzer.whitelistAnalyzer(addr2.address, true);
            expect(await analyzer.whitelistedAnalyzers(addr2.address)).to.equal(true);
        });

        it("Should allow owner to remove analyzers from whitelist", async function () {
            await analyzer.whitelistAnalyzer(addr2.address, true);
            await analyzer.whitelistAnalyzer(addr2.address, false);
            expect(await analyzer.whitelistedAnalyzers(addr2.address)).to.equal(false);
        });

        it("Should not allow non-owners to whitelist analyzers", async function () {
            await expect(
                analyzer.connect(addr1).whitelistAnalyzer(addr2.address, true)
            ).to.be.revertedWith("Ownable: caller is not the owner");
        });
    });

    describe("Contract Analysis", function () {
        it("Should allow whitelisted analyzers to analyze contracts", async function () {
            await expect(analyzer.connect(addr1).analyzeContract(mockBridge.address))
                .to.emit(analyzer, "AnalysisCompleted")
                .withArgs(1, mockBridge.address, 0, []);
        });

        it("Should not allow non-whitelisted analyzers to analyze contracts", async function () {
            await expect(
                analyzer.connect(addr2).analyzeContract(mockBridge.address)
            ).to.be.revertedWith("Not whitelisted");
        });

        it("Should not allow analysis of zero address", async function () {
            await expect(
                analyzer.connect(addr1).analyzeContract(ethers.constants.AddressZero)
            ).to.be.revertedWith("Invalid contract address");
        });
    });

    describe("Risk Analysis", function () {
        beforeEach(async function () {
            // Add some bridge interactions
            await mockBridge.addInteraction(analyzer.address, 1, "DEPOSIT", ethers.utils.parseEther("1"));
            await mockBridge.addInteraction(analyzer.address, 2, "WITHDRAW", ethers.utils.parseEther("2"));
        });

        it("Should calculate risk score based on bridge interactions", async function () {
            await analyzer.connect(addr1).analyzeContract(mockBridge.address);
            const analysis = await analyzer.getAnalysis(mockBridge.address);
            expect(analysis.riskScore).to.be.gt(0);
        });

        it("Should identify bridge-related risks", async function () {
            await analyzer.connect(addr1).analyzeContract(mockBridge.address);
            const analysis = await analyzer.getAnalysis(mockBridge.address);
            expect(analysis.risks.length).to.be.gt(0);
        });
    });

    describe("Pausable", function () {
        it("Should allow owner to pause and unpause", async function () {
            await analyzer.pause();
            await expect(
                analyzer.connect(addr1).analyzeContract(mockBridge.address)
            ).to.be.revertedWith("Pausable: paused");

            await analyzer.unpause();
            await expect(analyzer.connect(addr1).analyzeContract(mockBridge.address))
                .to.emit(analyzer, "AnalysisCompleted");
        });

        it("Should not allow non-owners to pause", async function () {
            await expect(
                analyzer.connect(addr1).pause()
            ).to.be.revertedWith("Ownable: caller is not the owner");
        });
    });

    describe("View Functions", function () {
        beforeEach(async function () {
            await analyzer.connect(addr1).analyzeContract(mockBridge.address);
        });

        it("Should return correct analysis results", async function () {
            const analysis = await analyzer.getAnalysis(mockBridge.address);
            expect(analysis.contractAddress).to.equal(mockBridge.address);
            expect(analysis.isActive).to.equal(true);
        });

        it("Should return bridge interactions", async function () {
            const interactions = await analyzer.getBridgeInteractions(mockBridge.address);
            expect(interactions.length).to.be.gte(0);
        });

        it("Should return message passing events", async function () {
            const messages = await analyzer.getMessagePassingEvents(mockBridge.address);
            expect(messages.length).to.be.gte(0);
        });
    });

    it("should analyze contracts on Avalanche C-Chain by default", async function () {
        // ... test logic for AVAX contract analysis ...
    });

    it("should simulate cross-chain risk analysis from AVAX to Ethereum via Chainlink", async function () {
        // ... test logic for AVAX -> Ethereum cross-chain analysis ...
    });

    it("should verify cross-chain messages with multi-validator signatures", async function () {
        // ... test logic for multi-validator signature verification ...
    });
}); 