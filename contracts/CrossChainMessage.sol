// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CrossChainMessage
 * @dev Contract for handling cross-chain message passing
 */
contract CrossChainMessage is ReentrancyGuard, Ownable {
    struct Message {
        uint256 messageId;
        address sender;
        bytes32 messageHash;
        uint256 sourceChainId;
        uint256 targetChainId;
        uint256 timestamp;
        bool isVerified;
        bool isProcessed;
    }

    // Mapping from message ID to message
    mapping(uint256 => Message) public messages;
    
    // Mapping from message hash to processed status
    mapping(bytes32 => bool) public processedMessages;
    
    // Mapping from chain ID to message verifier contract
    mapping(uint256 => address) public messageVerifiers;
    
    // Counter for message IDs
    uint256 private _messageIdCounter;

    // Events
    event MessageSent(
        uint256 indexed messageId,
        address indexed sender,
        bytes32 indexed messageHash,
        uint256 sourceChainId,
        uint256 targetChainId
    );

    event MessageVerified(
        uint256 indexed messageId,
        bytes32 indexed messageHash,
        uint256 sourceChainId,
        uint256 targetChainId
    );

    event MessageProcessed(
        uint256 indexed messageId,
        bytes32 indexed messageHash,
        uint256 sourceChainId,
        uint256 targetChainId
    );

    event MessageVerifierRegistered(
        uint256 indexed chainId,
        address indexed verifierContract
    );

    /**
     * @dev Send a cross-chain message
     * @param _messageHash Hash of the message
     * @param _targetChainId Target chain ID
     */
    function sendMessage(
        bytes32 _messageHash,
        uint256 _targetChainId
    ) external nonReentrant returns (uint256) {
        require(_messageHash != bytes32(0), "Invalid message hash");
        require(messageVerifiers[_targetChainId] != address(0), "Target chain not supported");

        _messageIdCounter++;
        uint256 messageId = _messageIdCounter;

        // Create message
        messages[messageId] = Message({
            messageId: messageId,
            sender: msg.sender,
            messageHash: _messageHash,
            sourceChainId: block.chainid,
            targetChainId: _targetChainId,
            timestamp: block.timestamp,
            isVerified: false,
            isProcessed: false
        });

        emit MessageSent(
            messageId,
            msg.sender,
            _messageHash,
            block.chainid,
            _targetChainId
        );

        return messageId;
    }

    /**
     * @dev Verify a cross-chain message
     * @param _messageId Message ID to verify
     * @param _signature Signature for verification
     */
    function verifyMessage(
        uint256 _messageId,
        bytes memory _signature
    ) external onlyOwner nonReentrant {
        Message storage message = messages[_messageId];
        require(message.sender != address(0), "Message does not exist");
        require(!message.isVerified, "Message already verified");

        // Verify signature (implementation depends on your verification mechanism)
        require(_verifySignature(message.messageHash, _signature), "Invalid signature");

        message.isVerified = true;

        emit MessageVerified(
            _messageId,
            message.messageHash,
            message.sourceChainId,
            message.targetChainId
        );
    }

    /**
     * @dev Process a verified message
     * @param _messageId Message ID to process
     */
    function processMessage(uint256 _messageId) external onlyOwner nonReentrant {
        Message storage message = messages[_messageId];
        require(message.sender != address(0), "Message does not exist");
        require(message.isVerified, "Message not verified");
        require(!message.isProcessed, "Message already processed");
        require(!processedMessages[message.messageHash], "Message already processed");

        message.isProcessed = true;
        processedMessages[message.messageHash] = true;

        emit MessageProcessed(
            _messageId,
            message.messageHash,
            message.sourceChainId,
            message.targetChainId
        );
    }

    /**
     * @dev Register a message verifier for a chain
     * @param _chainId Chain ID
     * @param _verifierContract Verifier contract address
     */
    function registerMessageVerifier(
        uint256 _chainId,
        address _verifierContract
    ) external onlyOwner {
        require(_verifierContract != address(0), "Invalid verifier contract address");
        messageVerifiers[_chainId] = _verifierContract;

        emit MessageVerifierRegistered(_chainId, _verifierContract);
    }

    /**
     * @dev Get message details
     * @param _messageId Message ID
     * @return Message details
     */
    function getMessage(uint256 _messageId)
        external
        view
        returns (Message memory)
    {
        require(messages[_messageId].sender != address(0), "Message does not exist");
        return messages[_messageId];
    }

    /**
     * @dev Check if a message has been processed
     * @param _messageHash Message hash to check
     * @return True if message has been processed
     */
    function isMessageProcessed(bytes32 _messageHash) external view returns (bool) {
        return processedMessages[_messageHash];
    }

    /**
     * @dev Verify a signature
     * @param _messageHash Message hash to verify
     * @param _signature Signature to verify
     * @return True if signature is valid
     */
    function _verifySignature(
        bytes32 _messageHash,
        bytes memory _signature
    ) internal view returns (bool) {
        // Implement your signature verification logic here
        // This is a placeholder implementation
        return true;
    }
} 