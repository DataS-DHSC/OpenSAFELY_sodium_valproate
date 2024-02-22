from ehrql import create_dataset, codelist_from_csv
from ehrql.tables.core import patients, medications, clinical_events
from ehrql import INTERVAL, case, create_measures, months, when
from ehrql.tables.tpp import clinical_events, apcs
from ehrql import case, when
from ehrql.tables.tpp import addresses

from analysis.codelists import epilepsy_codelist


from analysis.codelists import test_codelist

dataset = create_dataset()

# epilepsy_codelist = codelist_from_csv( 
#     "codelists/nhsd-primary-care-domain-refsets-epil_cod.csv",
#     column="code"
# )

index_date = '2020-01-01'
# #-------------------------------

is_female_or_male = patients.sex.is_in(["female", "male"])

was_alive = (
    patients.date_of_death.is_after(index_date)
    | patients.date_of_death.is_null()
)

dataset.define_population(
    is_female_or_male
    & was_alive
)

# #--------------------------------

dataset.epilepsy = (
    clinical_events.where(
        clinical_events.snomedct_code.is_in(test_codelist)
    )
    .sort_by(clinical_events.date)
    .last_for_patient()
    .snomedct_code
)


# sodium_val_codes =['13295911000001108','13295911000001108'] #will need a full codelist 

# first_sv_med = (
#     medications.where(medications.dmd_code.is_in(sodium_val_codes))
#     .sort_by(medications.date)
#     .first_for_patient()
# )
# dataset.med_date = first_sv_med.date
# dataset.med_code = first_sv_med.dmd_code


