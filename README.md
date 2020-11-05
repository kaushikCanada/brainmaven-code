# Brainmaven LRU Cache project

LRU cache is a cache removal algorithm where the least recently used items in a cache are removed to allocate space for new additions. The least recently used items reside at the front of the cache while newer items are found at the end. LRU stands for Least Recently Used

## Concept and features

1. This is a very basic implementation of the lru mechanism using doubly linked lists. Not meant to be used for production. However, it captures the essence of the requirement both in terms of interface and correctness. 

2. The data types used in this solution are extremely rudimentary pythonic objects which are memory efficient and cpu friendly.

3. The code is easy to understand and can be run with any standard IDE. In my case I am using our favourite VSCode.

4. The project has been organized in a standard cloud native way. This means this can be promptly mounted on a docker ready to be deployed on Kubernetes. The readme contains enough information to udnerstand the goal of this project and to reproduce the results on your own environment.

5. The unit test cases are giving expected results. However, for sure with extra time, more edge cases and improvements can be made to testing. Ultimately its a resource to ROI equation.

## Project organization

"app" folder contains the code as usual. Caching.py implements the actual cache and testing.py contaisn the test cases. requirements.txt contains the unittest2 library fortesting.

### To make virtual environment
<code>
python3 -m venv env

source env/bin/activate

pip install -r requirements.txt

python testing.py

deactivate
</code>

## Stay safe and good luck to you all !