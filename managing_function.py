# INTERFACES MANAGING SAMPLE
import mysql.connector
# Example usage
students = []

# Add a student
def add_student(student):
    students.append(student)

# Delete a student by ID
def delete_student(id):
    students[:] = [student for student in students if student.id != id]

# Update a student by ID
def update_student(id):
    # Prompt the user for updated information
    updated_fullname = input("Enter the updated full name: ")
    updated_hovaten = input("Enter the updated last name: ")
    updated_ngaysinh = input("Enter the updated birthdate (YYYY-MM-DD): ")
    updated_gioitinh = input("Enter the updated gender: ")
    updated_sodienthoai = input("Enter the updated phone number: ")
    updated_chungminhthu = input("Enter the updated IDC number: ")
    updated_email = input("Enter the updated email: ")
    updated_noisinh = input("Enter the updated place of birth: ")
    updated_dantoc = input("Enter the updated ethnicity: ")
    updated_tongiao = input("Enter the updated religion: ")
    updated_hokhau = input("Enter the updated permanent address: ")
    updated_macv = int(input("Enter the updated adviser ID: "))
    updated_course_id = int(input("Enter the updated course ID: "))
    updated_mabangdiem = int(input("Enter the updated score ID: "))

    # Create a new Student instance with the updated information
    updated_student = Student(id, updated_fullname, updated_hovaten, updated_ngaysinh, updated_gioitinh, updated_sodienthoai, updated_chungminhthu, updated_email, updated_noisinh, updated_dantoc, updated_tongiao, updated_hokhau, updated_macv, updated_course_id, updated_mabangdiem)

    # Find the student to update and replace it with the new Student instance
    for i, student in enumerate(students):
        if student.id == id:
            students[i] = updated_student
            break

# Sort students by ID
def sort_students():
    students.sort(key=lambda student: student.id)

# Search for a student by ID
def search_student(id):
    for student in students:
        if student.id == id:
            return student
    return None

# View student details
def view_student_details(id):
    student = search_student(id)
    if student:
        print(f"ID: {student.id}, Full Name: {student.fullname}, Last Name: {student.hovaten}, "
              f"Birthdate: {student.ngaysinh}, Gender: {student.gioitinh}, "
              f"Phone Number: {student.sodienthoai}, ID Number: {student.chungminhthu}, "
              f"Email: {student.email}, Place of Birth: {student.noisinh}, "
              f"Ethnicity: {student.dantoc}, Religion: {student.tongiao}, "
              f"Permanent Address: {student.hokhau}, Adviser ID: {student.macv}, "
              f"Course ID: {student.course_id}, Score ID: {student.mabangdiem}")
    else:
        print("Student not found.")

def amount_of_student():
    print(f'Số lượng sinh viên: {len(students)}')

def view_student_detail_list():
    if students:
        for i in range(len(students)):
            view_student_details(students[i].id)
    else:
        print("None")


from tkinter import messagebox
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="qlthongtinsv"
        )
    except Exception as e:
        messagebox.showerror("Lỗi kết nối", "Chưa mở kết nối cơ sở dữ liệu!")
        with open('result.txt', 'w') as f:
            f.write('')
        return None,None
    cursor = connection.cursor()
    return connection, cursor

def get_students_data(cursor):
    cursor.execute("SELECT * FROM sinhvien")
    rows = cursor.fetchall()
    return rows

def get_bangDiem_data(cursor, id):
    cursor.execute("""
        SELECT bangdiemchitiet.mamonhoc, monhoc.tenmon, thanhtich.hocki, 
               thanhtich.diem, bangdiemchitiet.diemgiuaki, bangdiemchitiet.diemcuoiki, sinhvien.trangthai 
        FROM bangdiemchitiet 
        JOIN sinhvien ON bangdiemchitiet.bangdiemchitiet = sinhvien.mabangdiem 
        JOIN thanhtich ON bangdiemchitiet.bangdiemchitiet = thanhtich.bangdiemchitiet 
        JOIN monhoc ON bangdiemchitiet.mamonhoc = monhoc.mamonhoc 
        WHERE bangdiemchitiet.bangdiemchitiet = %s""", (id,))
    rows = cursor.fetchall()
    # for row in rows:
    #     print(row)
    return rows
# Test Function
# student1 = Student(2, "John Doe", "Doe", "2000-01-01", "Male", "1234567890", "12345678", "john.doe@example.com", "New York", "American", "Christian", "123 Main St", 1, 1, 1)
# student2 = Student(1, "Jonathan Brando", "Brando", "2003-02-12", "Male", "1234569870", "123456987", "jonathan.brando@example.com", "Los Angeles", "American", "Buddhism", "13 Secondary St", 2, 2, 4)
# add_student(student1)
# add_student(student2)
# sort_students()
# delete_student(int(input("id")))
# update_student(int(input("id")))
# view_student_detail_list()