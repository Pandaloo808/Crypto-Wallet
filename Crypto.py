from web3 import Web3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("My Crypto Banking Appp")

root.configure(bg="white")

infura_url='https://sepolia.infura.io/v3/9dd40f74e73c434b9fc6cb1efa25f551'

web3_infura_connection=Web3(Web3.HTTPProvider(infura_url))

frame=Frame(root, bg='white', padx=5, pady=5)
logo=ImageTk.PhotoImage(Image.open('logo.jpeg'))
logolabel=Label(root, image=logo)
logolabel.pack(side='top')

Label(frame, text="Account Number 1: ", fg='black', bg='white').grid(row=0, column=0, pady=10)

Label(frame, text="Account Number 2: ", fg='black', bg='white').grid(row=1, column=0, pady=10)

Label(frame, text="Private Key: ", fg='black', bg='white').grid(row=2, column=0, pady=10)

Label(frame, text="ETH: ", fg='black', bg='white').grid(row=3, column=0, pady=10)

Label(frame, text="Gas Price (GWEI): ", fg='black', bg='white').grid(row=4, column=0, pady=10)

Label(frame, text="Gas Limit (GWEI): ", fg='black', bg='white').grid(row=5, column=0, pady=10)

account1=Entry(frame)

account2=Entry(frame)

private_key=Entry(frame)

amount=Entry(frame)

gas_price=Entry(frame)

gas_limit=Entry(frame)

account1.grid(row=0, column=1, pady=10, padx=20)
account2.grid(row=1, column=1, pady=10, padx=20)
private_key.grid(row=2, column=1, pady=10, padx=20)
amount.grid(row=3, column=1, pady=10, padx=20)
gas_price.grid(row=4, column=1, pady=10, padx=20)
gas_limit.grid(row=5, column=1, pady=10, padx=20)

def sendETH():
	account1_id=account1.get()
	account2_id-account2.get()
	key=private_key.get()
	eth_amount=amount.get()
	gas_fee=gas_price.get()
	Gaslimit=gas_limit.get()

	nonce=web3.infura_connection.eth.get_transaction_count(account1_id)
	transaction={
	'nonce': nonce,
	'to':account2_id,
	'value': web3_infura_connection.to_wei(eth.amount, 'ether'),
	'gas': int(Gaslimit),
	'gasPrice': web3_infura_connection.to_wei(gas_fee,'gwei')
	}

	signed_transaction=web3_infura_connection.eth.account.sign_transaction(transaction,key)
	transaction_hash=web3_infura_connection.eth.send_raw_transaction(signed_transaction.rawTransaction)

	print("Your transaction is successful. Your Transaction ID is: ", transaction_hash.hex())
	messagebox.showinfo("Transaction status!", "Transaction Successful! Verify your metamask wallet !-!")

frame.pack()

btn=Button(root,text="TRANSFER ETH", command=sendETH, highlightbackground='white',width=15)
tranfer_eth.pack()

root.mainloop()

 