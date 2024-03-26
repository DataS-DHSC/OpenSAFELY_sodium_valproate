from ehrql import create_dataset
from ehrql.tables.core import patients, medications, clinical_events
from ehrql import INTERVAL, case, create_measures, months, when
from analysis.codelists import sodium_valproate_test_codelist, epilepsy_test_codelist

measures = create_measures()
measures.configure_disclosure_control(enabled=True) #disables sup[resssing/rouding - maybe set to true for actual exp?]



age = patients.age_on(INTERVAL.start_date)
age_band = case(
    when((age >= 0) & (age < 12)).then("0-11"),
    when((age >= 12) & (age < 18)).then("12-17"),
    when((age >= 18) & (age < 45)).then("18-45"),
    when(age >= 45).then("45+"),
)

has_recorded_sex = patients.sex.is_in(["male", "female"])
has_epilepsy = epilepsy_test_codelist


rx_in_interval = medications.where(
    medications.date.is_during(INTERVAL)
)
sodium_val_rx = rx_in_interval.where(
    medications.dmd_code.is_in(sodium_valproate_test_codelist))


epilepsy_rx =  clinical_events.where(
    clinical_events.snomedct_code.is_in(epilepsy_test_codelist)
)

measures.define_measure(
    name="sodval_test",
    # numerator=sodium_val_rx.exists_for_patient() & epilepsy_rx.exists_for_patient() & has_recorded_sex,
    # denominator= epilepsy_rx.exists_for_patient() & has_recorded_sex,
    numerator= sodium_val_rx.exists_for_patient() & has_recorded_sex,
    denominator=  has_recorded_sex,
    group_by={
        "sex": patients.sex,
        "age_band": age_band
    },
    intervals=months(24).starting_on("2015-01-01"),
)