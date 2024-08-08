echo " BUILD START"
python3.12 -m install -r requirements.txt


# make migrations
python3.12 manage.py migrate 
python3.12 manage.py collectstatic

echo "BUILD END"