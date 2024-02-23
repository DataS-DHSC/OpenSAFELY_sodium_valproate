from ehrql import codelist_from_csv

epilepsy_test_codelist = codelist_from_csv( 
    "codelists/user-g-w-jenkins-dhsc-epilepsy_test.csv",
    column="code"
)

sodium_valproate_test_codelist = codelist_from_csv( 
    "codelists/user-g-w-jenkins-dhsc-sodium_valproat_2.csv",
    column="code"
)