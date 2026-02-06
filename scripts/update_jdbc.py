import os
import re
import sys

# 1️⃣ Read inputs from executor (CI/CD / Jenkins)
env = os.getenv("ENV")
new_jdbc_url = os.getenv("JDBC_URL")

if not env:
    print("ERROR: ENV not provided (dev / qa / stg / prod)")
    sys.exit(1)

if not new_jdbc_url:
    print("ERROR: JDBC_URL not provided")
    sys.exit(1)

# 2️⃣ Resolve config file for the environment
file_path = f"configs/{env}/app.properties"

if not os.path.exists(file_path):
    print(f"ERROR: Config file not found for ENV={env}")
    sys.exit(1)

# 3️⃣ Update JDBC URL safely
pattern = r"^jdbc\.url=.*$"
updated = False

with open(file_path, "r") as f:
    lines = f.readlines()

with open(file_path, "w") as f:
    for line in lines:
        if re.match(pattern, line):
            f.write(f"jdbc.url={new_jdbc_url}\n")
            updated = True
        else:
            f.write(line)

if not updated:
    print("ERROR: jdbc.url key not found in config")
    sys.exit(1)

print(f"SUCCESS: JDBC URL updated for ENV={env}")
sys.exit(0)
