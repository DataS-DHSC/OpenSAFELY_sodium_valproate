#%%

import seaborn as sns
import pandas as pd 
from pathlib import Path 


BASE_DIR = Path(__file__).parents[1]
OUTPUT_DIR = BASE_DIR / "output"
ANALYSIS_DIR = BASE_DIR / "analysis"
print(OUTPUT_DIR)
#pathlib.Path(OUTPUT_DIR / "rounded").mkdir(parents=True, exist_ok=True)


df = pd.read_csv(OUTPUT_DIR/ 'input.csv.gz')
df2 = df.query('epilepsy == "T"')
df2.to_csv('test_output.csv')