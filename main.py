from module1 import submodule1, submodule2
from module2 import submodule3
import json

def main():
    # Load configuration
    with open('config/config.json', 'r') as file:
        config = json.load(file)
    
    print(config['welcome_message'])

    submodule1.function1()
    submodule2.function2()
    submodule3.function3()

if __name__ == "__main__":
    main()

