@echo off

Xcopy "%LocalAppData%\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets" "SpotLight_temp" /q /i /s /e /k /r /y /b /d

cd SpotLight_temp
:: if < 150000 bytes, del
for /f  "usebackq delims=;" %%A in (`dir /b *.*`) do If %%~zA LSS 150000 del "%%A"
ren *.* *.jpg
cd ..

::Xcopy "SpotLight_temp" "SpotLight" /q /i /s /e /k /r /y /b /d
IF NOT EXIST "SpotLight\" (mkdir "SpotLight")
MOVE /Y "SpotLight_temp\*" "SpotLight"
RMDIR /s /q ""SpotLight_temp\"

EXIT /b
