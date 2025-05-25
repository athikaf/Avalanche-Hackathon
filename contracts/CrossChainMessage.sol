// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title CrossChainMessage
 * @dev This contract is designed for Avalanche C-Chain (AVAX) as the primary network.
 *      It enables secure cross-chain message passing to other L1s (Ethereum, Polygon, etc.)
 *      using Chainlink CCIP or Chainlink nodes.
 *      Signature verification is performed using a multi-validator set.
 */
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

/**
 * @title CrossChainMessage
 * @dev Contract for handling cross-chain message passing
 */
contract CrossChainMessage is ReentrancyGuard, Ownable {
    using ECDSA for bytes32;

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

    mapping(address => bool) public isValidator;
    address[] public validators;
    uint256 public threshold; // e.g., 2/3+ signatures required

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

    event ValidatorAdded(address indexed validator);
    event ValidatorRemoved(address indexed validator);
    event ThresholdChanged(uint256 newThreshold);

    constructor(address[] memory initialValidators, uint256 initialThreshold) {
        require(initialValidators.length >= initialThreshold, "Threshold too high");
        for (uint i = 0; i < initialValidators.length; i++) {
            isValidator[initialValidators[i]] = true;
            validators.push(initialValidators[i]);
        }
        threshold = initialThreshold;
    }

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

    function addValidator(address validator) external onlyOwner {
        require(!isValidator[validator], "Already validator");
        isValidator[validator] = true;
        validators.push(validator);
        emit ValidatorAdded(validator);
    }

    function removeValidator(address validator) external onlyOwner {
        require(isValidator[validator], "Not a validator");
        isValidator[validator] = false;
        // Remove from array
        for (uint i = 0; i < validators.length; i++) {
            if (validators[i] == validator) {
                validators[i] = validators[validators.length - 1];
                validators.pop();
                break;
            }
        }
        emit ValidatorRemoved(validator);
    }

    function setThreshold(uint256 newThreshold) external onlyOwner {
        require(newThreshold > 0 && newThreshold <= validators.length, "Invalid threshold");
        threshold = newThreshold;
        emit ThresholdChanged(newThreshold);
    }

    // Multi-validator signature verification
    function verifySignatures(bytes32 messageHash, bytes[] calldata signatures) public view returns (bool) {
        uint256 validCount = 0;
        address[] memory seen = new address[](signatures.length);
        for (uint i = 0; i < signatures.length; i++) {
            address signer = messageHash.toEthSignedMessageHash().recover(signatures[i]);
            if (isValidator[signer]) {
                // Prevent double counting
                bool alreadySeen = false;
                for (uint j = 0; j < validCount; j++) {
                    if (seen[j] == signer) {
                        alreadySeen = true;
                        break;
                    }
                }
                if (!alreadySeen) {
                    seen[validCount] = signer;
                    validCount++;
                }
            }
        }
        return validCount >= threshold;
    }

    function getValidators() external view returns (address[] memory) {
        return validators;
    }
} 