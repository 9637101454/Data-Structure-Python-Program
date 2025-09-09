def linear_search(customer_ids, target_id):
    """Performs linear search to find the target_id in customer_ids list."""
    for i, cid in enumerate(customer_ids):
        if cid == target_id:
            return True  # ID found
    return False  # ID not found


def binary_search(customer_ids, target_id):
    """Performs binary search to find the target_id in sorted customer_ids list."""
    low = 0
    high = len(customer_ids) - 1

    while low <= high:
        mid = (low + high) // 2
        if customer_ids[mid] == target_id:
            return True  # ID found
        elif customer_ids[mid] < target_id:
            low = mid + 1
        else:
            high = mid - 1

    return False  # ID not found


# Example usage
customer_ids = [102, 205, 301, 410, 512, 620, 733]  # Example sorted list
target_id = 410  # ID you want to search for

print("Linear Search Result:")
if linear_search(customer_ids, target_id):
    print(f"Customer ID {target_id} exists in the list.")
else:
    print(f"Customer ID {target_id} does NOT exist in the list.")

print("\nBinary Search Result:")
# Make sure the list is sorted before binary search
customer_ids_sorted = sorted(customer_ids)
if binary_search(customer_ids_sorted, target_id):
    print(f"Customer ID {target_id} exists in the list.")
else:
    print(f"Customer ID {target_id} does NOT exist in the list.")