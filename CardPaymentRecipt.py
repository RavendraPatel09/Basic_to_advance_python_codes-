# Simple Card Payment Receipt Program

print("CARD PAYMENT RECEIPT")
print("----------------------------")

store_name = "Samarth Mart"
amount = float(input("Enter payment amount (₹): "))
card_last4 = input("Enter last 4 digits of card: ")
transaction_id = input("Enter transaction ID: ")

print("\n------ RECEIPT ------")
print("Store Name      :", store_name)
print("Payment Method  : Card")
print("Card Number     : **** **** ****", card_last4)
print("Transaction ID  :", transaction_id)
print("Amount Paid     : ₹", amount)
print("Payment Status  : Successful")
print("----------------------")
print("Thank you for your payment")