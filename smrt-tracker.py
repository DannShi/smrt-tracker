import json

def load_tasks(filename="tasks.json"):
    """Load tasks from a JSON file."""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    

def save_tasks(tasks, filename="tasks.json"):
    """Save tasks to a JSON file."""
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=2)


def main():
    tasks = load_tasks()
    print("Welcome to Smrt Tracker!")
    # TODO: Add menu and task logic here
    print(f"{len(tasks)} tasks loaded.")

if __name__ == "__main__":
    main()

# THis is a test commit for iMac to test that everything in git is running.
