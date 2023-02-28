# %LocalAppData%\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\TargetedContentCache\v3\338387\
# py.exe -c "import sys, json; print(json.dumps(json.load(sys.stdin), indent=4))"
# py.exe -c "import sys, json; print(json.load(sys.stdin)['properties']['landscapeImage']['image'])"
# py.exe -c "import sys, json; print(json.load(sys.stdin)['items'][0]['properties']['description']['text'])"
import os
import json
import re


def pic_copy(source, desc, orientation):
    if orientation == 'landscape':
        dest = f'SpotLight\\{desc}.jpg'
    else:
        dest = f'SpotLight Portrait\\{desc}.jpg'

    if not os.path.exists(dest):
        # print(source, dest)
        os.system(f'echo F|Xcopy /m "{source}" "{dest}"')
    else:
        if re.match(r'^.*\((\d+)\)\.jpg', dest):
            desc_i = re.sub(r'(\()(\d+)(\))', lambda d: d.group(1) + str(int(d.group(2)) + 1) + d.group(3), desc, count=1)
        else:
            desc_i = desc + ' (1)'
        pic_copy(source, desc_i, orientation)


# metadata directory
metadata_dir = os.path.join(os.getenv('LocalAppData'), 'Packages\\Microsoft.Windows'
                                                       '.ContentDeliveryManager_cw5n1h2txyewy\\LocalState'
                                                       '\\TargetedContentCache\\v3\\338387\\')

# iterate over metadata files
for fname in os.listdir(metadata_dir):
    with open(os.path.join(metadata_dir, fname), encoding='utf-8') as fstream: metadata = json.load(fstream)
    landscapeImage = metadata['properties']['landscapeImage']['image']
    portraitImage = metadata['properties']['portraitImage']['image']
    description = metadata['items'][0]['properties']['description']['text'].strip()

    # os.system(f'copy "{landscapeImage}" "SpotLight\\{description}.jpg"')
    # subprocess.call(f'copy "{landscapeImage}" "SpotLight\\{description}.jpg"', shell=True)
    # shutil.copy2(landscapeImage, f"SpotLight\\{description}.jpg")

    pic_copy(landscapeImage, description, 'landscape')
    pic_copy(portraitImage, description, 'portrait')
