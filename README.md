# What is this?

This is a demo 101 Smart Contract used to store data from a virtual IoT Device. All the aspects are demonstrated using Solidity, Web3, and Python.

- Step 1 checks the ETH balance of the used Wallet
- Step 2 compiles the Smart Contact;
- Step 3 deploys the Smart Contact;
- Step 4 simulates an IoT device trying to push data every 10 seconds;
- Step 5 shows that the data is readable from the chain.

The configurable parameters are refactored in `settings.py`, while `contract.py` is a Python interface to read important details from the compiled smart contract (which will be saved, in step 3, as `IoTDevice.json`).

The presented Smart Contact is a **draft**.

**None** of the Solidity / Python snippets, nor the idea (of using on-chain storage for IoT data) presented should be considered good-practice. 


# Copyright and other disclaimers

The presented content is based on the tutorial found at [https://docs.moonbeam.network](https://docs.moonbeam.network/builders/build/eth-api/libraries/web3py/ "https://docs.moonbeam.network") and it is meant for Beia interns to visualize how a public ETH-like blockchain works by the analogy of storing IoT data in a database.
