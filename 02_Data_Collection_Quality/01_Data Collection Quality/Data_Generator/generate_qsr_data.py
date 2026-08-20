"""
================================================================================
Quick Service Restaurant (QSR) Business Analytics — Raw Data Generator
================================================================================
Generates 15 raw, intentionally-imperfect CSV tables for a fictional Indian
QSR chain, to be used as the source data for a SQL Server based portfolio
project (data profiling, cleaning, and analysis).

Author: Generated for portfolio project use
Note:   All data is 100% fictional. No real company, customer, or employee
        information is used anywhere in this script.

Usage:
    pip install pandas numpy faker
    python generate_qsr_data.py

Output:
    ./raw_data/*.csv  (15 files)
================================================================================
"""

import os
import random
import string
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from faker import Faker

# ==============================================================================
# 0. CONFIGURATION
# ==============================================================================

SEED = 42
random.seed(SEED)
np.random.seed(SEED)

fake = Faker("en_IN")
Faker.seed(SEED)

OUTPUT_DIR = "raw_data"

# Reference "today" for the dataset — keeps the generated data reproducible
# regardless of when the script is actually executed.
TODAY = datetime(2026, 8, 20)
ORDER_HISTORY_YEARS = 2.7
ORDER_START_DATE = TODAY - timedelta(days=int(365 * ORDER_HISTORY_YEARS))

# Target volumes (kept within the ranges requested in the spec)
N_BRANCHES = 20
N_BRANCHES_CLOSED = 4
N_CUSTOMERS = 12500
N_EMPLOYEES_TARGET = 700
N_PRODUCTS = 70
N_INGREDIENTS = 65
N_ORDERS = 42000

DIRTY_FRACTION_LOW = 0.02      # ~2% — subtle issues
DIRTY_FRACTION_MED = 0.05      # ~5% — moderate issues
DIRTY_FRACTION_HIGH = 0.08     # ~8% — more visible issues


# ==============================================================================
# 1. REFERENCE / LOOKUP DATA
# ==============================================================================

INDIAN_CITY_STATE = [
    ("Mumbai", "Maharashtra"), ("Pune", "Maharashtra"), ("Nagpur", "Maharashtra"),
    ("Thane", "Maharashtra"), ("Nashik", "Maharashtra"),
    ("New Delhi", "Delhi"), ("Gurugram", "Haryana"), ("Noida", "Uttar Pradesh"),
    ("Bengaluru", "Karnataka"), ("Mysuru", "Karnataka"),
    ("Hyderabad", "Telangana"), ("Chennai", "Tamil Nadu"), ("Coimbatore", "Tamil Nadu"),
    ("Kolkata", "West Bengal"), ("Ahmedabad", "Gujarat"), ("Surat", "Gujarat"),
    ("Vadodara", "Gujarat"), ("Jaipur", "Rajasthan"), ("Udaipur", "Rajasthan"),
    ("Lucknow", "Uttar Pradesh"), ("Kanpur", "Uttar Pradesh"), ("Chandigarh", "Chandigarh"),
    ("Kochi", "Kerala"), ("Thiruvananthapuram", "Kerala"), ("Indore", "Madhya Pradesh"),
    ("Bhopal", "Madhya Pradesh"), ("Patna", "Bihar"), ("Visakhapatnam", "Andhra Pradesh"),
    ("Bhubaneswar", "Odisha"), ("Guwahati", "Assam"),
]

LOCATION_TYPES = ["Mall", "High Street", "Business District", "Residential Area", "Transit Hub"]

EMPLOYEE_ROLES = [
    "Branch Manager", "Assistant Manager", "Shift Manager",
    "Kitchen Staff", "Cashier", "Delivery Coordinator", "Cleaner",
]
EMPLOYMENT_STATUSES = ["Active", "Resigned", "Terminated", "On Leave"]
EMPLOYMENT_STATUS_WEIGHTS = [0.78, 0.12, 0.05, 0.05]

PRODUCT_CATALOG = {
    "Pizza": [
        "Margherita Pizza", "Farmhouse Pizza", "Peppy Paneer Pizza", "Chicken Tikka Pizza",
        "Pepperoni Pizza", "Veggie Supreme Pizza", "Cheese Burst Pizza", "Tandoori Paneer Pizza",
        "Mexican Wave Pizza", "Chicken Sausage Pizza",
    ],
    "Burger": [
        "Classic Veg Burger", "Aloo Tikki Burger", "Paneer Tikka Burger", "Chicken Zinger Burger",
        "Grilled Chicken Burger", "Double Patty Burger", "Spicy Chicken Burger", "Mexican Bean Burger",
    ],
    "Side": [
        "French Fries", "Peri Peri Fries", "Cheesy Garlic Bread", "Chicken Wings",
        "Veg Nuggets", "Chicken Popcorn", "Onion Rings", "Potato Wedges", "Paneer Nuggets",
    ],
    "Beverage": [
        "Cola (Regular)", "Cola (Diet)", "Lemon Iced Tea", "Fresh Lime Soda", "Cold Coffee",
        "Masala Chaas", "Mango Shake", "Packaged Mineral Water", "Orange Juice",
    ],
    "Dessert": [
        "Choco Lava Cake", "Butterscotch Sundae", "Brownie with Ice Cream", "Gulab Jamun Fusion",
        "Vanilla Ice Cream Cup", "Chocolate Chip Cookie",
    ],
    "Combo": [
        "Pizza Meal Combo", "Burger Meal Combo", "Family Feast Combo", "Kids Meal Combo",
        "Duo Pizza Combo", "Snack Box Combo",
    ],
}

