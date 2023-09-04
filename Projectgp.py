import os
txt_files = []
txt_files2 = []
def Switch_case(choice):
    if choice==1:
        add_Patient_Record()
    elif choice==2:
        show_saved_records()
    elif choice==3:
        open_saved_records()
    elif choice==4:
        delete_existing_record()
    else:
        print("Invalid choise")

def add_Patient_Record():
    User_name=input("Enter the user name who is filling this form : ")
    patient_name=input("Enter the patient name : ")
    while(True):
        patient_age=int(input("Enter the patient age : "))
        if patient_age > 0:
            break;
        else:
            print("Enter a valid age !")
    while (True):
        patient_gender = input("Enter gender of the patient in (Male/Female/Others) : ").strip().lower()
        if patient_gender in ("male","female","other"):
            break;
        else:
            print("Enter a valid gender ! ")
    patient_blood_group=input("Enter the blood group of patient : ")
    patient_phnum=int(input("Enter the phone number of patient : "))
    patient_disease=input("Enter the disease of the patient")
    doctor_handling_patient=input(("Enter the Doctor name who is handeling the patient : "))

    print("\nPlease review the entered data : ")
    print("User Name :", User_name)
    print("Patient Name :", patient_name)
    print("Patient Age :", patient_age)
    print("Patient Gender :", patient_gender)
    print("Blood Group :", patient_blood_group)
    print("Phone Number :", patient_phnum)
    print("Patient Disease :", patient_disease)
    print("Doctor Handling Patient :", doctor_handling_patient)

    while True:
        confirm = input("\nIs the data is  correct and you want to save? (yes/no): ").strip().lower()
        if confirm == "yes":
            file_name = input("Enter the file in which you want to save the data and please add the extension also : ")
            with open(file_name, "a") as file:
                file.write(f"User Name : {User_name}\n")
                file.write(f"Patient Name : {patient_name}\n")
                file.write(f"Patient Age : {patient_age}\n")
                file.write(f"Patient Gender : {patient_gender}\n")
                file.write(f"Blood Group : {patient_blood_group}\n")
                file.write(f"Phone Number : {patient_phnum}\n")
                file.write(f"Patient Disease : {patient_disease}\n")
                file.write(f"Doctor Handling Patient : {doctor_handling_patient}\n\n")
            print("Data has been saved to the file.")
            break
        elif confirm == "no":
            # Data is incorrect, ask the user which field to edit
            field_to_edit = input("Which field would you like to edit? ").strip().lower()
            if field_to_edit == "user name":
                User_name = input("Enter the corrected user name: ")
            elif field_to_edit == "patient name":
                patient_name = input("Enter the corrected patient name: ")
            elif field_to_edit == "patient age":
                patient_age = int(input("Enter the corrected patient age: "))
            elif field_to_edit == "patient gender":
                patient_gender = input("Enter the corrected patient gender (Male/Female/Others): ").strip().lower()
            elif field_to_edit == "blood group":
                patient_blood_group = input("Enter the corrected blood group of patient: ")
            elif field_to_edit == "phone number":
                patient_phnum = int(input("Enter the corrected phone number of patient: "))
            elif field_to_edit == "patient disease":
                patient_disease = input("Enter the corrected patient disease: ")
            elif field_to_edit == "doctor handling patient":
                doctor_handling_patient = input("Enter the corrected Doctor name who is handling the patient: ")
            else:
                print("Invalid field name. Please enter a valid field to edit.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def show_saved_records():
    current_dir = os.getcwd()
    files = os.listdir(current_dir)

    txt_files = [file for file in files if file.endswith(".txt")]
    print("\nSaved File Names:")
    for idx, file_name in enumerate(txt_files, 1):
        print(f"{idx}.{file_name} \n")

def  open_saved_records():
    current_dir = os.getcwd()
    files = os.listdir(current_dir)
    txt_files = [file for file in files if file.endswith(".txt")]
    file_choise=int(input("Enter the file number or id : "))
    try:
        if 1<=file_choise <= len(txt_files):
            file_name=txt_files[file_choise-1]
            open_record(file_name)
        else:
            print("Invalid file name !!")
    except ValueError:
        print("Invalid input. Please enter a valid file number !!")

def open_record(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            print("\nPatient Records in", file_name)
            print(file.read())
    else:
        print("File not found.")


def delete_existing_record():

        file_name = input("Enter the file name you want to delete: ")
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"File {file_name} deleted successfully.")
        else:
            print("File not found. Cannot delete the file.")

while(True):
    print("User option:\n1.Add patient Record\n2.Show saved Records\n3.Open saved Records\n4.Delete existing record\n5.EXIT")
    choice = int(input("Enter your choice: "))
    Switch_case(choice)
    if choice == 5:
        break;
#Hey
