del .\config\user\.gitkeep
del .\log\.gitkeep
pip install -r requirements.txt
python -m venv env
call .\env\Scripts\activate.bat
pip install -r requirements.txt
pause