import json
import os
import sys
# Option 1
# export PYTHONPATH=/home/avi.varma/workspace/my_project

# Option 2
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))


from src.company_name.client.module1 import submodule1, submodule2
from src.company_name.libs.module2 import submodule3

def main():
    # Load configuration
    config_path = os.path.join(os.path.dirname(__file__), '/home/avi.varma/workspace/my_project/config/config.json')
    if os.path.exists(config_path):
        with open(config_path, 'r') as file:
            config = json.load(file)
        print(config.get('welcome_message', 'hello default'))
    else:
        print("hello default")

    submodule1.function1()
    submodule2.function2()
    submodule3.function3()

if __name__ == "__main__":
    main()