from ehrql import codelist_from_csv

epilepsy_codelist = codelist_from_csv( 
    "codelists/nhsd-primary-care-domain-refsets-epil_cod.csv",
    column="code"
)

test_codelist = codelist_from_csv( 
    "codelists/user-g-w-jenkins-dhsc-epilepsy_test.csv",
    column="code"
)