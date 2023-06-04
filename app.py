# # import streamlit as st
# # import sqlite3

# # # Function to create SQLite database and insert data
# # def create_database(course_name, course_description, course_outcomes):
# #     conn = sqlite3.connect('database.db')
# #     cursor = conn.cursor()
    
# #     # Insert data into tables
# #     # Customize the SQL INSERT statements according to your table structure and column names
    
# #     # Insert course details
# #     cursor.execute('''
# #         INSERT INTO Course (course_name, course_description)
# #         VALUES (?, ?)
# #     ''', (course_name, course_description))
# #     course_id = cursor.lastrowid
    
# #     # Insert course outcomes
# #     for outcome in course_outcomes:
# #         cursor.execute('''
# #             INSERT INTO Course_outcome (co_description, co_total_marks, course_id)
# #             VALUES (?, ?, ?)
# #         ''', (outcome['description'], outcome['total_marks'], course_id))
# #         co_id = cursor.lastrowid
        
# #         # Insert internal tests
# #         for test in outcome['tests']:
# #             cursor.execute('''
# #                 INSERT INTO Internal_tests (test_name, course_id)
# #                 VALUES (?, ?)
# #             ''', (test['name'], course_id))
# #             test_id = cursor.lastrowid
            
# #             # Insert test questions
# #             for question in test['questions']:
# #                 cursor.execute('''
# #                     INSERT INTO Test_questions (question_marks, test_id, co_id)
# #                     VALUES (?, ?, ?)
# #                 ''', (question['marks'], test_id, co_id))
    
# #     # Commit the changes and close the connection
# #     conn.commit()
# #     conn.close()

# # # Streamlit app
# # def main():
# #     st.title("Course Outcome Entry")
# #     st.write("---")
    
# #     # # Form inputs
# #     # course_name = st.text_input("Course Name")
# #     # course_description = st.text_area("Course Description")
# #     # course_outcomes = []
    
# #     # num_outcomes = st.number_input("Number of Course Outcomes", min_value=1, value=1)
    
# #     # for i in range(num_outcomes):
# #     #     st.write(f"Course Outcome #{i+1}")
# #     #     outcome_description = st.text_area(f"Course Outcome #{i+1} Description")
# #     #     total_marks = st.number_input(f"Total Marks for Course Outcome #{i+1}")
# #     #     num_tests = st.number_input(f"Number of Internal Tests for Course Outcome #{i+1}", min_value=1, value=1)
        
# #     #     tests = []
# #     #     for j in range(num_tests):
# #     #         st.write(f"Internal Test #{j+1} for Course Outcome #{i+1}")
# #     #         test_name = st.text_input(f"Internal Test #{j+1} Name")
# #     #         num_questions = st.number_input(f"Number of Questions for Internal Test #{j+1}", min_value=1, value=1)
            
# #     #         questions = []
# #     #         for k in range(num_questions):
# #     #             st.write(f"Question #{k+1} for Internal Test #{j+1}")
# #     #             question_marks = st.number_input(f"Marks for Question #{k+1}")
# #     #             questions.append({
# #     #                 'marks': question_marks
# #     #             })
            
# #     #         tests.append({
# #     #             'name': test_name,
# #     #             'questions': questions
# #     #         })
        
# #     #     course_outcomes.append({
# #     #         'description': outcome_description,
# #     #         'total_marks': total_marks,
# #     #         'tests': tests
# #     #     })
    
# #     # Form inputs
# #     course_name = st.text_input("Course Name", key="course_name_input")
# #     course_description = st.text_area("Course Description", key="course_description_input")
# #     course_outcomes = []

# #     num_outcomes = st.number_input("Number of Course Outcomes", min_value=1, value=1)

# #     for i in range(num_outcomes):
# #         st.write(f"Course Outcome #{i+1}")
# #         outcome_description = st.text_area(f"Course Outcome #{i+1} Description", key=f"outcome_description_{i+1}_input")
# #         total_marks = st.number_input(f"Total Marks for Course Outcome #{i+1}", key=f"total_marks_{i+1}_input")
# #         num_tests = st.number_input(f"Number of Internal Tests for Course Outcome #{i+1}", min_value=1, value=1)

