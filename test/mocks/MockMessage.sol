// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/access/Ownable.sol";

contract MockMessage is Ownable {
    struct Message {
        bytes32 messageHash;
        uint256 sourceChainId;
        uint256 targetChainId;
        string messageType;
        uint256 timestamp;
        bool isVerified;
    }

    Message[] public messages;

    event MessageAdded(
        bytes32 indexed messageHash,
        uint256 sourceChainId,
        uint256 targetChainId,
        string messageType
    );

    event MessageVerified(
        bytes32 indexed messageHash,
        uint256 sourceChainId,
        uint256 targetChainId
    );

    function addMessage(
        bytes32 _messageHash,
        uint256 _sourceChainId,
        uint256 _targetChainId,
        string memory _messageType
    ) external onlyOwner {
        messages.push(Message({
            messageHash: _messageHash,
            sourceChainId: _sourceChainId,
            targetChainId: _targetChainId,
            messageType: _messageType,
            timestamp: block.timestamp,
            isVerified: false
        }));

        emit MessageAdded(
            _messageHash,
            _sourceChainId,
            _targetChainId,
            _messageType
        );
    }

    function verifyMessage(uint256 _messageIndex) external onlyOwner {
        require(_messageIndex < messages.length, "Invalid message index");
        require(!messages[_messageIndex].isVerified, "Message already verified");

        messages[_messageIndex].isVerified = true;

        emit MessageVerified(
            messages[_messageIndex].messageHash,
            messages[_messageIndex].sourceChainId,
            messages[_messageIndex].targetChainId
        );
    }

    function getMessages() external view returns (Message[] memory) {
        return messages;
    }

    function getMessageCount() external view returns (uint256) {
        return messages.length;
    }
} 