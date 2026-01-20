from datetime import datetime


class StudentBiometricSystem:
    def __init__(self, details_file, log_in_file, log_out_file):
        self.details_file = details_file
        self.log_in_file = log_in_file
        self.log_out_file = log_out_file
        self.active_sessions = {}
        self.time_entered = None
        self.time_exited = None

    def get_time(self):
        return datetime.now()

    def user_search(self, student_id):
        with open(self.details_file, "r") as file:
            next(file) 

            for row in file:
                line = row.strip().split()

                if line[0].strip() == str(student_id).strip():
                    return line

        raise ValueError(f"User {student_id} not found")

    def input_entry(self, time_entered, user_details):
        with open(self.log_in_file, "a") as f:
            f.write(f"\n{user_details[1]} {self.time_entered}")

    def output_entry(self, time_exited, user_details):
        with open(self.log_out_file, "a") as e_file:
            e_file.write(f"\n{user_details[1]} {self.time_exited}")

    def sign_in(self):
        
        student_id = input("Enter your ID to sign-in: ")
        if student_id in self.active_sessions:
            return "You are already signed in, sign out to end your day"

        user = self.user_search(student_id)
        if not user: 
            return "Invalid student ID"
        self.time_entered = self.get_time()
        self.active_sessions[student_id] = self.time_entered
        self.input_entry(self.time_entered, user)
        return f"Hi {user[1].strip()}. You have entered at {self.time_entered}"
            
    
    def sign_out(self):
        student_id = input("Enter your ID to sign-out: ")
        if student_id not in self.active_sessions:
            return "You must sign in before sign out"

        user = self.user_search(student_id)
        self.time_exited = self.get_time()
        self.output_entry(self.time_exited, user)
        del self.active_sessions[student_id]

        return f"Hi {user[1].strip()}. You have exited at {self.time_exited}"

    def hours(self):
        if not self.time_entered or not self.time_exited:
            return"Cannot calculate your hours make sure you signed in and signed out"
        
        duration = self.time_exited - self.time_entered
        return (duration.total_seconds()/ 3600)



            
system = StudentBiometricSystem("student_details.txt", "student_log_in.txt", "student_log_out.txt")
print(system.sign_in())
print(system.sign_out())
print("Your hours for the day is...", system.hours())


# print(system.sign_out())
