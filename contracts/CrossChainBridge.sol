// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title CrossChainBridge
 * @dev Contract for handling cross-chain bridge interactions
 */
contract CrossChainBridge is ReentrancyGuard, Ownable {
    struct BridgeTransaction {
        uint256 transactionId;
        address sender;
        address token;
        uint256 amount;
        uint256 sourceChainId;
        uint256 targetChainId;
        uint256 timestamp;
        bool isCompleted;
    }

    // Mapping from transaction ID to bridge transaction
    mapping(uint256 => BridgeTransaction) public transactions;
    
    // Mapping from chain ID to bridge contract address
    mapping(uint256 => address) public bridgeContracts;
    
    // Counter for transaction IDs
    uint256 private _transactionIdCounter;

    // Events
    event BridgeTransactionInitiated(
        uint256 indexed transactionId,
        address indexed sender,
        address indexed token,
        uint256 amount,
        uint256 sourceChainId,
        uint256 targetChainId
    );

    event BridgeTransactionCompleted(
        uint256 indexed transactionId,
        address indexed recipient,
        uint256 amount
    );

    event BridgeContractRegistered(
        uint256 indexed chainId,
        address indexed bridgeContract
    );

    /**
     * @dev Initialize a bridge transaction
     * @param _token Token address to bridge
     * @param _amount Amount to bridge
     * @param _targetChainId Target chain ID
     */
    function initiateBridge(
        address _token,
        uint256 _amount,
        uint256 _targetChainId
    ) external nonReentrant returns (uint256) {
        require(_token != address(0), "Invalid token address");
        require(_amount > 0, "Amount must be greater than 0");
        require(bridgeContracts[_targetChainId] != address(0), "Target chain not supported");

        // Transfer tokens from sender
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);

        _transactionIdCounter++;
        uint256 transactionId = _transactionIdCounter;

        // Create bridge transaction
        transactions[transactionId] = BridgeTransaction({
            transactionId: transactionId,
            sender: msg.sender,
            token: _token,
            amount: _amount,
            sourceChainId: block.chainid,
            targetChainId: _targetChainId,
            timestamp: block.timestamp,
            isCompleted: false
        });

        emit BridgeTransactionInitiated(
            transactionId,
            msg.sender,
            _token,
            _amount,
            block.chainid,
            _targetChainId
        );

        return transactionId;
    }

    /**
     * @dev Complete a bridge transaction
     * @param _transactionId Transaction ID to complete
     * @param _recipient Recipient address
     */
    function completeBridge(
        uint256 _transactionId,
        address _recipient
    ) external onlyOwner nonReentrant {
        BridgeTransaction storage transaction = transactions[_transactionId];
        require(transaction.sender != address(0), "Transaction does not exist");
        require(!transaction.isCompleted, "Transaction already completed");

        // Transfer tokens to recipient
        IERC20(transaction.token).transfer(_recipient, transaction.amount);

        transaction.isCompleted = true;

        emit BridgeTransactionCompleted(
            _transactionId,
            _recipient,
            transaction.amount
        );
    }

    /**
     * @dev Register a bridge contract for a chain
     * @param _chainId Chain ID
     * @param _bridgeContract Bridge contract address
     */
    function registerBridgeContract(
        uint256 _chainId,
        address _bridgeContract
    ) external onlyOwner {
        require(_bridgeContract != address(0), "Invalid bridge contract address");
        bridgeContracts[_chainId] = _bridgeContract;

        emit BridgeContractRegistered(_chainId, _bridgeContract);
    }

    /**
     * @dev Get bridge transaction details
     * @param _transactionId Transaction ID
     * @return Bridge transaction details
     */
    function getTransaction(uint256 _transactionId)
        external
        view
        returns (BridgeTransaction memory)
    {
        require(transactions[_transactionId].sender != address(0), "Transaction does not exist");
        return transactions[_transactionId];
    }

    /**
     * @dev Check if a chain is supported
     * @param _chainId Chain ID to check
     * @return True if chain is supported
     */
    function isChainSupported(uint256 _chainId) external view returns (bool) {
        return bridgeContracts[_chainId] != address(0);
    }
} 