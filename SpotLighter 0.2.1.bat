@echo on

::%LocalAppData%\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\TargetedContentCache\v3\338387\
::py.exe -c "import sys, json; print(json.dumps(json.load(sys.stdin), indent=4))"
::py.exe -c "import sys, json; print(json.load(sys.stdin)['properties']['landscapeImage']['image'])"
::py.exe -c "import sys, json; print(json.load(sys.stdin)['items'][0]['properties']['description']['text'])"

::for file in metadata_dir
::  type file | py -c "
::    import sys, json;
::    metadata = json.load(sys.stdin);
::    #print("source_abspath" "SpotLight\name.jpg") -> %%s
::    print(f"\"{metadata['properties']['landscapeImage']['image']}\" \"SpotLight\\{metadata['items'][0]['properties']['description']['text'].strip()}.jpg\"")
::  "
::    COPY %%s

for %%f in ("%LocalAppData%\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\TargetedContentCache\v3\338387\*") do (
  FOR /F "tokens=* USEBACKQ" %%s IN (`type %%f ^| py -c "import sys, json; metadata = json.load(sys.stdin); print(f\"\\""{metadata['properties']['landscapeImage']['image']}\\"" \\""SpotLight\\{metadata['items'][0]['properties']['description']['text'].strip^(^)}.jpg\\""\"); print(f\"\\""{metadata['properties']['portraitImage']['image']}\\"" \\""SpotLight Portrait\\{metadata['items'][0]['properties']['description']['text'].strip^(^)}.jpg\\""\")"`) DO (
    echo F|Xcopy %%s
    pause
  )
)

EXIT /b
