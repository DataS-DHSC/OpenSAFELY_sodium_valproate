"""Data defintion for Q1 - change in SV perscribing over time"""

from ehrql import create_dataset, codelist_from_csv
from ehrql.tables.core import patients, medications, clinical_events
from ehrql import INTERVAL, case, create_measures, months, when
from ehrql.tables.tpp import clinical_events, apcs
from ehrql import case, when
from ehrql.tables.tpp import addresses

from analysis.codelists import sodium_valproate_test_codelist

dataset = create_dataset()

#find sodium val
dataset.has_sodium_valproate_prescription = medications.where(
        medications.dmd_code.is_in(sodium_valproate_test_codelist)
).exists_for_patient()

# find first/last sodium val
dataset.first_sodium_valproate_prescription_date = medications.where(
        medications.dmd_code.is_in(sodium_valproate_test_codelist)
).sort_by(
        medications.date
).first_for_patient().date

dataset.last_sodium_valproate_prescription_date = medications.where(
        medications.dmd_code.is_in(sodium_valproate_test_codelist)
).sort_by(
        medications.date
).last_for_patient().date

# take ALL patients 
dataset.define_population(patients.exists_for_patient())
# #--------------------------------


