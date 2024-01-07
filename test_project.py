import pytest
from project import (
    create_groups,
    get_student,
    make_groups,
)


@pytest.fixture
def sample_data():
    return [
        {"roll_no": 1, "qualities": ["Teamwork"]},
        {"roll_no": 2, "qualities": ["Communication"]},
        {"roll_no": 3, "qualities": ["Teamwork", "Communication"]},
        {"roll_no": 4, "qualities": ["Communication", "Teamwork"]},
        {"roll_no": 5, "qualities": ["Communication"]},
    ]


def test_create_groups():
    students_list = [{"roll_no": i, "qualities": []} for i in range(1, 11)]
    group_size = 3
    groups = create_groups(students_list, group_size)

    assert len(groups) == 4
    assert groups[0]["id"] == 1
    assert groups[-1]["id"] == 4


def test_get_student(sample_data):
    quality = "Communication"
    student = get_student(quality, sample_data)
    assert student is not None
    assert quality in student["qualities"]


def test_make_groups(sample_data):
    groups = create_groups(sample_data, 2, ["Teamwork", "Communication"])
    result_groups = make_groups(groups, sample_data)

    assert len(result_groups) == len(groups)
    for group in result_groups:
        assert group["group_members"]


if __name__ == "__main__":
    pytest.main()
