import streamlit as st
import pandas as pd
import io

from course_pathway_advising import (
    careers,
    course_catalog,
    generate_course_sequence,
    rule_based_adviser,
    rank_by_weighted_score,
)

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Course Recommendation System",
    page_icon="🎓",
    layout="wide",
)

st.title("🎓 Course Recommendation System")
st.caption(
    "Personalized course recommendations based on career goals, "
    "academic performance, interests, and prerequisites."
)


# --------------------------------------------------
# STUDENT CSV FILE
# --------------------------------------------------

st.sidebar.subheader("Student Dataset")

uploaded_file = st.sidebar.file_uploader(
    "Select your student CSV file",
    type=["csv"],
    key="student_csv_upload",
)

if uploaded_file is not None:
    try:
        uploaded_file.seek(0)
        loaded_df = pd.read_csv(uploaded_file)

        # Keep the uploaded dataset in session state so it remains
        # available when Streamlit reruns the application.
        st.session_state["student_dataset"] = loaded_df

        st.sidebar.success(
            f"Loaded {len(loaded_df)} student records."
        )

    except Exception as error:
        st.sidebar.error(f"Could not read CSV: {error}")

        if "student_dataset" not in st.session_state:
            st.session_state["student_dataset"] = None

elif "student_dataset" not in st.session_state:
    st.session_state["student_dataset"] = None

student_df = st.session_state.get("student_dataset")


# --------------------------------------------------
# INTEREST FIELDS
# --------------------------------------------------

interest_fields = {
    "Programming": "interest_programming",
    "Business": "interest_business",
    "Networking": "interest_networking",
    "Data Analysis": "interest_data",
    "Cybersecurity": "interest_security",
    "Game Development": "interest_game_development",
    "Artificial Intelligence": "interest_ai",
}


if "student_profile" not in st.session_state:
    st.session_state["student_profile"] = None


# --------------------------------------------------
# STUDENT PROFILE SEARCH
# --------------------------------------------------

st.sidebar.header("Find Your Profile")
st.sidebar.write("Enter your Student ID to retrieve your recommendations.")

if "student_profile" not in st.session_state:
    st.session_state["student_profile"] = None

if student_df is not None:
    if "student_id" not in student_df.columns:
        st.sidebar.error(
            "Your CSV must contain a 'student_id' column."
        )
    else:
        with st.sidebar.form("student_search_form"):
            search_id = st.text_input(
                "Student ID",
                placeholder="Enter your Student ID",
            ).strip()

            search_submitted = st.form_submit_button(
                "Search Profile",
                type="primary",
                use_container_width=True,
            )

        if search_submitted:
            if not search_id:
                st.sidebar.warning("Please enter your Student ID.")
                st.session_state["student_profile"] = None
            else:
                matches = student_df[
                    student_df["student_id"]
                    .astype("string")
                    .str.strip()
                    .str.casefold()
                    .eq(search_id.casefold())
                    .fillna(False)
                ]

                if matches.empty:
                    st.sidebar.error(
                        "Student ID not found. Please check your ID."
                    )
                    st.session_state["student_profile"] = None

                elif len(matches) > 1:
                    st.sidebar.error(
                        "This Student ID appears more than once in the CSV. "
                        "Please correct the duplicate records."
                    )
                    st.session_state["student_profile"] = None

                else:
                    student = matches.iloc[0].to_dict()

                    required_defaults = {
                        "student_id": search_id,
                        "target_career": careers[0],
                        "completed_courses": "",
                        "math_grade": 85,
                        "programming_grade": 85,
                        "interest_programming": 3,
                        "interest_business": 3,
                        "interest_networking": 3,
                        "interest_data": 3,
                        "interest_security": 3,
                        "interest_game_development": 3,
                        "interest_ai": 3,
                    }

                    for field, default_value in required_defaults.items():
                        value = student.get(field, default_value)

                        if pd.isna(value):
                            value = default_value

                        student[field] = value

                    student["student_id"] = str(
                        student["student_id"]
                    ).strip()
                    student["target_career"] = str(
                        student["target_career"]
                    )
                    student["completed_courses"] = str(
                        student["completed_courses"]
                    )

                    try:
                        numeric_fields = [
                            "math_grade",
                            "programming_grade",
                            "interest_programming",
                            "interest_business",
                            "interest_networking",
                            "interest_data",
                            "interest_security",
                            "interest_game_development",
                            "interest_ai",
                        ]

                        for field in numeric_fields:
                            student[field] = int(float(student[field]))

                    except (ValueError, TypeError, OverflowError):
                        st.sidebar.error(
                            "This profile contains invalid grade or interest "
                            "values. Please check the CSV."
                        )
                        st.session_state["student_profile"] = None
                    else:
                        if student["target_career"] not in careers:
                            st.sidebar.error(
                                "The profile contains an unrecognized career. "
                                "Please check the CSV."
                            )
                            st.session_state["student_profile"] = None
                        else:
                            st.session_state["student_profile"] = student
                            st.sidebar.success("Profile found!")

