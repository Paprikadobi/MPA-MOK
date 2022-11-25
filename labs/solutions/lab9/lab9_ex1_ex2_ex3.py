#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Raul Casanova-Marques"
__email__ = "casanova@vut.cz"

import hashlib
import json
from time import time


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash="The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.",
                       difficulty=0)

    def new_block(self, previous_hash=None, difficulty=0):
        if difficulty < 0:
            difficulty = 0
        elif difficulty > 8:
            difficulty = 8

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'difficulty': difficulty,
            'transactions': self.pending_transactions,
            'transactions_hash': self.hash(self.pending_transactions),
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
            'nonce': None,
        }

        block['nonce'] = self.proof_of_work(block, difficulty)
        print('block(' + str(len(self.chain) + 1) + '): ' + self.hash(block))

        self.pending_transactions = []
        self.chain.append(block)

        return block

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'id': None,
            'timestamp': time(),
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }

        transaction['id'] = self.hash(transaction)[0:8]

        self.pending_transactions.append(transaction)
        return transaction['id']

    def search_transaction(self, transaction_id):
        for block in self.chain:
            for transaction in block['transactions']:
                if transaction_id == transaction['id']:
                    return block

    def proof_of_work(self, block, difficulty):
        nonce = 0
        num_zeros = 0

        while num_zeros != difficulty:
            block['nonce'] = nonce
            challenge = self.hash(block)
            num_zeros = challenge[::-1].count('0', 0, difficulty)
            if num_zeros == difficulty:
                break
            nonce += 1

        return nonce

    @staticmethod
    def hash(data):
        string_object = json.dumps(data, sort_keys=True)
        data_string = string_object.encode()

        raw_hash = hashlib.sha256(data_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash


def main():
    blockchain = Blockchain()

    t0 = blockchain.new_transaction("Satoshi", "Mike", '5 MOK')
    t1 = blockchain.new_transaction("Mike", "Satoshi", '1 MOK')
    t2 = blockchain.new_transaction("Satoshi", "Hal Finney", '5 MOK')
    blockchain.new_block(difficulty=4)

    t3 = blockchain.new_transaction("Mike", "Alice", '1 MOK')
    t4 = blockchain.new_transaction("Alice", "Bob", '0.5 MOK')
    t5 = blockchain.new_transaction("Bob", "Mike", '0.5 MOK')
    blockchain.new_block(difficulty=5)

    print("[+] Genesis block:", blockchain.chain)

    block = blockchain.search_transaction(t1)
    print("[!] Transaction", t1, "found in block", block['index'])
    block = blockchain.search_transaction(t4)
    print("[!] Transaction", t4, "found in block", block['index'])


if __name__ == '__main__':
    main()
