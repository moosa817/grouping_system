import json
import random
from pyfiglet import Figlet
import config
from tabulate import tabulate


def main():
    print_info()

    # get json file
    config.INPUT_FILE = (
        input("Input json file (students.json by default) : ") or config.INPUT_FILE
    )

    # read json and checks if its valid
    students_list = read_json(config.INPUT_FILE)

    # create groups
    groups = create_groups(students_list)

    # make groups with prefered qualities
    final_groups = make_groups(groups, students_list)

    # prints everything in tabular form
    student_info_list = read_json(config.INPUT_FILE)
    print_result(final_groups, student_info_list)


def print_info():
    print(Figlet(font="doom").renderText("Grouping System"))

    print(
        "Welcome to the grouping system , \n This Program makes groups of students/people based on their qualities , \n you can choose the number of students in a group, Each student can have 1 upto 3 qualities \n All these setttings are setted in `config.py`, This Program reads the input from a json file which you can specify.\n\n"
    )
    print(
        """input json file example: \n
        [{
            "roll_no": 1,
            "qualities": [
                "etc1",
                "etc2"
            ]
        },...]
        , """
    )


# loads roll no and qualities
def read_json(file_name):
    with open(file_name, "r") as f:
        data = json.loads(f.read())
        random.shuffle(data)
        return data


def create_groups(
    students_list, group_size=config.GROUP_SIZE, qualities=config.QUALITIES
):
    groups = []
    if len(students_list) % group_size > 0:
        no_of_groups = len(students_list) // group_size + 1
    else:
        no_of_groups = len(students_list) // group_size

    for i in range(no_of_groups):
        groups.append(
            {
                "id": i + 1,
                "Qualities": {x: 0 for x in qualities},
                "group_members": [],
            }
        )

    return groups


def get_student(quality, students_list):
    if not students_list:
        return None
    iteration = 0
    while iteration < 3:
        # 2 iterations done we still didnot find prefered quality
        if iteration == 2:
            return random.choice(students_list)

        for student in students_list:
            if quality in student["qualities"]:
                if iteration == 0:
                    if len(student["qualities"]) > 1:
                        continue

                return student
        iteration += 1


def make_groups(groups, students_list):
    for i in range(len(groups)):
        for no in range(config.GROUP_SIZE):
            if no < len(config.QUALITIES):
                quality = config.QUALITIES[no]
            else:
                quality = random.choice(config.QUALITIES)
            if get_student(quality, students_list):
                student = get_student(quality, students_list)
                groups[i]["group_members"].append(student["roll_no"])
                for student_quality in student["qualities"]:
                    groups[i]["Qualities"][student_quality] += 1

                    for n, k in enumerate(students_list):
                        if k == student:
                            del students_list[n]

    return groups


from tabulate import tabulate


def print_result(groups, students_list):
    print(f"\n\nTotal Students : {len(students_list)}")
    for i in groups:
        memebers_info = []
        n = 0
        for j in i["group_members"]:
            for student in students_list:
                if student["roll_no"] == j:
                    if n < len(i["Qualities"]):
                        quality, count = list(i["Qualities"].items())[n]
                        skill = f"{quality}:{count}"
                        n += 1
                    else:
                        skill = ""

                    memebers_info.append(
                        [
                            j,
                            student["qualities"],
                            skill,
                        ]
                    )

        print(f"Group {i['id']}, Total Members: {len(memebers_info)}")
        print(
            tabulate(
                memebers_info,
                headers=["Roll No", "Qualities", "Quality Count"],
                tablefmt="grid",
            )
        )
        print()


if __name__ == "__main__":
    main()
    input("Press Enter to exit")
    exit(0)
