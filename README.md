# Course Pathway Advising Using Rule-Based Reasoning

## Project Description

The Course Pathway Advising System is a Python-based academic decision-support system developed in Google Colab. It recommends suitable courses based on a student's completed courses, academic performance, interests, and target career.

The system uses prerequisite rules to determine which courses a student is currently eligible to take. It identifies unmet prerequisites and generates a recommended course sequence. A weighted-scoring algorithm is also used as a comparison method to rank possible courses according to career alignment, grades, interests, and prerequisite completion.

## Features

- Reads student records from a CSV file using Pandas.
- Stores course information in a knowledge base.
- Checks whether required prerequisites have been completed.
- Uses rule-based reasoning to recommend eligible courses.
- Generates a recommended course sequence.
- Identifies prerequisite courses required before advanced courses.
- Ranks courses using weighted scoring.
- Provides explainable recommendations and unmet-prerequisite information.
- Exports ranked recommendations as a CSV file.

## Algorithms

### Main Algorithm: Rule-Based Reasoning

Rule-Based Reasoning is the primary algorithm of the Course Pathway Advising System. It uses predefined IF-THEN rules to determine which courses are appropriate based on the student's completed courses, target career, and prerequisite requirements.

The system retrieves the student's completed courses and target career from the CSV dataset. It then compares this information with the course catalog. For every course, the system checks whether the course is related to the student's selected career and whether all required prerequisites have been completed.

Eligible courses are organized into a recommended course sequence. Courses with incomplete prerequisites are not immediately recommended. Instead, the system reports the missing prerequisite courses so that the student can complete them first.

Example rule:

```text
IF a course matches the student's target career
AND all prerequisites are completed
THEN recommend the course.
```

### Comparison Algorithm: Weighted Scoring

Weighted Scoring is used to compare the results of the Rule-Based Reasoning algorithm. Instead of relying only on logical conditions, it assigns numerical values to different student and course characteristics.

Each course receives points based on:

1. Career alignment
2. Academic performance
3. Interest alignment
4. Prerequisite completion

A course receives a higher score when it matches the student's target career, corresponds to the student's academic strengths, and aligns with the student's interests. Courses with unmet prerequisites receive a penalty.

## How Scoring Works

The scoring formula is:

```text
Final Score = Career Alignment
            + Academic Performance
            + Interest Alignment
            - Prerequisite Penalty
```

### 1. Career Alignment

A course receives **40 points** when it belongs to the student's target career area.

```python
if career in course_catalog[course]["career_area"]:
    score += 40
```

### 2. Mathematics Performance

For mathematics-related courses, the system awards **20 points** when the mathematics grade is at least 85. For other courses, it awards **10 points** when the mathematics grade is at least 85.

Mathematics-related courses include:

- Discrete Structures
- Data Structures And Alggorithm
- Algorithms
- Analytics Fundamentals
- Modeling and Simulation
- Image Processing
- Intelligent Systems

### 3. Programming Performance

For programming-related courses, the system awards **20 points** when the programming grade is at least 85. For other courses, it awards **10 points** when the programming grade is at least 85.

Programming-related courses include:

- Computer Programming
- Object Oriented Programming
- Structured Programming
- Programming Tools and Techniques
- Programming Languages
- Software Engineering
- Algorithms
- Mobile Programming
- Applications Development
- Operating Systems

### 4. Interest Alignment

Student interest is rated from 1 to 5:

| Interest Rating | Points |
|---:|---:|
| 1 | 4 |
| 2 | 8 |
| 3 | 12 |
| 4 | 16 |
| 5 | 20 |

The interest category depends on the course:

- Programming courses use `interest_programming`.
- Data courses use `interest_data`.
- Networking courses use `interest_networking`.
- Security courses use `interest_security`.
- Business courses use `interest_business`.
- Artificial intelligence courses use `interest_ai`.

### 5. Prerequisite Penalty

The system subtracts **15 points for every unmet prerequisite**.

For example, if a course has two missing prerequisites:

```text
Prerequisite Penalty = 2 x -15 = -30 points
```

### Example Calculation

Suppose a course receives:

- Career alignment: 40 points
- Mathematics performance: 20 points
- Programming performance: 20 points
- Interest rating of 4: 16 points
- One unmet prerequisite: -15 points

```text
Final Score = 40 + 20 + 20 + 16 - 15
Final Score = 81 points
```

## Tie-Breaking and Ranking

Courses are ranked using the following order:

1. Courses matching the student's target career.
2. Higher weighted score.
3. Alphabetical course order when scores are equal.

Courses that the student has already completed are excluded from the recommendation list.

## Requirements and Installation

The project requires:

- Python
- Pandas
- NumPy
- SciPy
- OpenPyXL
- Streamlit

Install the dependencies using PowerShell:

```Python
py -m pip install pandas numpy scipy openpyxl streamlit
```

Use the same Python launcher to run the project so that it uses the interpreter where the packages were installed.

## How to Use

1. Place the Python files and CSV file in the same project folder.
2. Run the app.py through streamlit by using this command in the terminal.
   ```Python
   streamlit run app.py
   ```
4. Upload `course_pathway_records.csv` on the interface.
5. Search for a student profile, example: `S001`.
6. Enter or select the following information:
   - Target career
   - Mathematics grade
   - Programming grade
   - Interest ratings
7. Click **Save Profile**.
8. Review the recommended courses and unmet prerequisites.
9. Save the results as a CSV file.

## Important Notes

- Upload a CSV file using the required column names and format.
- Course names must exactly match the names in the course catalog.
- Separate multiple completed courses with commas.
- The target career must match one of the career paths listed in the system.
- A course with unmet prerequisites should not be treated as immediately eligible.
- Recommendations are based only on the rules and information stored in the system.
- Weighted scoring is a supporting comparison and should not override prerequisite requirements.
- Results are advisory and should be reviewed with an academic adviser.
- The system does not guarantee admission, course availability, graduation completion, or employment.
- If institutional requirements change, the course knowledge base must also be updated.

## Troubleshooting

- **CSV will not load:** Check that the file is saved as `.csv`, uploaded correctly, and not corrupted.
- **Missing columns:** Verify that the CSV contains all required column names.
- **No recommendations:** Review the student's target career and unmet prerequisites.

## Project Limitations

The system's recommendations depend on the accuracy and completeness of the course catalog, prerequisite information, career classifications, and reasoning rules. Incorrect or incomplete CSV records may affect the results. The dataset may not fully represent the academic performance, interests, and circumstances of actual students.

Students' career interests may change over time, and course structures and admission requirements may differ between institutions. The weighted-scoring method may also simplify complex student preferences into numerical values. Therefore, the system should be treated as a decision-support tool and should not replace consultation with a qualified academic adviser.