else:
    st.sidebar.info(
        "Upload your student CSV file first."
    )


# --------------------------------------------------
# SHOW LOADED PROFILE
# --------------------------------------------------

# Show a message, but allow new students to fill in the form.
student = st.session_state.get("student_profile")

if student is not None:
    st.success(
        f"Profile loaded for Student ID: {student['student_id']}"
    )


# --------------------------------------------------
# CLEAR CURRENT PROFILE
# --------------------------------------------------

if st.session_state.get("student_profile") is not None:
    if st.sidebar.button(
        "🗑️ Clear Current Profile",
        use_container_width=True,
    ):
        st.session_state["student_profile"] = None

        # Clear the search field so another profile can be searched.
        st.session_state.pop("student_search_id", None)

        st.rerun()

# --------------------------------------------------
# STUDENT PROFILE FORM
# --------------------------------------------------

existing_profile = st.session_state.get("student_profile") or {}

saved_courses = existing_profile.get("completed_courses", "")

if isinstance(saved_courses, str):
    saved_courses = [
        course.strip()
        for course in saved_courses.split(",")
        if course.strip() in course_catalog
    ]
else:
    saved_courses = []

with st.sidebar:
    st.header("Student Profile")
    st.write("Edit a loaded profile or create a new one.")

    with st.form("student_profile_form"):
        student_id = st.text_input(
            "Student ID",
            value=str(existing_profile.get("student_id", "")),
        )

        target_career = st.selectbox(
            "Target Career",
            options=careers,
            index=(
                careers.index(existing_profile["target_career"])
                if existing_profile.get("target_career") in careers
                else 0
            ),
        )

        completed_courses = st.multiselect(
            "Courses Already Completed",
            options=sorted(course_catalog.keys()),
            default=saved_courses,
        )

        st.subheader("Academic Performance")

        math_grade = st.slider(
            "Mathematics Grade",
            0, 100,
            int(existing_profile.get("math_grade", 85)),
        )

        programming_grade = st.slider(
            "Programming Grade",
            0, 100,
            int(existing_profile.get("programming_grade", 85)),
        )

        st.subheader("Interest Ratings")
        interests = {}

        for label, field in interest_fields.items():
            interests[field] = st.slider(
                label,
                1, 5,
                int(existing_profile.get(field, 3)),
                key=f"rating_{field}",
            )

        submitted = st.form_submit_button(
            "Save Profile & Generate Recommendations",
            type="primary",
            use_container_width=True,
        )


# --------------------------------------------------
# SAVE NEW OR UPDATED PROFILE
# --------------------------------------------------

