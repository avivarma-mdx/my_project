from libs.module1 import submodule1, submodule2
from libs.module2 import submodule3
import json
import os

def main():
    # Load configuration
    config_path = os.path.join(os.path.dirname(__file__), '../config/config.json')
    with open(config_path, 'r') as file:
        config = json.load(file)
    
    print(config['welcome_message'])

    submodule1.function1()
    submodule2.function2()
    submodule3.function3()

if __name__ == "__main__":
    main()