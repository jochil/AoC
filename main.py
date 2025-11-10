import aocd 
from pathlib import Path
import os
import shutil

def main():
    year = input("Enter year: ")
    day = input("Enter day: ")
    
    dir = os.path.join(".", year, f"day{day.zfill(2)}")
    Path(dir).mkdir(parents=True, exist_ok=True)
    print(f"Created directory: {dir}")

    puzzle = aocd.get_puzzle(day=int(day), year=int(year))
    
    input_file = os.path.join(dir, "input")
    with open(input_file, "w") as f:
        f.write(puzzle.input_data)
    print(f"Saved input data to: {input_file}")
    
    for i, example in enumerate(puzzle.examples):
        example_file = os.path.join(dir, f"input_example{i+1}")
        with open(example_file, "w") as f:
            f.write(example.input_data)
        print(f"Saved example {i} data to: {example_file}")
    
    
    code_file = os.path.join(dir, f"day{day.zfill(2)}.py")
    shutil.copy("template.py", code_file)
    print(f"Copied template.py to: {code_file}")
    
    

    
if __name__ == "__main__":
    main()