# #         tests = []
# #         for j in range(num_tests):
# #             st.write(f"Internal Test #{j+1} for Course Outcome #{i+1}")
# #             test_name = st.text_input(f"Internal Test #{j+1} Name", key=f"test_name_{i+1}_{j+1}_input")
# #             num_questions = st.number_input(f"Number of Questions for Internal Test #{j+1}", min_value=1, value=1)

# #             questions = []
# #             for k in range(num_questions):
# #                 st.write(f"Question #{k+1} for Internal Test #{j+1}")
# #                 question_marks = st.number_input(f"Marks for Question #{k+1}", key=f"question_marks_{i+1}_{j+1}_{k+1}_input")
# #                 questions.append({
# #                     'marks': question_marks
# #                 })

# #             tests.append({
# #                 'name': test_name,
# #                 'questions': questions
# #             })

# #         course_outcomes.append({
# #             'description': outcome_description,
# #             'total_marks': total_marks,
# #             'tests': tests
# #         })


# #     if st.button("Submit"):
# #         create_database(course_name, course_description, course_outcomes)
# #         st.success("Data submitted successfully.")

# # if __name__ == "__main__":
# #     main()


# import streamlit as st
# import sqlite3
# import pandas as pd

# # Function to fetch course details from the database
# def fetch_courses():
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
    
#     # Fetch course names
#     cursor.execute('SELECT course_id, course_name FROM Course')
#     courses = cursor.fetchall()
    
#     # Close the connection
#     conn.close()
    
#     return courses

# # Function to insert course details into the database
# def insert_course_details(course_name, course_description, course_outcomes):
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
    
#     # Insert course details
#     cursor.execute('INSERT INTO Course (course_name, course_description) VALUES (?, ?)', (course_name, course_description))
#     course_id = cursor.lastrowid
    
#     # Insert course outcomes
#     for outcome in course_outcomes:
#         outcome_description = outcome['description']
#         total_marks = outcome['total_marks']
        
#         cursor.execute('INSERT INTO Course_outcome (co_description, co_total_marks, course_id) VALUES (?, ?, ?)', (outcome_description, total_marks, course_id))
#         co_id = cursor.lastrowid
        
#         # Insert internal tests and test questions
#         for test in outcome['tests']:
#             test_name = test['name']
            
#             cursor.execute('INSERT INTO Internal_tests (test_name, course_id) VALUES (?, ?)', (test_name, course_id))
#             test_id = cursor.lastrowid
            
#             for question in test['questions']:
#                 question_marks = question['marks']
                
#                 cursor.execute('INSERT INTO Test_questions (question_marks, test_id, co_id) VALUES (?, ?, ?)', (question_marks, test_id, co_id))
    
#     # Commit the changes and close the connection
#     conn.commit()
#     conn.close()

# # Function to fetch internal tests for a specific course from the database
# def fetch_tests(course_id):
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
    
#     # Fetch test names for the given course
#     cursor.execute('''
#         SELECT test_id, test_name
#         FROM Internal_tests
#         WHERE course_id = ?
#     ''', (course_id,))
#     tests = cursor.fetchall()
    
#     # Close the connection
#     conn.close()
    
#     return tests

# # Function to insert student marks into the database
# def insert_student_marks(course_id, test_id, roll_no, question_marks):
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
    
#     # Insert student marks
#     for question_id, marks_obtained in question_marks.items():
#         cursor.execute('''
#             INSERT INTO Students_Marks (students_rollno, test_id, question_id, marks_obtained)
#             VALUES (?, ?, ?, ?)
#         ''', (roll_no, test_id, question_id, marks_obtained))
    
#     # Commit the changes and close the connection
#     conn.commit()
#     conn.close()

# def fetch_student_marks():
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
    
#     # Fetch student marks
#     cursor.execute('''
#         SELECT sm.marks_id, sm.students_rollno, c.course_name, t.test_name, tq.question_id, tq.question_marks, sm.marks_obtained
#         FROM Students_Marks AS sm
#         JOIN Internal_tests AS t ON sm.test_id = t.test_id
#         JOIN Test_questions AS tq ON sm.question_id = tq.question_id
#         JOIN Course_outcome AS co ON tq.co_id = co.co_id
#         JOIN Course AS c ON co.course_id = c.course_id
#         ORDER BY sm.marks_id DESC
#         LIMIT 10
#     ''')
#     data = cursor.fetchall()
    