INGREDIENT_LIST = [
    ("Mozzarella Cheese", "Dairy", "KG"), ("Processed Cheese Slice", "Dairy", "Piece"),
    ("Refined Flour (Maida)", "Bakery", "KG"), ("Whole Wheat Flour", "Bakery", "KG"),
    ("Pizza Base", "Bakery", "Piece"), ("Burger Bun", "Bakery", "Piece"),
    ("Tomato", "Vegetable", "KG"), ("Onion", "Vegetable", "KG"), ("Capsicum", "Vegetable", "KG"),
    ("Jalapeno", "Vegetable", "KG"), ("Sweet Corn", "Vegetable", "KG"), ("Mushroom", "Vegetable", "KG"),
    ("Paneer", "Dairy", "KG"), ("Chicken Breast", "Meat", "KG"), ("Chicken Sausage", "Meat", "KG"),
    ("Pepperoni", "Meat", "KG"), ("Minced Chicken", "Meat", "KG"), ("Potato", "Vegetable", "KG"),
    ("Pizza Sauce", "Sauce", "Liter"), ("Tomato Ketchup", "Sauce", "Liter"), ("Mayonnaise", "Sauce", "Liter"),
    ("Peri Peri Seasoning", "Seasoning", "Gram"), ("Oregano", "Seasoning", "Gram"),
    ("Chilli Flakes", "Seasoning", "Gram"), ("Cooking Oil", "Oil", "Liter"), ("Butter", "Dairy", "KG"),
    ("Salt", "Seasoning", "KG"), ("Sugar", "Seasoning", "KG"), ("Cola Syrup", "Beverage", "Liter"),
    ("Lemon", "Vegetable", "KG"), ("Mint Leaves", "Vegetable", "Gram"), ("Milk", "Dairy", "Liter"),
    ("Coffee Powder", "Beverage", "Gram"), ("Ice Cream Mix", "Dairy", "Liter"), ("Chocolate Sauce", "Sauce", "Liter"),
    ("Cookie Dough", "Bakery", "KG"), ("Brownie Mix", "Bakery", "KG"), ("Gulab Jamun Mix", "Bakery", "KG"),
    ("Bread Crumbs", "Bakery", "KG"), ("Garlic", "Vegetable", "KG"), ("Ginger", "Vegetable", "KG"),
    ("Coriander Leaves", "Vegetable", "Gram"), ("Green Chilli", "Vegetable", "KG"),
    ("Curd", "Dairy", "KG"), ("Tandoori Masala", "Seasoning", "Gram"), ("Red Chilli Powder", "Seasoning", "Gram"),
    ("Turmeric Powder", "Seasoning", "Gram"), ("Garam Masala", "Seasoning", "Gram"),
    ("Vegetable Nuggets Mix", "Frozen", "KG"), ("Chicken Wings (Raw)", "Meat", "KG"),
    ("Onion Rings Batter", "Bakery", "KG"), ("Potato Wedges (Frozen)", "Frozen", "KG"),
    ("Packaged Drinking Water", "Beverage", "Liter"), ("Orange Concentrate", "Beverage", "Liter"),
    ("Mango Pulp", "Beverage", "KG"), ("Iced Tea Powder", "Beverage", "Gram"), ("Vanilla Essence", "Seasoning", "Liter"),
    ("Cornflour", "Bakery", "KG"), ("Baking Powder", "Bakery", "Gram"), ("Cheese Spread", "Dairy", "KG"),
    ("Napkins/Packaging Material", "Packaging", "Piece"), ("Disposable Cutlery", "Packaging", "Piece"),
    ("Pizza Box (Medium)", "Packaging", "Piece"), ("Burger Wrap", "Packaging", "Piece"),
    ("Cold Drink Cup", "Packaging", "Piece"),
]

DELIVERY_PARTNERS = ["Own Fleet", "Swiggy Genie", "Dunzo", "Porter", "Shadowfax"]

WASTAGE_REASONS = ["Expired", "Spoilage", "Preparation Error", "Overproduction", "Storage Issue", "Quality Issue"]
COST_CATEGORIES = ["Rent", "Electricity", "Salaries", "Maintenance", "Delivery", "Cleaning", "Repairs", "Miscellaneous"]
REFUND_REASONS = ["Incorrect Order", "Poor Food Quality", "Delivery Delay", "Missing Item", "Payment Issue"]
REFUND_STATUSES = ["Requested", "Approved", "Rejected", "Processed"]

VIOLATION_CATEGORIES = [
    "Food Storage Temperature", "Pest Control", "Staff Hygiene", "Kitchen Cleanliness",
    "Expired Ingredient Usage", "Cross Contamination", "Waste Disposal", "Documentation Lapse",
]
VIOLATION_SEVERITIES = ["Low", "Medium", "High", "Critical"]
INSPECTION_TYPES = ["Routine", "Surprise", "Follow-up", "Complaint-Triggered"]


# ==============================================================================
# 2. GENERIC DIRTY-DATA HELPERS
# ==============================================================================

def _rand_idx(n_rows, frac, rng=None):
    """Return a random unique set of row positions for a given fraction."""
    rng = rng or random
    k = int(n_rows * frac)
    if k <= 0 or n_rows == 0:
        return []
    return rng.sample(range(n_rows), min(k, n_rows))


def introduce_nulls(df, col, frac):
    idx = _rand_idx(len(df), frac)
    df.loc[idx, col] = np.nan
    return df


def introduce_case_inconsistency(df, col, frac):
    """Randomly upper/lower-case a fraction of a text column's values."""
    idx = _rand_idx(len(df), frac)
    for i in idx:
        val = df.at[i, col]
        if pd.isna(val):
            continue
        choice = random.choice(["upper", "lower", "title"])
        df.at[i, col] = str(val).upper() if choice == "upper" else (
            str(val).lower() if choice == "lower" else str(val).title()
        )
    return df


def introduce_extra_spaces(df, col, frac):
    idx = _rand_idx(len(df), frac)
    for i in idx:
        val = df.at[i, col]
        if pd.isna(val):
            continue
        style = random.choice(["leading", "trailing", "both", "double_internal"])
        s = str(val)
        if style == "leading":
            s = "  " + s
        elif style == "trailing":
            s = s + "   "
        elif style == "both":
            s = "  " + s + "  "
        else:
            s = s.replace(" ", "  ", 1)
        df.at[i, col] = s
    return df


def introduce_duplicate_rows(df, frac):
    n = int(len(df) * frac)
    if n <= 0:
        return df
    dup_rows = df.sample(n=n, random_state=random.randint(1, 999999))
    return pd.concat([df, dup_rows], ignore_index=True)


def introduce_duplicate_values(df, col, frac):
    """Force some rows to reuse another row's value in `col` (e.g. duplicate emails)."""
    idx = _rand_idx(len(df), frac)
    if not idx:
        return df
    pool = df[col].dropna().tolist()
    if not pool:
        return df
    for i in idx:
        df.at[i, col] = random.choice(pool)
    return df


def introduce_negative_values(df, col, frac):
    idx = _rand_idx(len(df), frac)
    for i in idx:
        val = df.at[i, col]
        if pd.isna(val):
            continue
        df.at[i, col] = -abs(val)
    return df


