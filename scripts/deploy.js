const hre = require("hardhat");

async function main() {
  const [deployer] = await hre.ethers.getSigners();
  console.log("Deploying contracts with the account:", deployer.address);

  // Deploy CrossChainAnalyzer
  const CrossChainAnalyzer = await hre.ethers.getContractFactory("CrossChainAnalyzer");
  const analyzer = await CrossChainAnalyzer.deploy();
  await analyzer.deployed();
  console.log("CrossChainAnalyzer deployed to:", analyzer.address);

  // Deploy CrossChainBridge
  const CrossChainBridge = await hre.ethers.getContractFactory("CrossChainBridge");
  const bridge = await CrossChainBridge.deploy();
  await bridge.deployed();
  console.log("CrossChainBridge deployed to:", bridge.address);

  // Deploy CrossChainMessage
  const CrossChainMessage = await hre.ethers.getContractFactory("CrossChainMessage");
  const message = await CrossChainMessage.deploy();
  await message.deployed();
  console.log("CrossChainMessage deployed to:", message.address);

  // Verify contracts on Etherscan
  if (hre.network.name !== "hardhat" && hre.network.name !== "localhost") {
    console.log("Waiting for block confirmations...");
    await analyzer.deployTransaction.wait(6);
    await bridge.deployTransaction.wait(6);
    await message.deployTransaction.wait(6);

    console.log("Verifying contracts...");
    await hre.run("verify:verify", {
      address: analyzer.address,
      constructorArguments: [],
    });

    await hre.run("verify:verify", {
      address: bridge.address,
      constructorArguments: [],
    });

    await hre.run("verify:verify", {
      address: message.address,
      constructorArguments: [],
    });
  }
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  }); 