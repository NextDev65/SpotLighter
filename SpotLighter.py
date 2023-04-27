import os       # cmd commands
import json     # json parsing
import re       # regex
import hashlib  # file hashing
import base64   # hash decoding
import shutil

# DEBUG? 1.
DEBUG = 0
# metadata directory
metadata_dir = os.path.join(os.getenv('LocalAppData'), 'Packages\\Microsoft.Windows'
                                                       '.ContentDeliveryManager_cw5n1h2txyewy\\LocalState'
                                                       '\\TargetedContentCache\\v3\\338387\\')


def pic_copy(src, title, orientation, src_hash):
    if orientation == 'landscape':
        dest = f'SpotLight\\{title}.jpg'
    else:
        dest = f'SpotLight Portrait\\{title}.jpg'

    if DEBUG:
        print(src, dest)

    # if destination file does not already exist, copy
    if not os.path.exists(dest):
        # os.system(f'echo F|Xcopy /m "{src}" "{dest}"')
        # subprocess.call(f'copy "{src}" "{dest}"', shell=True)
        shutil.copy2(src, dest)
    # else destination file already exists and is not duplicate, enumerate title and recursively call pic_copy
    else:
        '''
        # duplicate check via hex sha256 hash
        src_hash = base64.b64decode(src_hash).hex()
        with open(dest, 'rb') as fstream:
            dest_hash = hashlib.sha256(fstream.read()).hexdigest()
        '''
        # duplicate check via b64 encoded sha256 hash
        # src_hash = src_hash
        with open(dest, 'rb') as fstream:
            dest_hash = base64.b64encode(hashlib.sha256(fstream.read()).digest()).decode('utf-8')
        if src_hash != dest_hash:
            if re.match(r'^.*\((\d+)\)\.jpg', dest):
                title_i = re.sub(r'(\()(\d+)(\))',
                                 lambda d: d.group(1) + str(int(d.group(2)) + 1) + d.group(3),
                                 title, count=1)
            else:
                title_i = title + ' (1)'
            pic_copy(src, title_i, orientation, src_hash)
        else:
            if DEBUG:
                print("Skipped!")


def mkdir(path='.'):
    if not os.path.exists(path):
        os.makedirs(path)


def main():
    # make dir 'SpotLight' and 'SpotLight Portrait'
    mkdir('SpotLight')
    mkdir('SpotLight Portrait')
    # iterate over metadata files
    for fname in os.listdir(metadata_dir):
        with open(os.path.join(metadata_dir, fname), 'r', encoding='utf-8') as fstream:
            metadata = json.load(fstream)
        landscape_path = metadata['properties']['landscapeImage']['image']
        portrait_path = metadata['properties']['portraitImage']['image']
        description = metadata['items'][0]['properties']['description']['text'].strip()
        landscape_hash = metadata['properties']['landscapeImage']['sha256']
        portrait_hash = metadata['properties']['portraitImage']['sha256']

        pic_copy(landscape_path, description, 'landscape', landscape_hash)
        pic_copy(portrait_path, description, 'portrait', portrait_hash)


if __name__ == '__main__':
    main()
