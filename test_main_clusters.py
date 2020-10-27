import pytest
from vodafone_interview.main import *


@pytest.mark.solution_test
def test_get_data_clusters():
    data = main()
    assert len(data[0].cluster) == 2
    assert len(data[1].cluster) == 1


@pytest.mark.solution_test
def test_first_cluster():
    data = main()
    assert data[0].cluster['BER-1'].name == 'BER-1'
    assert data[0].cluster['BER-1'].security_level == 1


@pytest.mark.solution_test
def test_first_cluster_networks():
    data = main()
    assert len(data[0].cluster['BER-1'].networks) == 2
    assert len(data[0].cluster['BER-1'].networks[0].entries) == 4
    assert len(data[0].cluster['BER-1'].networks[1].entries) == 3