def introduce_outliers(df, col, frac, multiplier=8):
    idx = _rand_idx(len(df), frac)
    for i in idx:
        val = df.at[i, col]
        if pd.isna(val):
            continue
        df.at[i, col] = round(val * multiplier, 2)
    return df


def introduce_label_variants(df, col, variant_map, frac):
    """variant_map: {canonical_value: [list of dirty variants]}"""
    idx = _rand_idx(len(df), frac)
    for i in idx:
        val = df.at[i, col]
        if val in variant_map:
            df.at[i, col] = random.choice(variant_map[col_variant_pick(val, variant_map)])
    return df


def col_variant_pick(val, variant_map):
    return val


def swap_label_case_variants(df, col, frac):
    """Generic case-scrambler used to mimic 'Completed/completed/COMPLETED' style issues."""
    return introduce_case_inconsistency(df, col, frac)


def make_unique_gov_id(existing):
    while True:
        gid = "GOV" + "".join(random.choices(string.digits, k=9))
        if gid not in existing:
            existing.add(gid)
            return gid


def fake_email(first, last, domain_pool=("gmail.com", "yahoo.com", "outlook.com", "rediffmail.com")):
    last = last or "user"
    tag = random.randint(1, 9999)
    return f"{first}.{last}{tag}@{random.choice(domain_pool)}".lower().replace(" ", "")


def fake_phone():
    return "9" + "".join(random.choices(string.digits, k=1)) + "".join(random.choices(string.digits, k=8))


# ==============================================================================
# 3. TABLE GENERATORS
# ==============================================================================

def generate_branches():
    print("Generating Branches...")
    cities = random.sample(INDIAN_CITY_STATE, N_BRANCHES) if len(INDIAN_CITY_STATE) >= N_BRANCHES \
        else [random.choice(INDIAN_CITY_STATE) for _ in range(N_BRANCHES)]

    rows = []
    closure_dates = {}  # internal use only, not written to CSV (not part of schema)
    closed_branch_ids = set(random.sample(range(1, N_BRANCHES + 1), N_BRANCHES_CLOSED))

    for i in range(1, N_BRANCHES + 1):
        city, state = cities[i - 1]
        opening_date = fake.date_between(start_date=datetime(2016, 1, 1), end_date=datetime(2022, 6, 1))
        status = "Closed" if i in closed_branch_ids else "Active"
        rows.append({
            "BranchID": i,
            "BranchName": f"QuickBite {city} {random.choice(['Central','Square','Plaza','Point','Junction'])}",
            "City": city,
            "State": state,
            "LocationType": random.choice(LOCATION_TYPES),
            "OpeningDate": opening_date,
            "BranchStatus": status,
        })
        if status == "Closed":
            # closure happens sometime well within the order-history window
            closure_dates[i] = fake.date_between(
                start_date=ORDER_START_DATE + timedelta(days=180),
                end_date=TODAY - timedelta(days=120),
            )

    df = pd.DataFrame(rows)
    return df, closed_branch_ids, closure_dates


def generate_customers(n):
    print(f"Generating {n} Customers...")
    rows = []
    for i in range(1, n + 1):
        gender = np.random.choice(["Male", "Female", "Transgender"], p=[0.49, 0.49, 0.02])
        first = fake.first_name_male() if gender == "Male" else (
            fake.first_name_female() if gender == "Female" else fake.first_name()
        )
        last = fake.last_name()
        middle = fake.first_name() if random.random() > 0.35 else None
        # ~4% genuinely missing last name, ~6% missing middle beyond the above
        if random.random() < 0.04:
            last = None
        city, state = random.choice(INDIAN_CITY_STATE)
        dob = fake.date_of_birth(minimum_age=16, maximum_age=70)
        join_date = fake.date_between(start_date=ORDER_START_DATE - timedelta(days=200), end_date=TODAY)
        rows.append({
            "CustomerID": i,
            "FirstName": first,
            "MiddleName": middle,
            "LastName": last,
            "DOB": dob,
            "Email": fake_email(first, last or "cust"),
            "Phone": fake_phone(),
            "JoinDate": join_date,
            "Gender": gender,
            "City": city,
            "State": state,
            "LoyaltyStatus": np.random.choice(
                ["Bronze", "Silver", "Gold", "Platinum", "None"], p=[0.35, 0.28, 0.18, 0.07, 0.12]
            ),
        })
    return pd.DataFrame(rows)


