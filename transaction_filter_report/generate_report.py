# Sample transaction data
data = [
    ("ref1", "clientA", "txnTypeA", "03/03/2025", "N"),
    ("ref2", "clientB", "txnTypeA", "03/03/2025", "N"),
    ("ref3", "clientA", "txnTypeA", "03/03/2025", "Y"),
    ("ref4", "clientA", "txnTypeA", "03/03/2025", "N"),
    ("ref5", "clientA", "txnTypeB", "03/03/2025", "N"),
]

# Map clientname and transaction_type to a flag indicating if any transaction has cancellation_flag = 'Y'
transaction_map = {}
for txn in data:
    key = (txn[1], txn[2])
    if key not in transaction_map:
        transaction_map[key] = False
    if txn[4] == "Y":
        transaction_map[key] = True

# Find clientname and transaction_type with any cancellation_flag = 'Y'
cancelled_transactions = {key for key, has_cancellation in transaction_map.items() if has_cancellation}

# Filtering transactions based on cancellation criteria
filtered_transactions = [txn[0] for txn in data if (txn[1], txn[2]) in cancelled_transactions]

# Display report
print("Filtered Transactions:")
for ref in filtered_transactions:
    print(ref)

# Save report to CSV
with open("filtered_transactions.csv", "w") as file:
    file.write("transaction_reference\n")
    for ref in filtered_transactions:
        file.write(f"{ref}\n")
