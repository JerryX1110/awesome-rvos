import os
import gdown
import tarfile


print('The script will download and extract the segment one by one')
#reply = input('[y] to confirm, others to exit: ')
#if reply != 'y':
 #   exit()

links = [
    'https://drive.google.com/uc?id=14DNamenZsvZnb32NFBNkZCGene5D2oaE'
]

names = [
    'a2d_annotation_with_instances.zip'
]

for i, link in enumerate(links):
    print('Downloading segment %d/%d ...' % (i, len(links)))
    gdown.download(link, output='./%s' % names[i], quiet=False)
    print('Extracting...')
    #with tarfile.open('./%s' % names[i], 'r') as tar_file:
    #    tar_file.extractall('./%s' % names[i])
    #print('Cleaning up...')
    #os.remove('../%s' % names[i])


print('Done.')
