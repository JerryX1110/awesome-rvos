import os
import gdown
import zipfile

# YouTubeVOS
os.makedirs('./refer_youtube_vos', exist_ok=True)
os.makedirs('./refer_youtube_vos/all_frames', exist_ok=True)

print('Downloading YouTubeVOS train...')
gdown.download('https://drive.google.com/uc?id=13Eqw0gVK-AO5B-cqvJ203mZ2vzWck9s4', output='./refer_youtube_vos/train.zip', quiet=False)
print('Downloading YouTubeVOS val...')
gdown.download('https://drive.google.com/uc?id=1o586Wjya-f2ohxYf9C1RlRH-gkrzGS8t', output='./refer_youtube_vos/valid.zip', quiet=False)
print('Downloading YouTubeVOS all frames valid...')
gdown.download('https://drive.google.com/uc?id=1rWQzZcMskgpEQOZdJPJ7eTmLCBEIIpEN', output='./refer_youtube_vos/all_frames/valid.zip', quiet=False)
print('Downloading meta_expressions...')
gdown.download('https://drive.google.com/uc?id=10PwQmpBGhtob_yDt0yJIAopZZQ_wLa3R', output='./refer_youtube_vos/meta_expressions.zip', quiet=False)


print('Extracting YouTube datasets...')
with zipfile.ZipFile('./refer_youtube_vos/train.zip', 'r') as zip_file:
    zip_file.extractall('./refer_youtube_vos/')
with zipfile.ZipFile('./refer_youtube_vos/valid.zip', 'r') as zip_file:
    zip_file.extractall('./refer_youtube_vos/')
with zipfile.ZipFile('./refer_youtube_vos/all_frames/valid.zip', 'r') as zip_file:
    zip_file.extractall('./refer_youtube_vos/all_frames')
with zipfile.ZipFile('./refer_youtube_vos/meta_expressions.zip', 'r') as zip_file:
    zip_file.extractall('./refer_youtube_vos/')

print('Cleaning up YouTubeVOS datasets...')
os.remove('./refer_youtube_vos/train.zip')
os.remove('./refer_youtube_vos/valid.zip')
os.remove('./refer_youtube_vos/all_frames/valid.zip')
os.remove('./refer_youtube_vos/meta_expressions.zip')

print('Done.')