#     # Close the connection
#     conn.close()
    
#     # Create a DataFrame from the fetched data
#     df = pd.DataFrame(data, columns=["Marks ID", "Roll No", "Course", "Test", "Question ID", "Question Marks", "Marks Obtained"])
    
#     return df

# # Streamlit app
# def main():
#     st.title("Course and Student Marks Entry")
#     st.write("---")
    
#     # Page selection
#     page = st.sidebar.selectbox("Select Page", ["Course Entry", "Student Marks Entry"])
    
#     if page == "Course Entry":
#         st.header("Course Entry")
        
#         # Course details input
#         course_name = st.text_input("Course Name")
#         course_description = st.text_area("Course Description")
        
#         # Course outcomes input
#         course_outcomes = []
#         num_outcomes = st.number_input("Number of Course Outcomes", min_value=1, value=1)
        
#         for i in range(num_outcomes):
#             outcome_description = st.text_input(f"Course Outcome #{i+1} Description")
#             total_marks = st.number_input(f"Total Marks for Course Outcome #{i+1}", min_value=0, value=100)
            
#             num_tests = st.number_input(f"Number of Internal Tests for Course Outcome #{i+1}", min_value=1, value=1)
#             tests = []
            
#             for j in range(num_tests):
#                 test_name = st.text_input(f"Internal Test #{j+1} Name")
                
#                 num_questions = st.number_input(f"Number of Questions for Internal Test #{j+1}", min_value=1, value=1)
#                 questions = []
                
#                 for k in range(num_questions):
#                     question_marks = st.number_input(f"Marks for Question #{k+1}", min_value=0, value=25)
#                     questions.append({"marks": question_marks})
                
#                 tests.append({"name": test_name, "questions": questions})
            
#             course_outcomes.append({"description": outcome_description, "total_marks": total_marks, "tests": tests})
        
#         # Submit button
#         if st.button("Submit"):
#             insert_course_details(course_name, course_description, course_outcomes)
#             st.success("Course details submitted successfully.")
    
#     elif page == "Student Marks Entry":
#         st.header("Student Marks Entry")
        
#         st.write("---")
#         st.header("Student Marks Entry View")
        
#         # Fetch and display student marks in a table
#         student_marks_df = fetch_student_marks()
#         st.dataframe(student_marks_df)

#         # Fetch course names from the database
#         courses = fetch_courses()
        
#         # Course selection
#         selected_course_id = st.selectbox("Select Course", [course[1] for course in courses])
#         selected_course_index = [course[1] for course in courses].index(selected_course_id)
#         selected_course_id = courses[selected_course_index][0]
        
#         # Fetch internal tests for the selected course
#         tests = fetch_tests(selected_course_id)
        
#         # Test selection
#         selected_test_id = st.selectbox("Select Test", [test[1] for test in tests])
#         selected_test_index = [test[1] for test in tests].index(selected_test_id)
#         selected_test_id = tests[selected_test_index][0]
        
#         # Fetch course outcomes for the selected course
#         conn = sqlite3.connect('database.db')
#         cursor = conn.cursor()
        
#         cursor.execute('''
#             SELECT co.co_id, co.co_description, tq.question_id, tq.question_marks
#             FROM Course_outcome AS co
#             JOIN Test_questions AS tq ON co.co_id = tq.co_id
#             WHERE co.course_id = ? AND tq.test_id = ?
#         ''', (selected_course_id, selected_test_id))
#         data = cursor.fetchall()
        
#         conn.close()

#         # Student roll number input
#         roll_no = st.text_input("Student Roll Number")
        
#         # Prepare student marks input fields
#         question_marks = {}
#         for row in data:
#             co_id = row[0]
#             co_description = row[1]
#             question_id = row[2]
#             question_marks[question_id] = st.number_input(f"{co_description} - Question #{question_id}", value=row[3])
        
#         if st.button("Submit"):
#             insert_student_marks(selected_course_id, selected_test_id, question_marks)
#             st.success("Student marks submitted successfully.")

# if __name__ == "__main__":
#     main()


import streamlit as st
import sqlite3
import pandas as pd

