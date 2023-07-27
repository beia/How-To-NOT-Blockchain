# 1. Import the ABI
import settings
from contract import abi
from web3 import Web3
import pprint

# 2. Create Web3 instance
web3 = Web3(Web3.HTTPProvider(settings.RPC_ENDPOINT))

print(f'Making a call to contract at address: { settings.CONTRACT_ADDRESS }')

# 4. Create contract instance
IoTDevice = web3.eth.contract(address=settings.CONTRACT_ADDRESS, abi=abi)

# 5. Call Contract
events = IoTDevice.events.NewDataPublished().get_logs(fromBlock=settings.CONTRACT_CREATION_BLOCK_NUMBER, toBlock='latest')
data = [x['args']['data'] for x in events]
print(f'The stored data is: \n { pprint.pformat(data) } ')
