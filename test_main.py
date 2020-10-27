import pytest
from vodafone_interview.main import *


@pytest.mark.solution_test
def test_get_data_wrong_url():
    print("Testing get_data function")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        get_data("ana", 5, 5)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2


@pytest.mark.solution_test
def test_get_data_nr_of_data_center():
    data = main()
    assert len(data) == 2
