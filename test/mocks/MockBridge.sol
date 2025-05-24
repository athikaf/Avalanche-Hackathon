// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/access/Ownable.sol";

contract MockBridge is Ownable {
    struct Interaction {
        address contractAddress;
        uint256 chainId;
        string interactionType;
        uint256 value;
        uint256 timestamp;
    }

    Interaction[] public interactions;

    event InteractionAdded(
        address indexed contractAddress,
        uint256 chainId,
        string interactionType,
        uint256 value
    );

    function addInteraction(
        address _contractAddress,
        uint256 _chainId,
        string memory _interactionType,
        uint256 _value
    ) external onlyOwner {
        interactions.push(Interaction({
            contractAddress: _contractAddress,
            chainId: _chainId,
            interactionType: _interactionType,
            value: _value,
            timestamp: block.timestamp
        }));

        emit InteractionAdded(
            _contractAddress,
            _chainId,
            _interactionType,
            _value
        );
    }

    function getInteractions() external view returns (Interaction[] memory) {
        return interactions;
    }

    function getInteractionCount() external view returns (uint256) {
        return interactions.length;
    }
} 