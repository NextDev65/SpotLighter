@echo off

Xcopy "%LocalAppData%\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets" "SpotLight_temp" /q /i /s /e /k /r /y /b /d

cd SpotLight_temp
:: if < 150000 bytes, del
for /f  "usebackq delims=;" %%A in (`dir /b *.*`) do If %%~zA LSS 150000 del "%%A"
ren *.* *.jpg
cd ..

MOVE "SpotLight\*" "SB"
::Xcopy "SpotLight" "SB" /q /i /s /e /k /r /y /b /d
RMDIR /s /q "SpotLight\"

EXIT /b
