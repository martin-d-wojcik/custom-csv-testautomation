from filehandler import csvfilehandler
from assertions import csvassertions
from testengine import testrunner


def test_organization_name_by_index_should_pass(self):
    # prepare
    row = csvfilehandler.read_row_from_csv_file(1)

    # perform
    name_of_organization = csvfilehandler.read_one_value_from_row(row, 2)

    # assert
    return csvassertions.assert_strings_are_equal('Ferrell LLC', name_of_organization)


def test_read_invalid_organization_should_fail(self):
    # prepare
    row = csvfilehandler.read_row_from_csv_file(1)

    # perform
    name_of_organization = csvfilehandler.read_one_value_from_row(row, 2)

    # assert
    return csvassertions.assert_strings_are_not_equal('Görans blommor', name_of_organization)


if __name__ == '__main__':
    test_suite = ['test_organization_name_by_index_should_pass',
                  'test_read_invalid_organization_should_fail']
    testrunner.test_runner(test_suite)

    # The testengine. Select tests. Mimmick before.
    # start and log integrationtest cases
    # save passed/failed var. Number of tests ran. NUmber of passed.
    # print to console/log
    # config with logging config