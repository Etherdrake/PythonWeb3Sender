from eth_utils.conversions import to_hex
from web3 import Web3

# ftm = Web3(Web3.HTTPProvider('https://rpcapi.fantom.network')) # Mainnnet
ftm = Web3(Web3.HTTPProvider('https://rpc.testnet.fantom.network/')) # Testnet 

account_1 = "PUBLIC ADDRESS OF SENDER "
private_key1 = "PRIVATE KEY OF SENDER ACCOUNT "

account_2 = "PUBLIC ADDRESS OF RECEIVER"


# ftm = Web3(Web3.HTTPProvider('https://rpcapi.fantom.network')) # Mainnnet

ftm = Web3(Web3.HTTPProvider('https://rpc.testnet.fantom.network/')) # Testnet 

is_connected = ftm.isConnected()

print("Connection to Fantom Opera Testnet: " + str(is_connected))

# Get the nonce. Prevents one from sending the transaction twice
nonce = ftm.eth.getTransactionCount(account_1)

# Build a transaction in a dictionary
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': ftm.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': ftm.toWei('50', 'gwei'),
    'chainId': 0xfa2
}

#sign the transaction
signed_tx = ftm.eth.account.sign_transaction(tx, private_key1)

#send transaction
tx_hash = ftm.eth.sendRawTransaction(signed_tx.rawTransaction)

#get transaction hash
print(ftm.toHex(tx_hash))

balance_account_1 = ftm.eth.get_balance(account_1) / 1000000000000000000
balance_account_2 = ftm.eth.get_balance(account_2) / 1000000000000000000

print(f"{balance_account_1} FTM")
print(f"{balance_account_2} FTM")

