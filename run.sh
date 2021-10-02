export FLASK_APP=app.py 
npm install
npx tailwindcss-cli@latest build ./api/static/src/style.css -o ./api/static/main.css   
cd api
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
flask run