# Grouping System 

## Introduction
Welcome to the Grouping System! This Python program facilitates the creation of groups based on the qualities of students. It takes input from a JSON file containing information about students, such as their roll number and qualities. The program allows customization, allowing you to specify the group size and the qualities students possess.

## Getting Started
To use the Grouping System, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python installed.
3. Install the required packages by running:
    ```bash
    pip install pyfiglet tabulate
    ```
4. Adjust configuration settings in the `config.py` file to suit your preferences.
5. Prepare a JSON file with student information. The structure should include a list of dictionaries, each containing the student's roll number and a list of qualities.

Example JSON format:
```json
[
    {
        "roll_no": 1,
        "qualities": ["etc1", "etc2"]
    },
    ...
]
```

## Running the Program
Execute the program by running the `main.py` file in your terminal or preferred Python environment. The program will prompt you to input the JSON file name, defaulting to "students.json" if not provided. It then reads the JSON file, shuffles the data, and proceeds to create groups based on the specified settings.

## Program Flow
1. **Initialization**: The program starts by displaying a stylish title using the "pyfiglet" package and providing an overview of its purpose.

2. **JSON Input**: The user is prompted to input the name of the JSON file containing student information. If no input is provided, the default file name from the `config.py` file is used.

3. **Reading JSON**: The program reads the JSON file, shuffles the data randomly, and stores the information in a list.

4. **Group Creation**: Groups are initialized based on the desired group size. The number of groups is calculated to accommodate all students.

5. **Qualities Assignment**: The program assigns students to groups, considering their specified qualities. It aims to distribute students with similar qualities evenly across groups.

6. **Print Result**: The final step involves printing the results in a tabular format. The total number of students, each group's members with their qualities, and any remaining students who were not assigned to a group are displayed.

## Customization
The program's behavior can be customized through the `config.py` file. You can adjust settings such as the default input file name, group size, and qualities.

## Dependencies
- **pyfiglet**: Used for creating ASCII art titles.
- **tabulate**: Used for formatting and printing tabular data.

## Conclusion
The Grouping System provides a flexible and customizable solution for creating groups based on student qualities. Whether you're organizing a class project or team-building exercise, this program streamlines the process of forming diverse and balanced groups. Feel free to explore the code, modify configurations, and adapt it to your specific needs. If you encounter any issues or have suggestions for improvement, please contribute to the repository or reach out to the developer. Happy grouping!