from blockchain import Blockchain

block_one_transactions = {"sender":"Dhiren", "receiver": "Anurag", "amount":"2090"}
block_two_transactions = {"sender": "Ashray", "receiver":"Dhiren", "amount":"1500"}
block_three_transactions = {"sender":"Dhiren", "receiver":"Cook", "amount":"1500"}
fake_transactions = {"sender": "Anurag", "receiver":"Dhiren", "amount":"2500"}

local_blockchain = Blockchain()

local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
local_blockchain.print_blocks()
#local_blockchain.chain[2].transactions = fake_transactions
#local_blockchain.validate_chain()
