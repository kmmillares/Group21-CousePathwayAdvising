import pandas as pd

# Career interest mappings
career_interest_fields = {
    "Software Developer": "interest_programming",
    "Software Engineer": "interest_programming",
    "Data Analyst": "interest_data",
    "Network Administrator": "interest_networking",
    "Network Analyst": "interest_networking",
    "Business Systems Analyst": "interest_business",
    "App Developer": "interest_programming",
    "Web Developer": "interest_programming",
    "Database Administrator": "interest_data",
    "Cybersecurity Analyst": "interest_security",
    "Mobile Developer": "interest_programming",
    "Game Developer": "interest_game_development",
    "Data Scientist": "interest_data",
    "AI Engineer": "interest_ai"
}


# Available career paths
careers = [
    "Software Developer",
    "Software Engineer",
    "Data Analyst",
    "Network Administrator",
    "Network Analyst",
    "Business Systems Analyst",
    "App Developer",
    "Web Developer",
    "Database Administrator",
    "Cybersecurity Analyst",
    "Mobile Developer",
    "Game Developer",
    "Data Scientist",
    "AI Engineer"
]


# Course catalog and prerequisites
course_catalog = {
    "Introduction to Computing": {
        "prerequisites": [],
        "career_area": [
            "Software Developer", "Software Engineer", "Data Analyst",
            "Network Administrator", "Network Analyst",
            "Business Systems Analyst", "App Developer", "Web Developer",
            "Database Administrator", "Cybersecurity Analyst",
            "Mobile Developer", "Game Developer",
            "Data Scientist", "AI Engineer"
        ]
    },

    "Computer Programming": {
        "prerequisites": [],
        "career_area": [
            "Software Developer", "Software Engineer", "Data Analyst",
            "Network Administrator", "Network Analyst",
            "Business Systems Analyst", "App Developer", "Web Developer",
            "Database Administrator", "Cybersecurity Analyst",
            "Mobile Developer", "Game Developer",
            "Data Scientist", "AI Engineer"
        ]
    },

    "Introduction to Human Computer Interaction": {
        "prerequisites": ["Introduction to Computing"],
        "career_area": [
            "Software Developer", "Software Engineer",
            "Data Analyst", "Business Systems Analyst",
            "App Developer", "Web Developer",
            "Mobile Developer", "Game Developer"
        ]
    },

    "Data Structures And Alggorithm": {
        "prerequisites": ["Computer Programming"],
        "career_area": [
            "Software Developer", "Software Engineer",
            "Data Analyst", "Data Scientist",
            "AI Engineer", "Game Developer"
        ]
    },

    "Professional Development": {
        "prerequisites": [],
        "career_area": [
            "Software Developer", "Software Engineer",
            "Data Analyst", "Network Administrator",
            "Network Analyst", "Business Systems Analyst",
            "Database Administrator", "Cybersecurity Analyst"
        ]
    },

    "Information Management": {
        "prerequisites": ["Data Structures And Alggorithm"],
        "career_area": [
            "Database Administrator", "Data Analyst",
            "Business Systems Analyst", "Cybersecurity Analyst",
            "Data Scientist", "AI Engineer"
        ]
    },

    "Discrete Structures": {
        "prerequisites": ["Introduction to Computing"],
        "career_area": [
            "Software Developer", "Software Engineer",
            "Data Analyst", "Data Scientist",
            "AI Engineer", "Cybersecurity Analyst"
        ]
    },

    "Computer Systems and Architecture": {
        "prerequisites": ["Introduction to Computing"],
        "career_area": [
            "Software Engineer", "Network Administrator",
            "Network Analyst", "Cybersecurity Analyst",
            "Database Administrator"
        ]
    },

    "Object Oriented Programming": {
        "prerequisites": ["Computer Programming"],
        "career_area": [
            "Software Developer", "Software Engineer",
            "Mobile Developer", "App Developer",
            "Web Developer", "Game Developer"
        ]
    },

    "Analytics Fundamentals": {
        "prerequisites": [],
        "career_area": [
            "Data Analyst", "Business Systems Analyst",
            "Data Scientist", "AI Engineer",
            "Database Administrator"
        ]
    },

    "Operating Systems": {
        "prerequisites": ["Computer Programming"],
        "career_area": [
            "Software Engineer", "Software Developer",
            "Network Administrator", "Network Analyst",
            "Cybersecurity Analyst", "Database Administrator"
        ]
    },

    "Mobile Programming": {
        "prerequisites": ["Object Oriented Programming"],
        "career_area": [
            "Mobile Developer", "App Developer",
            "Software Developer"
        ]
    },

    "Algorithms": {
        "prerequisites": [
            "Data Structures And Alggorithm",
            "Object Oriented Programming"
        ],
        "career_area": [
            "Software Developer", "Software Engineer",
            "Game Developer", "Data Scientist",
            "AI Engineer", "Data Analyst"
        ]
    },

    "Database System with Administration": {
        "prerequisites": ["Information Management"],
        "career_area": [
            "Database Administrator", "Data Analyst",
            "Business Systems Analyst", "Data Scientist",
            "Cybersecurity Analyst"
        ]
    },

    "Applications Development": {
        "prerequisites": ["Mobile Programming"],
        "career_area": [
            "Software Developer", "Mobile Developer",
            "App Developer", "Web Developer"
        ]
    },

    "Networks and Communication": {
        "prerequisites": ["Introduction to Computing"],
        "career_area": [
            "Network Administrator", "Network Analyst",
            "Cybersecurity Analyst", "Software Engineer",
            "Database Administrator"
        ]
    },

    "Automata and Formal Languages": {
        "prerequisites": ["Computer Programming"],
        "career_area": [
            "Software Engineer", "Software Developer",
            "AI Engineer", "Data Scientist"
        ]
    },

    "Structured Programming": {
        "prerequisites": ["Object Oriented Programming"],
        "career_area": [
            "Software Developer", "Software Engineer",
            "Game Developer", "Web Developer",
            "Mobile Developer"
        ]
    },

    "Modeling and Simulation": {
        "prerequisites": ["Computer Programming"],
        "career_area": [
            "Software Engineer", "Game Developer",
            "Data Scientist", "AI Engineer",
            "Data Analyst"
        ]
    },

    "Software Engineering": {
        "prerequisites": [
            "Computer Programming",
            "Information Management"
        ],
        "career_area": [
            "Software Engineer", "Software Developer",
            "Web Developer", "App Developer",
            "Business Systems Analyst", "Mobile Developer"
        ]
    },

    "Programming Tools and Techniques": {
        "prerequisites": [
            "Structured Programming",
            "Object Oriented Programming"
        ],
        "career_area": [
            "Software Developer", "Software Engineer",
            "Web Developer", "Mobile Developer",
            "App Developer", "Game Developer"
        ]
    },

    "Programming Languages": {
        "prerequisites": ["Automata and Formal Languages"],
        "career_area": [
            "Software Developer", "Software Engineer",
            "Web Developer", "Game Developer",
            "Mobile Developer", "App Developer"
        ]
    },

    "Image Processing": {
        "prerequisites": ["Programming Tools and Techniques"],
        "career_area": [
            "AI Engineer", "Data Scientist",
            "Software Engineer", "Data Analyst"
        ]
    },

    "Information Security and Assurance": {
        "prerequisites": ["Networks and Communication"],
        "career_area": [
            "Cybersecurity Analyst", "Network Administrator",
            "Network Analyst", "Database Administrator"
        ]
    },

    "Business Process for Computing": {
        "prerequisites": ["Information Management"],
        "career_area": [
            "Business Systems Analyst", "Data Analyst",
            "Database Administrator", "Software Developer"
        ]
    },

    "Intelligent Systems": {
        "prerequisites": [
            "Modeling and Simulation",
            "Automata and Formal Languages"
        ],
        "career_area": [
            "Software Engineer", "AI Engineer",
            "Data Scientist", "Data Analyst",
            "Software Developer"
        ]
    }
}


