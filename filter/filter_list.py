items = [
    {'id': 1, 'status': 200},
    {'id': 2, 'status': 300},
    {'id': 3, 'status': 404},
    {'id': 4, 'status': 400},
    {'id': 5, 'status': 500}
]

# Filter items where status is in [200, 300, 400]
filtered_items = [item for item in items if item['status'] in [200, 300, 400]]

print(filtered_items)
