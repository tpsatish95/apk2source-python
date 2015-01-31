for /d /r "temp\temp" %%i in (*) do if exist "Decoded_APK\%%~ni" (dir "%%i" | find "0 File(s)" > NUL & if errorlevel 1 move /y "%%i\*.*" "Decoded_APK\%%~ni") else (move /y "%%i" "Decoded_APK")
move /y temp\temp\*.* Decoded_APK
rd /s /q temp\temp