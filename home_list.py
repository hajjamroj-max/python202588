from functools import reduce

# Original home list
Home_list = [
    {"address": "tehran", "area": 200, "price": 200, "distribution": "parking , elevator , warehouse"},
    {"address": "esfahan", "area": 20, "price": 20, "distribution": "parking"},
    {"address": "gome", "area": 100, "price": 2000, "distribution": "parking , elevator"},
    {"address": "shiraz", "area": 150, "price": 200, "distribution": "parking , elevator , warehouse"}
]

def has_parking(home):
    """Check if the home has parking"""
    return "parking" in home["distribution"]

def get_address(home):
    """Extract address for sorting"""
    return home["address"]

def get_price(home):
    """Extract price"""
    return home["price"]

def sum_prices(total, home):
    """Sum prices for reduce function"""
    return total + home["price"]

def format_home_info(home):
    """Format home information"""
    return f"Address: {home['address']}, Area: {home['area']}m², Price: {home['price']}, Features: {home['distribution']}"

# 1. Filter homes that have parking
homes_with_parking = list(filter(has_parking, Home_list))

# 2. Sort alphabetically by address
sorted_homes = sorted(homes_with_parking, key=get_address)

# 3. Calculate total price
total_price = reduce(sum_prices, homes_with_parking, 0)

# 4. Format information for display
formatted_info = list(map(format_home_info, sorted_homes))

# Display results
print("Homes with parking (sorted alphabetically):")
print("=" * 80)

for i, home_info in enumerate(formatted_info, 1):
    print(f"{i}. {home_info}")

print("=" * 80)
print(f"Total price of homes with parking: {total_price}")
print(f"Number of homes with parking: {len(homes_with_parking)}")
print(f"Average price: {total_price / len(homes_with_parking) if homes_with_parking else 0:.1f}")

# Detailed display with f-string
print("\n" + "="*80)
print("Detailed display with f-string:")
print("="*80)

for i, home in enumerate(sorted_homes, 1):
    print(f"""
House number {i}:
Address: {home['address']}
Area: {home['area']} square meters
Price: {home['price']} (currency units)
Features: {home['distribution']}
{'='*50}""")

print(f"\nTotal price of homes with parking: {total_price}")

# Display additional statistics
print(f"\nStatistics:")
print(f"   Total number of homes: {len(Home_list)}")
print(f"   Homes with parking: {len(homes_with_parking)}")
print(f"   Percentage of homes with parking: {(len(homes_with_parking)/len(Home_list)*100):.1f}%")
print(f"   Most expensive home with parking: {max(map(get_price, homes_with_parking))}")
print(f"   Cheapest home with parking: {min(map(get_price, homes_with_parking))}")