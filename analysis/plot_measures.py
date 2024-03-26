#%%

import seaborn as sns
import pandas as pd 
from pathlib import Path 


BASE_DIR = Path(__file__).parents[1]
OUTPUT_DIR = BASE_DIR / "output"
ANALYSIS_DIR = BASE_DIR / "analysis"
print(OUTPUT_DIR)
#pathlib.Path(OUTPUT_DIR / "rounded").mkdir(parents=True, exist_ok=True)





data_df = pd.read_csv(OUTPUT_DIR/ 'input.csv.gz')
data_df.loc[:,'first_epilepsy_diagnosis'] = pd.to_datetime(data_df.first_epilepsy_diagnosis)
data_df.loc[:,'first_sodium_valproate_prescription_date'] = pd.to_datetime(data_df.first_sodium_valproate_prescription_date)
data_df.loc[:,'diag_to_sodium_val'] = data_df.first_sodium_valproate_prescription_date - data_df.first_epilepsy_diagnosis
# grouped_df = data_df.query('has_had_epilepsy_diagnosis == "T" and has_sodium_valproate_prescription == "T"').groupby('sex')['diag_to_sodium_val'].mean()
data_df.loc[:,'diag_to_sodium_val'] = [x.days for x in data_df.diag_to_sodium_val]
f = sns.barplot(data_df,
                  x = 'sex',
                  y = 'diag_to_sodium_val')
f.set_title('example figure')
sns.despine()
# grouped_df.to_csv('test_output.csv')
f.savefig('example_figure.png')