def read_excel_and_store(file):
    # Read the Excel file
    df = pd.read_excel(file)

    # Connect to the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Store the data in the database
    for index, row in df.iterrows():
        # Extract the necessary data from the Excel sheet
        roll_no = row['Roll No']
        course_id = row['Course ID']
        test_id = row['Test ID']
        marks = {}

        # Iterate over the columns to extract marks for each question
        for col in df.columns:
            if col.startswith('Question'):
                question_id = int(col.split()[1])
                marks_obtained = row[col]
                marks[question_id] = marks_obtained

        # Insert the student marks into the database
        for question_id, marks_obtained in marks.items():
            cursor.execute('''
                INSERT INTO Students_Marks (students_rollno, test_id, question_id, marks_obtained)
                VALUES (?, ?, ?, ?)
            ''', (roll_no, test_id, question_id, marks_obtained))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()



# Function to fetch course details from the database
def fetch_courses():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Fetch course names
    cursor.execute('SELECT course_id, course_name FROM Course')
    courses = cursor.fetchall()
    
    # Close the connection
    conn.close()
    
    return courses

# Function to insert course details into the database
def insert_course_details(course_name, course_description, course_outcomes):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Insert course details
    cursor.execute('INSERT INTO Course (course_name, course_description) VALUES (?, ?)', (course_name, course_description))
    course_id = cursor.lastrowid
    
    # Insert course outcomes
    for outcome in course_outcomes:
        outcome_description = outcome['description']
        total_marks = outcome['total_marks']
        
        cursor.execute('INSERT INTO Course_outcome (co_description, co_total_marks, course_id) VALUES (?, ?, ?)', (outcome_description, total_marks, course_id))
        co_id = cursor.lastrowid
        
        # Insert internal tests and test questions
        for test in outcome['tests']:
            test_name = test['name']
            
            cursor.execute('INSERT INTO Internal_tests (test_name, course_id) VALUES (?, ?)', (test_name, course_id))
            test_id = cursor.lastrowid
            
            for question in test['questions']:
                question_marks = question['marks']
                
                cursor.execute('INSERT INTO Test_questions (question_marks, test_id, co_id) VALUES (?, ?, ?)', (question_marks, test_id, co_id))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Function to fetch internal tests for a specific course from the database
