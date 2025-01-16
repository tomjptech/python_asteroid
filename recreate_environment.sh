#Recreate venv
python3 -m venv venv

#Activate it. You will need to run this from project root in your WSL environment if you ever restart it. The front of your terminal should look something like this: (venv) <user>@<computer>:~/projects/github.com/tomjptech/python_asteroid$
source venv/bin/activate

#Install requirements
pip install -r requirements.txt
