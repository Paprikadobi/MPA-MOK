// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.22;

contract Ownership {
    address private owner;

    event OwnerSet(address indexed oldOwner, address indexed newOwner);

    constructor() {
        owner = msg.sender;
        emit OwnerSet(address(0), owner);
    }

    function getOwner() external view returns (address) {
        return owner;
    }

    function changeOwner(address _owner) public {
        require(msg.sender == owner, "Error: caller is not the owner!");

        owner = _owner;
        emit OwnerSet(owner, _owner);
    }
}