def fetch_tests(course_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Fetch test names for the given course
    cursor.execute('''
        SELECT test_id, test_name
        FROM Internal_tests
        WHERE course_id = ?
    ''', (course_id,))
    tests = cursor.fetchall()
    
    # Close the connection
    conn.close()
    
    return tests

# Function to insert student marks into the database
def insert_student_marks(course_id, test_id, question_marks):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Insert student marks
    for question_id, marks_obtained in question_marks.items():
        cursor.execute('''
            INSERT INTO Students_Marks (students_rollno, test_id, question_id, marks_obtained)
            VALUES (?, ?, ?, ?)
        ''', (12345, test_id, question_id, marks_obtained))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def fetch_student_marks():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Fetch student marks
    cursor.execute('''
        SELECT sm.marks_id, sm.students_rollno, c.course_name, t.test_name, tq.question_id, tq.question_marks, sm.marks_obtained
        FROM Students_Marks AS sm
        JOIN Internal_tests AS t ON sm.test_id = t.test_id
        JOIN Test_questions AS tq ON sm.question_id = tq.question_id
        JOIN Course_outcome AS co ON tq.co_id = co.co_id
        JOIN Course AS c ON co.course_id = c.course_id
        ORDER BY sm.marks_id DESC
    ''')
    data = cursor.fetchall()
    
    # Close the connection
    conn.close()
    
    # Create a DataFrame from the fetched data
    df = pd.DataFrame(data, columns=["Marks ID", "Roll No", "Course", "Test", "Question ID", "Question Marks", "Marks Obtained"])
    
    return df



# Streamlit app
def main():
    st.title("Course and Student Marks Entry")
    st.write("---")

    # Page selection
    page = st.sidebar.selectbox("Select Page", ["Course Entry", "Student Marks Entry", "Excel to DB"])



    if page == "Course Entry":
        st.header("Course Entry")

        # Course input fields
        course_name = st.text_input("Course Name", value="Course Name")
        course_description = st.text_area("Course Description", value="Course Description")

        # Course outcome input fields
        num_course_outcomes = st.number_input("Number of Course Outcomes", min_value=1, max_value=5, step=1, value=1)

        course_outcomes = []
        for i in range(num_course_outcomes):
            outcome_description = st.text_input(f"Course Outcome {i+1} Description", value=f"Course Outcome {i+1}", key=f"outcome_description_{i+1}")
            course_outcomes.append(outcome_description)

        if st.button("Insert Course"):
            insert_course(course_name, course_description, course_outcomes)
            st.success("Course details inserted successfully.")

        st.write("---")
        st.subheader("Internal Tests") 

        # Internal test input fields
        num_internal_tests = st.number_input("Number of Internal Tests", min_value=2, max_value=4, step=1, value=2)

        internal_tests = []
        test_questions = []
        for i in range(num_internal_tests):
            test_name = st.text_input(f"Internal Test {i+1} Name", value=f"IT {i+1}", key=f"test_name_{i+1}")
            internal_tests.append(test_name)

            # Question input fields
            num_questions = st.number_input(f"Number of Questions for Internal Test {i+1}", min_value=1, max_value=5, step=1, value=1)
            question_marks = []
            total_marks = 0
            for j in range(num_questions):
                question = st.text_input(f"Question {j+1} for Internal Test {i+1}", value=f"Question {j+1}", key=f"question_{i+1}_{j+1}")
                marks = st.number_input(f"Marks for Question {j+1} (Max 25)", min_value=1, max_value=25, step=1, value=1, key=f"marks_{i+1}_{j+1}")
                question_marks.append(marks)
                total_marks += marks

            if total_marks != 25:
                st.error(f"Total marks for questions under Internal Test {i+1} should be 25. Please adjust the marks.")

            test_questions.append(question_marks)

        # Course entry submit button
        if st.button("Submit Course"):
            if sum([sum(questions) for questions in test_questions]) != 25 * num_internal_tests:
                st.error("Total marks for questions across all internal tests should be 25 per test. Please adjust the marks.")
            else:
                insert_course(course_name, course_description, internal_tests, course_outcomes, test_questions)
                st.success("Course details submitted successfully.")
    # Rest of the code...

    elif page == "Student Marks Entry":
        
        st.write("---")
        st.header("Student Marks Entry View")
        
        # Fetch and display student marks in a table
        student_marks_df = fetch_student_marks()
        st.dataframe(student_marks_df)

        st.header("Student Marks Entry")
        # Fetch course names from the database
        courses = fetch_courses()
        
        # Course selection
        selected_course_id = st.selectbox("Select Course", [course[1] for course in courses])
        selected_course_index = [course[1] for course in courses].index(selected_course_id)
        selected_course_id = courses[selected_course_index][0]
        
        # Fetch internal tests for the selected course
        tests = fetch_tests(selected_course_id)
        
        # Test selection
        selected_test_id = st.selectbox("Select Test", [test[1] for test in tests])
        selected_test_index = [test[1] for test in tests].index(selected_test_id)
        selected_test_id = tests[selected_test_index][0]
        # Student roll number input
        roll_no = st.text_input("Student Roll Number")
        
        # Fetch course outcomes for the selected course
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT co.co_id, co.co_description, tq.question_id, tq.question_marks
            FROM Course_outcome AS co
            JOIN Test_questions AS tq ON co.co_id = tq.co_id
            WHERE co.course_id = ? AND tq.test_id = ?
        ''', (selected_course_id, selected_test_id))
        data = cursor.fetchall()
        
        conn.close()
        
        # Prepare student marks input fields
        question_marks = {}
        for row in data:
            co_id = row[0]
            co_description = row[1]
            question_id = row[2]
            question_marks[question_id] = st.number_input(f"{co_description} - Question #{question_id}", value=row[3])
        
        if st.button("Submit"):
            insert_student_marks(selected_course_id, selected_test_id, question_marks)
            st.success("Student marks submitted successfully.")

    elif page == "Excel to DB":
        st.header("Excel to Database")

        # File upload
        file = st.file_uploader("Upload Excel File", type=["xlsx"])
        if file is not None:
            if st.button("Read Excel and Store"):
                read_excel_and_store(file)
                st.success("Excel data stored in the database successfully.")


if __name__ == "__main__":
    main()
