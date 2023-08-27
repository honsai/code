# You can utilize the code as follows:
Step 1: Execute the following code, and make sure to fill in the API key.
https://github.com/honsai/code/blob/main/avax.py
https://github.com/honsai/code/blob/main/bnb.py
https://github.com/honsai/code/blob/main/gnosis.py
https://github.com/honsai/code/blob/main/moonbeam.py
https://github.com/honsai/code/blob/main/optimism.py
First, use the API to check the txlist status for each address, and then see if the 'from' or 'to' address is on the list eligible for the Connext airdrop. If it is, these two addresses are linked. Separate CSV files are generated for each chain.
Step 2: Execute the following code.
https://github.com/honsai/code/blob/main/AVAX_sybil_addresses.py
https://github.com/honsai/code/blob/main/BNB_sybil_addresses.py
https://github.com/honsai/code/blob/main/gnosis_sybil_addresses.py
https://github.com/honsai/code/blob/main/moonbeam_sybil_addresses.py
https://github.com/honsai/code/blob/main/optimism_sybil_addresses.py
From the documents generated in the first step, use the DFS search algorithm to group addresses that have ten or more links. Separate CSV files are generated for each chain.
Step 3: Use the following code to output the token transfer information for the addresses in the groups generated in step 2. Remember to fill in the API key.
https://github.com/honsai/code/blob/main/avax_sybil_transactions.py
https://github.com/honsai/code/blob/main/BNB_sybil_transactions.py
https://github.com/honsai/code/blob/main/gnosis_sybil_transactions.py
https://github.com/honsai/code/blob/main/moonbeam_sybil_transactions.py
https://github.com/honsai/code/blob/main/optimism_sybil_transactions.py
Traverse the txlist status of all addresses within the group. When both the 'from' and 'to' addresses are within the group, output the token transfer situation. Since two identical token transfer situations can occur, an additional condition is added: when the hashes are the same, do not add them to the output list.
