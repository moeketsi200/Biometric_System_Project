from datetime import datetime

def id(ID):
    with open("student_details.txt", "r+") as f:
        next(f) # This skips the header line
        ID = input("Enter your ID: ")
        
        for column in f:
            users = column.strip().split() # This line removes an unwanted characters in the row and splits the remaining characters before putting them in a list
            if users[0].strip() == str(ID).strip(): # The reason why we casted the ID into a string is because all the text in the text file are strings so we need to compare them using strings
                time_entered = datetime.now().strftime("%H:%M:%S")
                time_in = time_entered
                with open("gg.txt", "a") as f:
                 
                 f.write(f"\n{time_entered} {users}")
                
                 return f"Hi {users[1].strip()}. You have entered at {time_entered}"
            
        raise ValueError (f"User {ID} not found") # Raises ValueError if the ID entered by the user is not found 

print(id(5))