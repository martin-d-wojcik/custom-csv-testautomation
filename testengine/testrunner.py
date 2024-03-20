from integrationtest import testreadvaluesfromcsv
import logging

logging.basicConfig(level=logging.DEBUG)


def test_runner(list_of_test_cases):
    print(testreadvaluesfromcsv.__all__)

    for test_case in list_of_test_cases:
        match test_case:
            case 'test_organization_name_by_index_should_pass':
                log_test_case('test_organization_name_by_index_should_pass')
                # Run the test case function
                result = testreadvaluesfromcsv.test_organization_name_by_index_should_pass()

                # TODO: save result in global var

                # Log the result
                log_test_result(result)
            case 'test_read_invalid_organization_should_fail':
                log_test_case('test_read_invalid_organization_should_fail')
                # Run the test case function
                result = testreadvaluesfromcsv.test_read_invalid_organization_should_fail()

                # Log the result
                log_test_result(result)


def log_test_case(test_case_name):
    logging.info("Starting new integrationtest case: {}".format(test_case_name))


def log_test_result(result):
    logging.info("Test case {}\n".format(result))

# log result for each integrationtest case
# log x/y