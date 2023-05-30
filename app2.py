import streamlit as st
import pandas as pd
import sqlite3

# Connect to the database
conn = sqlite3.connect('db2.db')
cursor = conn.cursor()

# Function to insert data into the database
def insert_data_to_db(data):
    try:
        # Extract data from the input
        class_id = data['Class ID']
        test_id = data['Test ID']
        sub_id = data['Subject ID']
        question_id = data['Question ID']
        question_marks = data['Question Marks']
        co_attainment = data['CO Attainment']

        # Insert data into the DataMaster table
        cursor.execute('''
            INSERT INTO DataMaster (class_id, test_id, sub_id, question_id, question_marks, co_attainment)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (class_id, test_id, sub_id, question_id, question_marks, co_attainment))

        conn.commit()
        st.success("Data inserted successfully.")
    except Exception as e:
        st.error(f"Error occurred: {str(e)}")

# Read specific cells from the Excel file
def read_excel_file(file, sheet_name):
    try:
        # Read the selected sheet into a DataFrame
        df = pd.read_excel(file, sheet_name=sheet_name)

        # Extract the required data from the DataFrame
        data = {
            'Class ID': df.iloc[7, 0],
            'Test ID': df.iloc[17, 2],
            'Subject ID': df.iloc[9, 0]
        }

        # Retrieve the questions, marks, and CO attainment values
        for col in range(3, 9):
            question_id = df.iloc[18, col]
            question_marks = df.iloc[19, col]
            co_attainment = df.iloc[20, col]

            # Check if the question ID is not empty
            if pd.notna(question_id):
                # Insert the data into the database
                data['Question ID'] = question_id
                data['Question Marks'] = question_marks
                data['CO Attainment'] = co_attainment

                insert_data_to_db(data)
            else:
                # Break the loop if an empty cell is encountered
                break

    except Exception as e:
        st.error(f"Error occurred: {str(e)}")


# Streamlit app
def main():
    st.title("Data Upload")
    st.write("---")

    # Page selection
    page = st.sidebar.selectbox("Select Page", ["Upload Excel File"])

    if page == "Upload Excel File":
        st.header("Upload Excel File")
        file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

    if file is not None:
        # Read the selected sheet from the uploaded Excel file
        sheet_names = pd.ExcelFile(file).sheet_names
        selected_sheet = st.selectbox("Select Sheet", sheet_names)
        read_excel_file(file, selected_sheet)

# Run the app
if __name__ == "__main__":
    main()