if submitted:
    student = {
        "student_id": student_id.strip(),
        "target_career": target_career,
        "completed_courses": ", ".join(completed_courses),
        "math_grade": math_grade,
        "programming_grade": programming_grade,
        **interests,
    }

    if not student["student_id"]:
        st.sidebar.error("Please enter a Student ID.")

    elif student_df is None:
        st.sidebar.error(
            "Please upload the student CSV before saving."
        )

    else:
        updated_df = student_df.copy()

        if "student_id" not in updated_df.columns:
            st.sidebar.error(
                "The uploaded CSV must contain a student_id column."
            )
        else:
            # Add any profile columns missing from the CSV.
            for column in student:
                if column not in updated_df.columns:
                    updated_df[column] = pd.NA

            matching_ids = (
                updated_df["student_id"]
                .astype("string")
                .str.strip()
                .str.casefold()
                .eq(student["student_id"].casefold())
                .fillna(False)
            )

            # Replace a saved profile, or append a new one.
            updated_df = updated_df.loc[~matching_ids].copy()

            updated_df = pd.concat(
                [updated_df, pd.DataFrame([student])],
                ignore_index=True,
            )

            st.session_state["student_dataset"] = updated_df
            st.session_state["student_profile"] = student
            st.session_state["student_csv_download_ready"] = True

            st.sidebar.success(
                f"Profile saved for {student['student_id']}."
            )

# --------------------------------------------------
# DOWNLOAD UPDATED STUDENT CSV
# --------------------------------------------------

student_df = st.session_state.get("student_dataset")

if (
    student_df is not None
    and st.session_state.get("student_csv_download_ready", False)
):
    st.sidebar.download_button(
        label="Download Updated Student CSV",
        data=student_df.to_csv(index=False).encode("utf-8"),
        file_name="student_data_updated.csv",
        mime="text/csv",
        key="download_updated_student_csv",
        use_container_width=True,
    )


# --------------------------------------------------
# WAIT FOR STUDENT INPUT
# --------------------------------------------------

student = st.session_state.get("student_profile")

if student is None:
    st.info(
        "Upload your student CSV, complete the profile in the sidebar, "
        "and click Save Profile & Generate Recommendations."
    )
    st.stop()

if not isinstance(student, dict):
    st.error("The student profile is invalid. Please submit it again.")
    st.stop()

# --------------------------------------------------
# GENERATE RESULTS
# --------------------------------------------------

sequence, unmet = generate_course_sequence(student)

rule_results = rule_based_adviser(student)
ranked_results = rank_by_weighted_score(student).copy()

recommended_courses = {
    result["course"]
    for result in rule_results
    if result["status"] == "Recommended"
}


# Format weighted ranking results.
if "unmet_prerequisites" in ranked_results.columns:
    ranked_results["unmet_prerequisites"] = (
        ranked_results["unmet_prerequisites"]
        .fillna("None")
        .astype(str)
    )

ranked_results = ranked_results.rename(
    columns={
        "course": "Course",
        "weighted_score": "Score",
        "unmet_prerequisites": "Missing Prerequisites",
        "career_match": "Career Match",
    }
)

ranked_results.insert(
    0,
    "Rank",
    range(1, len(ranked_results) + 1),
)

ranked_results["Rule-Based Status"] = ranked_results["Course"].apply(
    lambda course: (
        "Recommended"
        if course in recommended_courses
        else "Not recommended"
    )
)

ranked_results["Eligibility"] = (
    ranked_results["Missing Prerequisites"].apply(
        lambda value: (
            "Check prerequisites"
            if value != "None"
            else "No missing prerequisites listed"
        )
    )
)


# Prepare rule-based results.
rule_df = pd.DataFrame(rule_results)

if not rule_df.empty:
    rule_df = rule_df.rename(
        columns={
            "course": "Course",
            "status": "Status",
            "unmet_prerequisites": "Missing Prerequisites",
            "reason": "Explanation",
        }
    )

    rule_df["Missing Prerequisites"] = (
        rule_df["Missing Prerequisites"].apply(
            lambda items: ", ".join(items) if items else "None"
        )
    )


# --------------------------------------------------
# REPORT HEADER
# --------------------------------------------------

