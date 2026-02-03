import sys
from pathlib import Path

p = Path.cwd().resolve()
repo_root = next((parent for parent in [p] + list(p.parents) if (parent / ".git").exists()), None)
if repo_root is None:
    raise RuntimeError("Repo root not found. Open the repo folder in VS Code.")

sys.path.insert(0, str(repo_root))
print("Repo root:", repo_root)

import pandas as pd
import numpy as np
#/usr/local/bin/python3 -m pip install [pckg]

county_commuting = pd.read_csv(f"{str(repo_root)}/cleaned/00_commuting_data/county_commuting.csv")
county_econ_activity = pd.read_csv(f"{str(repo_root)}/cleaned/00_econ_activity_data/county_econ_activity.csv")
county_econ_activity # some (4) incomplete but matches to the muni's for which there is commuting data anyway

county_commuting_prop = county_commuting.merge(county_econ_activity.rename(columns={'county_code':'county_code_residence'}))
county_commuting_prop['commuters_prop'] = county_commuting_prop['commuters'] / county_commuting_prop['econ_active_population']

print(county_commuting_prop.head())