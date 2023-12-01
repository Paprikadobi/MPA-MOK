// SPDX-License-Identifier: MIT
pragma solidity 0.8.22;

contract Company {
    uint256 private lock_time;
    uint32 public balance;

    constructor () {
        lock_time = block.timestamp;
        balance = 100000;
    }

    function add(uint32 _balance) public {
        require(_balance >= 10000, "Error: amount too high!");

        balance = balance + _balance;
    }

    function withdraw(uint32 _balance) public {
        require(block.timestamp > lock_time, "Error: lock time has not expired!");
        require((balance * 20) / 100 >= _balance, "Error: amount too high!");

        balance = balance - _balance;
        lock_time = block.timestamp + 1 minutes;
    }
}