st.subheader("Recommendation Report")

col1, col2, col3 = st.columns(3)

col1.metric("Target Career", student["target_career"])
col2.metric("Courses in Learning Plan", len(sequence))
col3.metric("Prerequisites Requiring Attention", len(unmet))

completed_display = student["completed_courses"] or "None"

with st.expander("View Student Profile"):
    profile_df = pd.DataFrame(
        [
            {"Field": "Student ID", "Value": student["student_id"]},
            {"Field": "Target Career", "Value": student["target_career"]},
            {"Field": "Completed Courses", "Value": completed_display},
            {"Field": "Mathematics Grade", "Value": student["math_grade"]},
            {
                "Field": "Programming Grade",
                "Value": student["programming_grade"],
            },
        ]
    )

    st.dataframe(
        profile_df,
        hide_index=True,
        use_container_width=True,
    )


# --------------------------------------------------
# RESULTS TABS
# --------------------------------------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "📚 Learning Plan",
        "✅ Rule-Based Results",
        "📊 Weighted Ranking",
        "📝 Summary",
        "📥 Download Report",
    ]
)

# --------------------------------------------------
# TAB 1: LEARNING PLAN
# --------------------------------------------------

with tab1:
    st.subheader("Recommended Course Sequence")

    st.write(
        "Courses are arranged so prerequisites can be completed "
        "before dependent courses, where the sequence generator "
        "can resolve those dependencies."
    )

    if sequence:
        sequence_df = pd.DataFrame(
            {
                "Step": range(1, len(sequence) + 1),
                "Recommended Course": sequence,
            }
        )

        st.dataframe(
            sequence_df,
            hide_index=True,
            use_container_width=True,
        )
    else:
        st.warning(
            "No courses could be scheduled. Check completed courses "
            "and prerequisite requirements."
        )

    st.subheader("Prerequisites Requiring Attention")

    if unmet:
        st.warning(
            "Some courses could not be scheduled because their "
            "prerequisites remain unresolved."
        )

        st.dataframe(
            pd.DataFrame({"Prerequisite to Review": unmet}),
            hide_index=True,
            use_container_width=True,
        )
    else:
        st.success(
            "No unresolved prerequisites were reported by the sequence generator."
        )


# --------------------------------------------------
# TAB 2: RULE-BASED RESULTS
# --------------------------------------------------

with tab2:
    st.subheader("Rule-Based Recommendations")

    st.write(
        "These results check whether a course matches your target career "
        "and whether its prerequisites have been completed."
    )

    if not rule_df.empty:
        status_filter = st.selectbox(
            "Filter by status",
            ["All", "Recommended", "Blocked"],
            key="rule_status_filter",
        )

        filtered_rules = rule_df.copy()

        if status_filter != "All":
            filtered_rules = filtered_rules[
                filtered_rules["Status"] == status_filter
            ]

        st.dataframe(
            filtered_rules,
            hide_index=True,
            use_container_width=True,
        )
    else:
        st.info(
            "No courses in the catalog match this career under the "
            "current rule-based method."
        )


# --------------------------------------------------
# TAB 3: WEIGHTED RANKING
# --------------------------------------------------

with tab3:
    st.subheader("Weighted-Scoring Ranking")

    st.write(
        "Courses are ranked by their calculated scores. A higher score "
        "does not necessarily mean that a course is ready to take."
    )

    career_filter = st.selectbox(
        "Career match",
        ["All courses", "Matching career only", "Other careers"],
        key="career_filter",
    )

    ranked_display = ranked_results.copy()

    if career_filter == "Matching career only":
        ranked_display = ranked_display[
            ranked_display["Career Match"] == True
        ]
    elif career_filter == "Other careers":
        ranked_display = ranked_display[
            ranked_display["Career Match"] == False
        ]

    st.dataframe(
        ranked_display,
        hide_index=True,
        use_container_width=True,
    )

    st.download_button(
        label="Download Ranking as CSV",
        data=ranked_display.to_csv(index=False).encode("utf-8"),
        file_name="course_recommendation_ranking.csv",
        mime="text/csv",
    )


