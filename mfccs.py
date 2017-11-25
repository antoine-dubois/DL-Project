from python_speech_features.python_speech_features import mfcc
import scipy.io.wavfile as wav
import glob
import os
import numpy as np

'''
train_dir_name = 'train/'
train_dir = os.walk(train_dir_name + 'audio/')
for cur_dir in train_dir:
    cur_dir = cur_dir[0]
    cur_dir_name = cur_dir[len(train_dir_name + 'audio/'):]
    print(cur_dir_name)
    # Create a directory to receive the mfccs for the corresponding sound
    mfccs_dir_name = train_dir_name + 'mfccs/' + cur_dir_name + '/'
    if not os.path.exists(mfccs_dir_name):
        os.makedirs(mfccs_dir_name)
    for filename in glob.glob(os.path.join(cur_dir + '/', '*.wav')):
        (rate, sig) = wav.read(filename)
        mfcc_feat = mfcc(sig, rate)
        # Write the file with mfccs
        new_filename = filename[len(mfccs_dir_name):-4]
        np.save(mfccs_dir_name + new_filename, mfcc_feat)
'''

test_dir_name = 'test/'
audio_dir = test_dir_name + 'audio/'
mfccs_dir = test_dir_name + 'mfccs/'
for filename in glob.glob(os.path.join(audio_dir, '*.wav')):
    (rate, sig) = wav.read(filename)
    mfcc_feat = mfcc(sig, rate)
    # Write the file with mfccs
    new_filename = filename[len(audio_dir):-4]
    np.save(mfccs_dir + new_filename, mfcc_feat)