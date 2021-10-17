
import subprocess

def create_python_code():
    subprocess.call(["touch" ,"ml.py","/Users"])
    # python code must be written in this part
    with open("/Users/ml.py","w") as file:
        file.write("print('hello world :)')")
        file.close()
    subprocess.call("python /Users/ml.py;rm /Users/ml.py",shell=True)