def generate_employees(branches_df, target_total):
    print("Generating Employees...")
    rows = []
    emp_id = 1
    gov_ids = set()
    per_branch = max(20, target_total // len(branches_df))

    for _, branch in branches_df.iterrows():
        branch_id = branch["BranchID"]
        n_staff = random.randint(per_branch - 6, per_branch + 10)

        # 1. Branch Manager (top of hierarchy for this branch)
        bm_first, bm_last = fake.first_name(), fake.last_name()
        branch_manager_id = emp_id
        rows.append(_employee_row(emp_id, branch_id, bm_first, bm_last, "Branch Manager",
                                   manager_id=None, gov_ids=gov_ids))
        emp_id += 1

        # 2. Assistant Managers (report to Branch Manager)
        n_asst = random.randint(1, 2)
        asst_ids = []
        for _ in range(n_asst):
            f, l = fake.first_name(), fake.last_name()
            rows.append(_employee_row(emp_id, branch_id, f, l, "Assistant Manager",
                                       manager_id=branch_manager_id, gov_ids=gov_ids))
            asst_ids.append(emp_id)
            emp_id += 1

        # 3. Shift Managers (report to an Assistant Manager)
        n_shift = random.randint(2, 4)
        shift_ids = []
        for _ in range(n_shift):
            f, l = fake.first_name(), fake.last_name()
            mgr = random.choice(asst_ids)
            rows.append(_employee_row(emp_id, branch_id, f, l, "Shift Manager",
                                       manager_id=mgr, gov_ids=gov_ids))
            shift_ids.append(emp_id)
            emp_id += 1

        # 4. Remaining staff (report to a Shift Manager or Assistant Manager)
        remaining = max(n_staff - (1 + n_asst + n_shift), 10)
        staff_roles = ["Kitchen Staff", "Cashier", "Delivery Coordinator", "Cleaner"]
        supervisor_pool = shift_ids + asst_ids
        for _ in range(remaining):
            f, l = fake.first_name(), fake.last_name()
            role = random.choices(staff_roles, weights=[0.4, 0.25, 0.2, 0.15])[0]
            rows.append(_employee_row(emp_id, branch_id, f, l, role,
                                       manager_id=random.choice(supervisor_pool), gov_ids=gov_ids))
            emp_id += 1

    return pd.DataFrame(rows)


def _employee_row(emp_id, branch_id, first, last, role, manager_id, gov_ids):
    hire_date = fake.date_between(start_date=datetime(2016, 1, 1), end_date=TODAY - timedelta(days=10))
    salary_bands = {
        "Branch Manager": (55000, 90000),
        "Assistant Manager": (38000, 55000),
        "Shift Manager": (25000, 38000),
        "Kitchen Staff": (14000, 22000),
        "Cashier": (13000, 20000),
        "Delivery Coordinator": (14000, 21000),
        "Cleaner": (11000, 16000),
    }
    lo, hi = salary_bands[role]
    middle = fake.first_name() if random.random() > 0.5 else None
    return {
        "EmployeeID": emp_id,
        "BranchID": branch_id,
        "FirstName": first,
        "MiddleName": middle,
        "LastName": last,
        "GovernmentID": make_unique_gov_id(gov_ids),
        "Role": role,
        "HireDate": hire_date,
        "EmploymentStatus": np.random.choice(EMPLOYMENT_STATUSES, p=EMPLOYMENT_STATUS_WEIGHTS),
        "ManagerID": manager_id,
        "Salary": random.randint(lo, hi),
        "Phone": fake_phone(),
        "Email": fake_email(first, last),
    }


def generate_products():
    print("Generating Products...")
    rows = []
    pid = 1
    for category, items in PRODUCT_CATALOG.items():
        for name in items:
            if category == "Combo":
                ptype = "Veg" if "Kids" in name or random.random() > 0.5 else "Non-Veg"
                cost = round(random.uniform(90, 180), 2)
                sell = round(cost * random.uniform(1.5, 2.1), 2)
            elif category == "Beverage":
                ptype = "Beverage"
                cost = round(random.uniform(8, 40), 2)
                sell = round(cost * random.uniform(2.0, 3.5), 2)
            elif category == "Dessert":
                ptype = "Dessert"
                cost = round(random.uniform(15, 45), 2)
                sell = round(cost * random.uniform(2.0, 3.0), 2)
            else:
                ptype = "Non-Veg" if any(k in name for k in
                                          ["Chicken", "Pepperoni", "Sausage"]) else "Veg"
                cost = round(random.uniform(30, 110), 2)
                sell = round(cost * random.uniform(1.8, 2.6), 2)

            rows.append({
                "ProductID": pid,
                "ProductName": name,
                "Category": category,
                "ProductType": ptype,
                "CostPrice": cost,
                "SellingPrice": sell,
                "ProductStatus": np.random.choice(["Active", "Discontinued"], p=[0.9, 0.1]),
                "LaunchDate": fake.date_between(start_date=datetime(2016, 1, 1), end_date=TODAY - timedelta(days=30)),
            })
            pid += 1

    # top up with a few extra generic variants to reach N_PRODUCTS
    while len(rows) < N_PRODUCTS:
        base = random.choice(rows)
        pid += 1
        variant = dict(base)
        variant["ProductID"] = pid
        variant["ProductName"] = base["ProductName"] + " (Large)"
        variant["CostPrice"] = round(base["CostPrice"] * 1.3, 2)
        variant["SellingPrice"] = round(base["SellingPrice"] * 1.3, 2)
        rows.append(variant)

    return pd.DataFrame(rows[:max(N_PRODUCTS, len(PRODUCT_CATALOG))])


def generate_ingredients():
    print("Generating Ingredients...")
    rows = []
    shelf_life_by_category = {
        "Dairy": (5, 20), "Bakery": (3, 30), "Vegetable": (4, 14), "Meat": (2, 10),
        "Sauce": (30, 180), "Seasoning": (90, 720), "Oil": (90, 365),
        "Beverage": (60, 365), "Frozen": (60, 270), "Packaging": (365, 1825),
    }
    for i, (name, category, uom) in enumerate(INGREDIENT_LIST[:N_INGREDIENTS], start=1):
        lo, hi = shelf_life_by_category.get(category, (7, 90))
        rows.append({
            "IngredientID": i,
            "IngredientName": name,
            "IngredientCategory": category,
            "UnitOfMeasure": uom,
            "ShelfLifeDays": random.randint(lo, hi),
        })
    return pd.DataFrame(rows)


def generate_product_ingredients(products_df, ingredients_df):
    print("Generating ProductIngredients...")
    rows = []
    ing_ids = ingredients_df["IngredientID"].tolist()
    for _, product in products_df.iterrows():
        n_ing = random.randint(3, 7)
        chosen = random.sample(ing_ids, min(n_ing, len(ing_ids)))
        for ing_id in chosen:
            rows.append({
                "ProductID": product["ProductID"],
                "IngredientID": ing_id,
                "QuantityRequired": round(random.uniform(0.01, 0.6), 3),
            })
    return pd.DataFrame(rows)


def _weighted_order_datetime(active_days, branch_performance_ok):
    """Pick a date/time biased toward weekends and evenings."""
    day_offset = random.randint(0, active_days - 1)
    d = ORDER_START_DATE + timedelta(days=day_offset)
    # bias toward weekends: resample with 55% chance if it's a weekday
    if d.weekday() < 5 and random.random() < 0.35:
        d = d + timedelta(days=(5 - d.weekday()) % 7)
        if (d - ORDER_START_DATE).days >= active_days:
            d = ORDER_START_DATE + timedelta(days=day_offset)

    # bias toward evening hours
    hour = np.random.choice(
        range(10, 23),
        p=_hour_weights(),
    )
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    order_dt = d.replace(hour=int(hour), minute=minute, second=second)
    return order_dt


_HOUR_WEIGHTS_CACHE = None


def _hour_weights():
    global _HOUR_WEIGHTS_CACHE
    if _HOUR_WEIGHTS_CACHE is None:
        hours = list(range(10, 23))
        weights = []
        for h in hours:
            if 12 <= h <= 14:      # lunch bump
                weights.append(3.0)
            elif 18 <= h <= 21:    # dinner peak
                weights.append(4.5)
            else:
                weights.append(1.0)
        total = sum(weights)
        _HOUR_WEIGHTS_CACHE = [w / total for w in weights]
    return _HOUR_WEIGHTS_CACHE


def generate_orders(customers_df, branches_df, employees_df, closed_branch_ids, closure_dates, n_orders):
    print(f"Generating {n_orders} Orders...")
    active_employees = employees_df[employees_df["EmploymentStatus"].isin(["Active", "On Leave"])]
    emp_by_branch = {
        bid: grp["EmployeeID"].tolist()
        for bid, grp in active_employees.groupby("BranchID")
    }
    customer_ids = customers_df["CustomerID"].tolist()

    # branch popularity weights -> some branches perform better than others
    branch_ids = branches_df["BranchID"].tolist()
    branch_weight = {}
    for bid, status in zip(branches_df["BranchID"], branches_df["BranchStatus"]):
        base = np.random.lognormal(mean=0.0, sigma=0.5)
        branch_weight[bid] = base * (0.4 if status == "Closed" else 1.0)
    weight_sum = sum(branch_weight.values())
    branch_probs = [branch_weight[b] / weight_sum for b in branch_ids]

    rows = []
    order_id = 1
    total_days = (TODAY - ORDER_START_DATE).days

    while order_id <= n_orders:
        branch_id = np.random.choice(branch_ids, p=branch_probs)
        order_dt = _weighted_order_datetime(total_days, True)

        if branch_id in closed_branch_ids:
            close_dt = datetime.combine(closure_dates[branch_id], datetime.min.time())
            if order_dt > close_dt:
                continue  # closed branches: no orders after closure

        emp_pool = emp_by_branch.get(branch_id)
        if not emp_pool:
            continue
        employee_id = random.choice(emp_pool)
        customer_id = random.choice(customer_ids)

        order_type = np.random.choice(["Dine-In", "Takeaway", "Delivery"], p=[0.38, 0.27, 0.35])
        status = np.random.choice(["Completed", "Cancelled", "Refunded"], p=[0.90, 0.06, 0.04])
        payment_mode = np.random.choice(
            ["UPI", "Credit Card", "Debit Card", "Cash", "Wallet"],
            p=[0.42, 0.15, 0.15, 0.18, 0.10],
        )

        rows.append({
            "OrderID": order_id,
            "CustomerID": customer_id,
            "BranchID": branch_id,
            "EmployeeID": employee_id,
            "OrderDate": order_dt.date(),
            "OrderTime": order_dt.time(),
            "OrderType": order_type,
            "OrderStatus": status,
            # Subtotal/Discount/Tax/Total are back-filled after OrderDetails are generated
            "Subtotal": None,
            "DiscountAmount": None,
            "TaxAmount": None,
            "TotalAmount": None,
            "PaymentMode": payment_mode,
        })
        order_id += 1

    return pd.DataFrame(rows)


def generate_order_details(orders_df, products_df):
    print("Generating OrderDetails (and back-filling Order totals)...")
    product_records = products_df.to_dict("records")
    detail_rows = []
    detail_id = 1

    order_subtotal = {}
    order_discount = {}

    for order in orders_df.itertuples(index=False):
        n_items = random.choices([1, 2, 3, 4, 5], weights=[0.30, 0.30, 0.20, 0.12, 0.08])[0]
        chosen_products = random.sample(product_records, min(n_items, len(product_records)))
        sub, disc = 0.0, 0.0
        for prod in chosen_products:
            qty = random.randint(1, 3)
            unit_price = prod["SellingPrice"]
            line_discount = round(unit_price * qty * random.choice([0, 0, 0, 0.05, 0.10, 0.15]), 2)
            final_amount = round((unit_price * qty) - line_discount, 2)
            detail_rows.append({
                "OrderDetailID": detail_id,
                "OrderID": order.OrderID,
                "ProductID": prod["ProductID"],
                "Quantity": qty,
                "UnitPrice": unit_price,
                "DiscountAmount": line_discount,
                "FinalAmount": final_amount,
            })
            sub += unit_price * qty
            disc += line_discount
            detail_id += 1
        order_subtotal[order.OrderID] = round(sub, 2)
        order_discount[order.OrderID] = round(disc, 2)

    details_df = pd.DataFrame(detail_rows)

    orders_df = orders_df.copy()
    orders_df["Subtotal"] = orders_df["OrderID"].map(order_subtotal)
    orders_df["DiscountAmount"] = orders_df["OrderID"].map(order_discount)
    orders_df["TaxAmount"] = ((orders_df["Subtotal"] - orders_df["DiscountAmount"]) * 0.05).round(2)
    orders_df["TotalAmount"] = (
        orders_df["Subtotal"] - orders_df["DiscountAmount"] + orders_df["TaxAmount"]
    ).round(2)

    return orders_df, details_df


def generate_deliveries(orders_df):
    print("Generating Deliveries...")
    delivery_orders = orders_df[orders_df["OrderType"] == "Delivery"]
    rows = []
    del_id = 1
    for order in delivery_orders.itertuples(index=False):
        distance = round(random.uniform(0.5, 14.5), 2)
        order_dt = datetime.combine(order.OrderDate, order.OrderTime)
        ready_offset = random.randint(8, 25)
        pickup_offset = ready_offset + random.randint(2, 15)
        deliver_offset = pickup_offset + int(distance * random.uniform(2.5, 5.0)) + random.randint(0, 10)

        status = np.random.choice(
            ["Delivered", "Pending", "Cancelled", "Returned", "Failed"],
            p=[0.86, 0.03, 0.04, 0.03, 0.04],
        )
        ready_time = order_dt + timedelta(minutes=ready_offset)
        pickup_time = order_dt + timedelta(minutes=pickup_offset)
        delivery_time = order_dt + timedelta(minutes=deliver_offset) if status == "Delivered" else None

        rows.append({
            "DeliveryID": del_id,
            "OrderID": order.OrderID,
            "DeliveryPartner": random.choice(DELIVERY_PARTNERS),
            "DeliveryDistanceKM": distance,
            "OrderReadyTime": ready_time,
            "DeliveryPickupTime": pickup_time,
            "DeliveryTime": delivery_time,
            "DeliveryStatus": status,
            "DeliveryFee": round(20 + distance * random.uniform(5, 9), 2),
        })
        del_id += 1
    return pd.DataFrame(rows)


def generate_inventory(branches_df, ingredients_df):
    print("Generating Inventory...")
    rows = []
    inv_id = 1
    months = pd.date_range(ORDER_START_DATE, TODAY, freq="MS")
    for _, branch in branches_df.iterrows():
        for _, ingredient in ingredients_df.iterrows():
            for month in months:
                opening = round(random.uniform(20, 400), 2)
                received = round(random.uniform(10, 250), 2)
                used = round(random.uniform(10, opening + received - 5) if opening + received > 15 else 5, 2)
                wastage = round(used * random.uniform(0.0, 0.08), 2)
                closing = round(opening + received - used - wastage, 2)
                reorder_level = round(opening * random.uniform(0.15, 0.3), 2)
                expiry = month + timedelta(days=int(ingredient["ShelfLifeDays"]))
                rows.append({
                    "InventoryID": inv_id,
                    "BranchID": branch["BranchID"],
                    "IngredientID": ingredient["IngredientID"],
                    "StockAuditDate": month.date(),
                    "OpeningStock": opening,
                    "StockReceived": received,
                    "StockUsed": used,
                    "ClosingStock": max(closing, 0),
                    "ReorderLevel": reorder_level,
                    "ExpiryDate": expiry.date(),
                })
                inv_id += 1
    return pd.DataFrame(rows)


def generate_wastage(branches_df, ingredients_df, high_wastage_branch_ids):
    print("Generating Wastage...")
    rows = []
    wid = 1
    months = pd.date_range(ORDER_START_DATE, TODAY, freq="MS")
    ingredient_records = ingredients_df.to_dict("records")
    for _, branch in branches_df.iterrows():
        is_high = branch["BranchID"] in high_wastage_branch_ids
        n_ingredients_wasted = random.randint(20, 35) if is_high else random.randint(6, 15)
        for month in months:
            wasted_ings = random.sample(ingredient_records, min(n_ingredients_wasted, len(ingredient_records)))
            for ing in wasted_ings:
                qty = round(random.uniform(1, 15) * (2.5 if is_high else 1.0), 2)
                cost_per_unit = round(random.uniform(20, 350), 2)
                rows.append({
                    "WastageID": wid,
                    "BranchID": branch["BranchID"],
                    "IngredientID": ing["IngredientID"],
                    "WastageDate": (month + timedelta(days=random.randint(0, 27))).date(),
                    "WastageQuantity": qty,
                    "WastageReason": random.choices(
                        WASTAGE_REASONS,
                        weights=[0.30, 0.20, 0.15, 0.15, 0.10, 0.10] if is_high else [0.25, 0.15, 0.15, 0.15, 0.15, 0.15],
                    )[0],
                    "EstimatedWastageCost": round(qty * cost_per_unit, 2),
                })
                wid += 1
    return pd.DataFrame(rows)


def generate_operating_costs(branches_df, high_cost_branch_ids):
    print("Generating OperatingCosts...")
    rows = []
    cid = 1
    months = pd.date_range(ORDER_START_DATE, TODAY, freq="MS")
    base_cost_range = {
        "Rent": (80000, 250000), "Electricity": (25000, 70000), "Salaries": (350000, 700000),
        "Maintenance": (8000, 30000), "Delivery": (15000, 60000), "Cleaning": (5000, 15000),
        "Repairs": (3000, 40000), "Miscellaneous": (2000, 20000),
    }
    for _, branch in branches_df.iterrows():
        is_high_cost = branch["BranchID"] in high_cost_branch_ids
        multiplier = random.uniform(1.3, 1.8) if is_high_cost else random.uniform(0.85, 1.15)
        for month in months:
            for category in COST_CATEGORIES:
                lo, hi = base_cost_range[category]
                amount = round(random.uniform(lo, hi) * multiplier, 2)
                rows.append({
                    "CostID": cid,
                    "BranchID": branch["BranchID"],
                    "CostDate": month.date(),
                    "CostCategory": category,
                    "CostAmount": amount,
                    "Description": f"{category} expense for {month.strftime('%B %Y')}",
                })
                cid += 1
    return pd.DataFrame(rows)


def generate_refunds(orders_df):
    print("Generating Refunds...")
    candidates = orders_df[orders_df["OrderStatus"].isin(["Refunded", "Cancelled"])]
    rows = []
    rid = 1
    for order in candidates.itertuples(index=False):
        if order.OrderStatus == "Cancelled" and random.random() > 0.5:
            continue  # not every cancellation results in a refund record
        order_dt = datetime.combine(order.OrderDate, order.OrderTime)
        refund_date = order_dt + timedelta(days=random.randint(0, 5))
        status = np.random.choice(REFUND_STATUSES, p=[0.15, 0.35, 0.15, 0.35])
        refund_amount = round(order.TotalAmount * random.uniform(0.3, 1.0), 2) if status in ("Approved", "Processed") \
            else round(order.TotalAmount * random.uniform(0.3, 1.0), 2)
        rows.append({
            "RefundID": rid,
            "OrderID": order.OrderID,
            "RefundDate": refund_date.date(),
            "RefundAmount": refund_amount,
            "RefundReason": random.choice(REFUND_REASONS),
            "RefundStatus": status,
        })
        rid += 1
    return pd.DataFrame(rows)


REVIEW_TEMPLATES = {
    "Positive": [
        "Absolutely loved the food, quick service too!", "Great taste and hot, fresh delivery.",
        "One of the best QSR experiences in the city.", "Friendly staff and tasty food, will order again.",
        "Perfectly cooked and packed really well.",
    ],
    "Neutral": [
        "Food was okay, nothing special.", "Average experience, delivery took a bit long.",
        "Decent taste but portion size could be better.", "It was fine, met basic expectations.",
    ],
    "Negative": [
        "Food arrived cold and soggy.", "Order was incorrect and staff was unhelpful.",
        "Way too oily and not fresh at all.", "Delivery was very late and food quality was poor.",
        "Extremely disappointed, will not order again.",
    ],
}


def generate_reviews(customers_df, orders_df, products_df, branches_df, food_safety_risk_branch_ids):
    print("Generating Reviews...")
    completed_orders = orders_df[orders_df["OrderStatus"] == "Completed"]
    sampled = completed_orders.sample(frac=0.42, random_state=SEED)
    rows = []
    rev_id = 1
    product_ids = products_df["ProductID"].tolist()

    for order in sampled.itertuples(index=False):
        risk_branch = order.BranchID in food_safety_risk_branch_ids
        rating = np.random.choice(
            [1, 2, 3, 4, 5],
            p=[0.18, 0.17, 0.20, 0.22, 0.23] if risk_branch else [0.04, 0.06, 0.15, 0.35, 0.40],
        )
        sentiment = "Positive" if rating >= 4 else ("Neutral" if rating == 3 else "Negative")
        review_text = random.choice(REVIEW_TEMPLATES[sentiment]) if random.random() > 0.15 else None
        rows.append({
            "ReviewID": rev_id,
            "CustomerID": order.CustomerID,
            "OrderID": order.OrderID,
            "ProductID": random.choice(product_ids),
            "BranchID": order.BranchID,
            "ReviewDate": order.OrderDate + timedelta(days=random.randint(0, 4)),
            "Rating": int(rating),
            "ReviewText": review_text,
            "SentimentCategory": sentiment,
        })
        rev_id += 1
    return pd.DataFrame(rows)


def generate_food_safety_inspections(branches_df, closed_branch_ids, closure_dates):
    print("Generating FoodSafetyInspections...")
    rows = []
    insp_id = 1

    for _, branch in branches_df.iterrows():
        branch_id = branch["BranchID"]
        opening_dt = pd.to_datetime(branch["OpeningDate"])
        is_closed = branch_id in closed_branch_ids
        end_dt = pd.to_datetime(closure_dates[branch_id]) if is_closed else pd.Timestamp(TODAY)
        start_dt = max(opening_dt, pd.Timestamp(ORDER_START_DATE) - timedelta(days=365))

        if is_closed:
            # Monthly inspections leading up to closure, trending toward non-compliance
            dates = pd.date_range(start=max(start_dt, end_dt - timedelta(days=730)), end=end_dt, freq="30D")
        else:
            # Quarterly routine inspections
            dates = pd.date_range(start=start_dt, end=end_dt, freq="90D")

        for i, insp_date in enumerate(dates):
            if is_closed:
                # increasing probability of failure as branch approaches closure
                progress = i / max(len(dates) - 1, 1)
                compliance_probs = {
                    "Compliant": max(0.35 - progress * 0.35, 0.02),
                    "Minor Issues": 0.30,
                    "Major Issues": 0.20 + progress * 0.20,
                    "Non-Compliant": 0.15 + progress * 0.30,
                }
            else:
                compliance_probs = {"Compliant": 0.68, "Minor Issues": 0.22, "Major Issues": 0.07, "Non-Compliant": 0.03}

            statuses = list(compliance_probs.keys())
            probs = np.array(list(compliance_probs.values()))
            probs = probs / probs.sum()
            compliance = np.random.choice(statuses, p=probs)

            score_ranges = {"Compliant": (85, 100), "Minor Issues": (65, 84),
                             "Major Issues": (40, 64), "Non-Compliant": (0, 39)}
            lo, hi = score_ranges[compliance]
            score = random.randint(lo, hi)

            has_violation = compliance != "Compliant"
            severity = None
            category = None
            action_status = None
            action_desc = None
            if has_violation:
                severity = random.choices(
                    VIOLATION_SEVERITIES,
                    weights=[0.35, 0.30, 0.22, 0.13] if compliance != "Non-Compliant" else [0.05, 0.15, 0.35, 0.45],
                )[0]
                category = random.choice(VIOLATION_CATEGORIES)
                action_status = np.random.choice(
                    ["Pending", "In Progress", "Completed", "Not Addressed"],
                    p=[0.20, 0.25, 0.40, 0.15],
                )
                action_desc = f"{category} issue flagged — corrective action {action_status.lower()}."

            rows.append({
                "InspectionID": insp_id,
                "BranchID": branch_id,
                "InspectionDate": insp_date.date(),
                "InspectionType": random.choice(INSPECTION_TYPES),
                "InspectionScore": score,
                "ComplianceStatus": compliance,
                "ViolationCategory": category,
                "ViolationSeverity": severity,
                "CorrectiveActionStatus": action_status,
                "CorrectiveActionDescription": action_desc,
            })
            insp_id += 1

    return pd.DataFrame(rows)


# ==============================================================================
# 4. DIRTY DATA INJECTION (applied AFTER clean data + relationships are built)
# ==============================================================================

def dirty_branches(df):
    df = introduce_case_inconsistency(df, "City", DIRTY_FRACTION_LOW)
    df = introduce_extra_spaces(df, "BranchName", DIRTY_FRACTION_LOW)
    return df


def dirty_customers(df):
    df = introduce_case_inconsistency(df, "City", DIRTY_FRACTION_MED)
    df = introduce_case_inconsistency(df, "Email", DIRTY_FRACTION_LOW)
    df = introduce_extra_spaces(df, "FirstName", DIRTY_FRACTION_LOW)
    df = introduce_extra_spaces(df, "LastName", DIRTY_FRACTION_LOW)
    df = introduce_duplicate_values(df, "Email", DIRTY_FRACTION_LOW)
    df = introduce_duplicate_values(df, "Phone", DIRTY_FRACTION_LOW)
    df = introduce_duplicate_rows(df, 0.01)
    # a few missing DOBs / join dates for cleaning practice
    df = introduce_nulls(df, "DOB", 0.01)
    return df


def dirty_employees(df):
    df = introduce_case_inconsistency(df, "Role", DIRTY_FRACTION_LOW)
    df = introduce_extra_spaces(df, "Email", DIRTY_FRACTION_LOW)
    df = introduce_duplicate_values(df, "Email", 0.01)
    # negative salary as a data-quality problem to catch during cleaning
    df = introduce_negative_values(df, "Salary", 0.01)
    return df


def dirty_products(df):
    df = introduce_case_inconsistency(df, "Category", DIRTY_FRACTION_LOW)
    df = introduce_extra_spaces(df, "ProductName", DIRTY_FRACTION_LOW)
    return df


def dirty_orders(df):
    df = introduce_case_inconsistency(df, "OrderType", DIRTY_FRACTION_MED)
    df = introduce_case_inconsistency(df, "OrderStatus", DIRTY_FRACTION_MED)
    df = introduce_case_inconsistency(df, "PaymentMode", DIRTY_FRACTION_LOW)
    df = introduce_negative_values(df, "DiscountAmount", 0.01)
    df = introduce_outliers(df, "TotalAmount", 0.005, multiplier=6)
    df = introduce_nulls(df, "PaymentMode", 0.01)
    return df


def dirty_order_details(df):
    df = introduce_negative_values(df, "Quantity", 0.005)
    df = introduce_outliers(df, "DiscountAmount", 0.005, multiplier=10)
    return df


def dirty_deliveries(df):
    df = introduce_case_inconsistency(df, "DeliveryStatus", DIRTY_FRACTION_LOW)
    df = introduce_negative_values(df, "DeliveryDistanceKM", 0.01)
    df = introduce_nulls(df, "DeliveryTime", 0.02)  # beyond the structurally-null failed/pending ones
    return df


def dirty_inventory(df):
    # suspicious negative stock + inconsistent opening/closing math
    df = introduce_negative_values(df, "StockUsed", 0.01)
    idx = _rand_idx(len(df), 0.03)
    for i in idx:
        df.at[i, "ClosingStock"] = round(df.at[i, "ClosingStock"] + random.uniform(-40, 40), 2)
    df = introduce_nulls(df, "ExpiryDate", 0.02)
    return df


def dirty_wastage(df):
    df = introduce_case_inconsistency(df, "WastageReason", DIRTY_FRACTION_LOW)
    df = introduce_outliers(df, "WastageQuantity", 0.01, multiplier=7)
    return df


def dirty_operating_costs(df):
    df = introduce_negative_values(df, "CostAmount", 0.005)
    df = introduce_case_inconsistency(df, "CostCategory", DIRTY_FRACTION_LOW)
    return df


def dirty_refunds(df):
    df = introduce_case_inconsistency(df, "RefundStatus", DIRTY_FRACTION_LOW)
    df = introduce_negative_values(df, "RefundAmount", 0.01)
    return df


def dirty_reviews(df):
    df = introduce_case_inconsistency(df, "SentimentCategory", DIRTY_FRACTION_LOW)
    # a few inconsistent sentiment labels vs rating (intentional mismatch for cleaning)
    idx = _rand_idx(len(df), 0.02)
    for i in idx:
        df.at[i, "SentimentCategory"] = random.choice(["Positive", "Neutral", "Negative"])
    return df


def dirty_inspections(df):
    df = introduce_case_inconsistency(df, "ComplianceStatus", DIRTY_FRACTION_LOW)
    # a small percentage of invalid/out-of-range inspection scores
    idx = _rand_idx(len(df), 0.01)
    for i in idx:
        df.at[i, "InspectionScore"] = random.choice([-5, 105, 150])
    return df


# ==============================================================================
# 5. MAIN ORCHESTRATION
# ==============================================================================

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    summary = []

    def save(df, name):
        path = os.path.join(OUTPUT_DIR, f"{name}.csv")
        df.to_csv(path, index=False)
        summary.append({
            "table_name": name,
            "rows": len(df),
            "columns": len(df.columns),
            "file_name": f"{name}.csv",
        })
        print(f"  -> saved {name}.csv  ({len(df):,} rows x {len(df.columns)} cols)")

    # ---- 1. Independent / low-dependency tables -----------------------------
    branches_df, closed_branch_ids, closure_dates = generate_branches()
    customers_df = generate_customers(N_CUSTOMERS)
    employees_df = generate_employees(branches_df, N_EMPLOYEES_TARGET)
    products_df = generate_products()
    ingredients_df = generate_ingredients()
    product_ingredients_df = generate_product_ingredients(products_df, ingredients_df)

    # scenario branches: closed branches double as the food-safety risk branches;
    # pick a couple of extra branches with high wastage / high operating cost
    non_closed_ids = set(branches_df["BranchID"]) - closed_branch_ids
    high_wastage_branch_ids = closed_branch_ids | set(random.sample(sorted(non_closed_ids), 2))
    high_cost_branch_ids = set(random.sample(sorted(non_closed_ids), 3))

    # ---- 2. Transactional core -----------------------------------------------
    orders_df = generate_orders(customers_df, branches_df, employees_df,
                                 closed_branch_ids, closure_dates, N_ORDERS)
    orders_df, order_details_df = generate_order_details(orders_df, products_df)
    deliveries_df = generate_deliveries(orders_df)

    # ---- 3. Operations tables --------------------------------------------
    inventory_df = generate_inventory(branches_df, ingredients_df)
    wastage_df = generate_wastage(branches_df, ingredients_df, high_wastage_branch_ids)
    operating_costs_df = generate_operating_costs(branches_df, high_cost_branch_ids)

    # ---- 4. Post-sale tables --------------------------------------------
    refunds_df = generate_refunds(orders_df)
    reviews_df = generate_reviews(customers_df, orders_df, products_df, branches_df, closed_branch_ids)
    inspections_df = generate_food_safety_inspections(branches_df, closed_branch_ids, closure_dates)

    # ---- 5. Inject controlled dirty data ----------------------------------
    print("\nInjecting controlled data-quality issues...")
    branches_df = dirty_branches(branches_df)
    customers_df = dirty_customers(customers_df)
    employees_df = dirty_employees(employees_df)
    products_df = dirty_products(products_df)
    orders_df = dirty_orders(orders_df)
    order_details_df = dirty_order_details(order_details_df)
    deliveries_df = dirty_deliveries(deliveries_df)
    inventory_df = dirty_inventory(inventory_df)
    wastage_df = dirty_wastage(wastage_df)
    operating_costs_df = dirty_operating_costs(operating_costs_df)
    refunds_df = dirty_refunds(refunds_df)
    reviews_df = dirty_reviews(reviews_df)
    inspections_df = dirty_inspections(inspections_df)

    # ---- 6. Save everything -------------------------------------------------
    print("\nSaving CSV files to ./raw_data/ ...")
    save(branches_df, "Branches")
    save(customers_df, "Customers")
    save(employees_df, "Employees")
    save(products_df, "Products")
    save(ingredients_df, "Ingredients")
    save(product_ingredients_df, "ProductIngredients")
    save(orders_df, "Orders")
    save(order_details_df, "OrderDetails")
    save(deliveries_df, "Deliveries")
    save(inventory_df, "Inventory")
    save(wastage_df, "Wastage")
    save(operating_costs_df, "OperatingCosts")
    save(refunds_df, "Refunds")
    save(reviews_df, "Reviews")
    save(inspections_df, "FoodSafetyInspections")

    # ---- 7. Summary -----------------------------------------------------
    summary_df = pd.DataFrame(summary)
    print("\n" + "=" * 70)
    print("GENERATION SUMMARY")
    print("=" * 70)
    print(summary_df.to_string(index=False))
    print("-" * 70)
    print(f"TOTAL ROWS ACROSS ALL TABLES: {summary_df['rows'].sum():,}")
    print("=" * 70)
    summary_df.to_csv(os.path.join(OUTPUT_DIR, "_generation_summary.csv"), index=False)


if __name__ == "__main__":
    main()
