# main.py

from alternate_min_max.rearranger import rearrange

def run_demo():
    print("Alternate Min-Max Rearrangement\n")

    while True:
        user_input = input("Enter a list of numbers separated by commas (or type 'exit' to quit): ").strip()

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            # Convert string input to list of integers
            arr = [int(x.strip()) for x in user_input.split(",") if x.strip()]
            result = rearrange(arr)
            print(f"Rearranged Output: {result}\n")
        except ValueError:
            print("Please enter a valid list of numbers separated by commas.\n")

if __name__ == "__main__":
    run_demo()
