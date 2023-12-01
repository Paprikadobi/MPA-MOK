// SPDX-License-Identifier: MIT
pragma solidity 0.8.22;

contract Greetings {
    string private name;

    constructor () {
        name = "Alice";
    }

    function store(string calldata _name) public {
        require(bytes(_name).length > 0, "Error: the name cannot be empty!");

        name = _name;
    }

    function retrieve() public view returns (string memory) {
        return name;
    }

    function greetings() public view returns (string memory) {
        return string(abi.encodePacked("Hello ", name, "!"));
    }
}
