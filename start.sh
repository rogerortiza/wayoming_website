source /home/wayoming/bin/activate
cd /src
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver 0.0.0.0:8000