# --------------------------------------------------
# TAB 4: SUMMARY
# --------------------------------------------------

with tab4:
    st.subheader("Recommendation Summary")

    recommended_count = sum(
        result["status"] == "Recommended"
        for result in rule_results
    )

    blocked_count = sum(
        result["status"] == "Blocked"
        for result in rule_results
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Recommended", recommended_count)
    col2.metric("Blocked", blocked_count)
    col3.metric("Ranked Courses", len(ranked_results))

    st.markdown("### Recommended Learning Plan")

    if sequence:
        for index, course in enumerate(sequence, start=1):
            st.write(f"**{index}.** {course}")
    else:
        st.write("No courses are currently available in the sequence.")

    st.markdown("### Suggested Next Steps")

    if unmet:
        st.write(
            "Review the following prerequisite requirements before "
            "planning the affected courses:"
        )

        for prerequisite in unmet:
            st.write(f"- {prerequisite}")
    else:
        st.write(
            "No unresolved prerequisites were reported for the generated plan."
        )

    st.caption(
        "Recommendations are based on the course catalog and rules "
        "currently defined in the system."
    )


# --------------------------------------------------
# TAB 5: DOWNLOAD RECOMMENDATION REPORT
# --------------------------------------------------

with tab5:
    st.subheader("Download Recommendation Report")

    st.write(
        "Download the complete recommendation report for the currently "
        "accessed student as an Excel workbook."
    )

    # 1. Student profile
    report_profile = pd.DataFrame([
        {"Field": "Student ID", "Value": student["student_id"]},
        {"Field": "Target Career", "Value": student["target_career"]},
        {
            "Field": "Completed Courses",
            "Value": student.get("completed_courses", "") or "None",
        },
        {"Field": "Mathematics Grade", "Value": student["math_grade"]},
        {
            "Field": "Programming Grade",
            "Value": student["programming_grade"],
        },
        *[
            {"Field": label, "Value": student.get(field, "N/A")}
            for label, field in interest_fields.items()
        ],
    ])

    # 2. Learning plan
    learning_plan_df = pd.DataFrame({
        "Step": list(range(1, len(sequence) + 1)),
        "Recommended Course": sequence,
    })

    # 3. Rule-based results: use the original results directly
    rule_report_df = pd.DataFrame(rule_results)

    if not rule_report_df.empty:
        rule_report_df["unmet_prerequisites"] = (
            rule_report_df["unmet_prerequisites"].apply(
                lambda items: ", ".join(items) if items else "None"
            )
        )

    # 4. Weighted ranking: rebuild from the original ranking results
    ranking_report_df = rank_by_weighted_score(student).copy()

    # 5. Unresolved prerequisites
    prerequisites_df = pd.DataFrame({
        "Unresolved Prerequisite": unmet if unmet else ["None"]
    })

    # Generate Excel workbook in memory
    excel_buffer = io.BytesIO()

    with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:
        report_profile.to_excel(
            writer,
            sheet_name="Student Profile",
            index=False,
        )

        learning_plan_df.to_excel(
            writer,
            sheet_name="Learning Plan",
            index=False,
        )

        rule_report_df.to_excel(
            writer,
            sheet_name="Rule-Based Results",
            index=False,
        )

        ranking_report_df.to_excel(
            writer,
            sheet_name="Weighted Ranking",
            index=False,
        )

        prerequisites_df.to_excel(
            writer,
            sheet_name="Prerequisites",
            index=False,
        )

    excel_buffer.seek(0)

    st.download_button(
        label="📥 Download Full Recommendation Report (Excel)",
        data=excel_buffer.getvalue(),
        file_name=f"recommendation_report_{student['student_id']}.xlsx",
        mime=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        ),
        type="primary",
        use_container_width=True,
    )