# Interest category assigned to each course
course_interest_fields = {
    # Programming and software development
    "Computer Programming": "interest_programming",
    "Data Structures And Alggorithm": "interest_programming",
    "Object Oriented Programming": "interest_programming",
    "Algorithms": "interest_programming",
    "Structured Programming": "interest_programming",
    "Programming Tools and Techniques": "interest_programming",
    "Programming Languages": "interest_programming",
    "Software Engineering": "interest_programming",
    "Operating Systems": "interest_programming",
    "Automata and Formal Languages": "interest_programming",

    # Web, mobile, applications, and design
    "Introduction to Human Computer Interaction": "interest_programming",
    "Mobile Programming": "interest_programming",
    "Applications Development": "interest_programming",

    # Data and databases
    "Analytics Fundamentals": "interest_data",
    "Information Management": "interest_data",
    "Database System with Administration": "interest_data",
    "Image Processing": "interest_data",
    "Modeling and Simulation": "interest_data",
    "Intelligent Systems": "interest_ai",

    # Networking and security
    "Computer Systems and Architecture": "interest_networking",
    "Networks and Communication": "interest_networking",
    "Information Security and Assurance": "interest_security",

    # Business systems
    "Business Process for Computing": "interest_business",

    # General courses
    "Introduction to Computing": "interest_programming",
    "Professional Development": "interest_business",
    "Discrete Structures": "interest_data"
}


