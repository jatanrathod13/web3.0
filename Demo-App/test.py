from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/753accb6f0cc463b8c1b353b0a89961a"
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
print(web3.eth.blockNumber)
account = "0x90e63c3d53E0Ea496845b7a03ec7548B70014A91"
balance = web3.eth.getBalance("0x90e63c3d53E0Ea496845b7a03ec7548B70014A91")
print(web3.fromWei(balance, "ether"))

