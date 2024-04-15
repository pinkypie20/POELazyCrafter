pyinstaller --onefile --icon=icon.ico --name=POELazyCrafter --windowed main.py
xcopy /f /y icon.ico dist\
xcopy /f /y Kanit-Regular.ttf dist\