def parse_completed_courses(value):
    """Convert a student's completed courses into a list."""
    if pd.isna(value) or str(value).strip().lower() in ("none", "nan", ""):
        return []

    return [
        course.strip()
        for course in str(value).split(",")
        if course.strip() in course_catalog
    ]


def check_prerequisites(course, completed_courses):
    """Return prerequisites that the student has not completed."""
    required = course_catalog[course]["prerequisites"]

    return [
        prerequisite
        for prerequisite in required
        if prerequisite not in completed_courses
    ]


def rule_based_adviser(student):
    """Recommend courses based on career alignment and prerequisites."""
    completed = parse_completed_courses(student["completed_courses"])
    career = student["target_career"]

    recommendations = []

    for course, information in course_catalog.items():
        if course in completed:
            continue

        unmet = check_prerequisites(course, completed)
        career_match = career in information["career_area"]

        if career_match and not unmet:
            recommendations.append({
                "course": course,
                "status": "Recommended",
                "unmet_prerequisites": [],
                "reason": (
                    "The course matches the target career and "
                    "all prerequisites are satisfied."
                )
            })

        elif career_match and unmet:
            recommendations.append({
                "course": course,
                "status": "Blocked",
                "unmet_prerequisites": unmet,
                "reason": (
                    "The course matches the target career, "
                    "but prerequisite courses are missing."
                )
            })

    return recommendations


def generate_course_sequence(student):
    """Generate a course sequence that respects prerequisites."""
    completed = set(
        parse_completed_courses(student["completed_courses"])
    )
    career = student["target_career"]

    relevant_courses = {
        course
        for course, information in course_catalog.items()
        if career in information["career_area"]
        and course not in completed
    }

    sequence = []
    scheduled = set()
    remaining = set(relevant_courses)

    while remaining:
        ready_courses = []

        for course in course_catalog:
            if course not in remaining:
                continue

            prerequisites = course_catalog[course]["prerequisites"]

            if all(
                prerequisite in completed or prerequisite in scheduled
                for prerequisite in prerequisites
            ):
                ready_courses.append(course)

        if not ready_courses:
            break

        for course in ready_courses:
            sequence.append(course)
            scheduled.add(course)
            remaining.remove(course)

    unmet_prerequisites = set()

    for course in remaining:
        for prerequisite in course_catalog[course]["prerequisites"]:
            if prerequisite not in completed and prerequisite not in scheduled:
                unmet_prerequisites.add(prerequisite)

    return sequence, sorted(unmet_prerequisites)


def weighted_score(student, course):
    """Calculate a course recommendation score."""
    score = 0
    career = student["target_career"]

    # Career alignment
    if career in course_catalog[course]["career_area"]:
        score += 40

    # Academic performance
    math_courses = [
        "Discrete Structures",
        "Data Structures And Alggorithm",
        "Algorithms",
        "Analytics Fundamentals",
        "Modeling and Simulation",
        "Image Processing",
        "Intelligent Systems"
    ]

    if course in math_courses and student["math_grade"] >= 85:
        score += 20
    elif student["math_grade"] >= 85:
        score += 10

    programming_courses = [
        "Computer Programming",
        "Object Oriented Programming",
        "Structured Programming",
        "Programming Tools and Techniques",
        "Programming Languages",
        "Software Engineering",
        "Algorithms",
        "Mobile Programming",
        "Applications Development",
        "Operating Systems"
    ]

    if course in programming_courses and student["programming_grade"] >= 85:
        score += 20
    elif student["programming_grade"] >= 85:
        score += 10

    # Interest alignment
    interest_field = course_interest_fields.get(course)

    if interest_field and interest_field in student:
        interest_level = student[interest_field]

        interest_points = {
            1: 4,
            2: 8,
            3: 12,
            4: 16,
            5: 20
        }

        score += interest_points.get(interest_level, 0)

    # Penalize courses with unmet prerequisites
    completed = parse_completed_courses(student["completed_courses"])
    unmet = check_prerequisites(course, completed)

    score -= len(unmet) * 15

    return score


def rank_by_weighted_score(student):
    """Rank incomplete courses using weighted scores."""
    rankings = []

    completed = parse_completed_courses(student["completed_courses"])

    for course in course_catalog:
        if course in completed:
            continue

        score = weighted_score(student, course)
        unmet = check_prerequisites(course, completed)

        rankings.append({
            "course": course,
            "weighted_score": score,
            "unmet_prerequisites": ", ".join(unmet) if unmet else "None",
            "career_match": (
                student["target_career"]
                in course_catalog[course]["career_area"]
            )
        })

    result = pd.DataFrame(rankings)

    if result.empty:
        return result

    return result.sort_values(
        by=["career_match", "weighted_score", "course"],
        ascending=[False, False, True]
    ).reset_index(drop=True)