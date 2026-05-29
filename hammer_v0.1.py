import csv

headers = ["Task Name", "Priority Group", "Target Date", "Progress", "Status", "Notes", "Updates"]

def add_new_goal():
    print("--- Initialize New Goal ---")
    name = input("Task Name: ")
    priority = input("Priority Group (Critical/High/Medium/Low): ")
    target = input("Target Date (MM/DD/YYYY): ")
    with open("hammer_db.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writerow({"Task Name": name, "Priority Group": priority, "Target Date": target, "Progress": "0%", "Status": "Not Started", "Notes": "", "Updates": ""})

def view_all_goals():
    print("n=== CURRENT GOALS ===")
    with open("hammer_db.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"- {row['Task Name']} (Priority: {row['Priority Group']} | Status: {row['Status']})")
def update_goal():
    print("\n=== UPDATE GOAL ===")
    all_goals = []
    with open("hammer_db.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            all_goals.append(row)
            
    target_name = input("Enter the EXACT Task Name to update: ")
    found = False
    
    for goal in all_goals:
        if goal["Task Name"] == target_name:
            print(f"Current Status: {goal['Status']}")
            new_status = input("Enter new Status (e.g., In Progress, Done): ")
            goal["Status"] = new_status  
            found = True
            break
            
    if not found:
        print("Error: Task not found in database.")
        return        
        with open("hammer_db.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(all_goals)
        
    print(f"Success: {target_name} updated.")

def main_menu():
    while True:
        print("\n=== THE HAMMER OS ===")
        print("1. View All Goals")
        print("2. Add New Goal")
        print("3. Update a Goal")
        print("4. Exit System")
        
        choice = input("Enter command (1 or 2 or 3): ")
        
        if choice == "1":
            view_all_goals()
        elif choice == "2":
            add_new_goal()
        elif choice == "3":
            update_goal()
        elif choice == "4":
            print("Shutting down...")
            break
        else:
            print("Invalid command. Try again.")
main_menu()