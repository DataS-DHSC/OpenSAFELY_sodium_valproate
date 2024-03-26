from ehrql import create_dataset, codelist_from_csv
from ehrql.tables.core import patients, medications, clinical_events
from ehrql import INTERVAL, case, create_measures, months, when
from ehrql.tables.tpp import clinical_events, apcs
from ehrql import case, when
from ehrql.tables.tpp import addresses

from analysis.codelists import epilepsy_test_codelist, sodium_valproate_test_codelist

dataset = create_dataset()

# epilepsy_codelist = codelist_from_csv( 
#     "codelists/nhsd-primary-care-domain-refsets-epil_cod.csv",
#     column="code"
# )

index_date = '2020-01-01'
# #-------------------------------
#sex filter
is_female_or_male = patients.sex.is_in(["female", "male"])
#alvie filter
was_alive = (
    patients.date_of_death.is_after(index_date)
    | patients.date_of_death.is_null()
)

# find age band
age = patients.age_on("2023-01-01")
dataset.age_band = case(
    when((age >= 0) & (age < 12)).then("0-11"),
    when((age >= 12) & (age < 18)).then("12-17"),
    when((age >= 18) & (age < 45)).then("18-45"),
    when(age >= 45).then("45+"),
    otherwise="missing",
)
#find sex
dataset.sex = patients.sex
#find epilpesy
dataset.has_had_epilepsy_diagnosis = clinical_events.where(
        clinical_events.snomedct_code.is_in(epilepsy_test_codelist)
).exists_for_patient()
#first epi dat
dataset.first_epilepsy_diagnosis = clinical_events.where(
        clinical_events.snomedct_code.is_in(epilepsy_test_codelist)
).sort_by(
        clinical_events.date
).first_for_patient().date




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

#see erhqql how to guides - for how to select first med after first event
# -eg is sodium val the first med perscribed after epilsepey diag when it should be last resort



dataset.define_population(
    is_female_or_male
    & was_alive
)

# #--------------------------------

# dataset.epilepsy = (
#     clinical_events.where(
#         clinical_events.snomedct_code.is_in(epilepsy_test_codelist)
#     )
#     .exists_for_patient()
# )

# dataset.sodium_val = (
#     medications.where(
#         medications.dmd_code.is_in(sodium_valproate_test_codelist)
#     )
#     .exists_for_patient()
# )



# # sodium_val_codes =['13295911000001108','13295911000001108'] #will need a full codelist 

# first_sv_med = (
#     medications.where(medications.dmd_code.is_in(sodium_val_codes))
#     .sort_by(medications.date)
#     .first_for_patient()
# )
# dataset.med_date = first_sv_med.date
# dataset.med_code = first_sv_med.dmd_code


