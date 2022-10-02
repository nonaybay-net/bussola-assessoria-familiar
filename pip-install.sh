pip3 install --no-cache-dir --upgrade pip
pip3 install --no-cache-dir --upgrade -r requirements.txt
rm -fv installed.txt; pip3 freeze > installed.txt
