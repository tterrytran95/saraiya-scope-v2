import requests, os, cv2, time
# import os
# import cv2

URL = 'http://127.0.0.1:8000/post_cur_image'
FRAME_DIR = os.getcwd().replace('/utils', '') + '/frames/'
FRAMES = os.listdir(FRAME_DIR)
FRAME_RATE = 10
VIDEO_PATH = os.getcwd().replace('/utils', '') + '/samples/mochu_ks.mp4'

"""
    * film is 9mins 6 seconds @ 60 fps 
    * (9mins * 60sec/mins) + 6sec = 546sec
    * 546sec * 60frames/sec = 32760 frames
    * 32760 / FRAME_RATE = 16380
    * round down to 32000 frames to be safe 
"""
def get_frames_from_mov(path):
    vidObj = cv2.VideoCapture(path) # path to video file
    count = 0 # count variable for sanity check
    success = 1 
    outframes = [] # list out outframes
    while success:
        success, image = vidObj.read() # vidObj object calls read # function extract frames
        if count % FRAME_RATE == 0 and success: # saves the frames with frame-count
            out = cv2.imwrite(FRAME_DIR + 'frame%d.jpg' % count, image)
            outframes.append("frame%d.jpg" % count) # just save the name of the image 
            print('saved', "frame%d" % count)
        count += 1
    return outframes

def upload_images(frames):
    i = 0
    for f in frames:
    # while i < len(frames):
        img_name = f.split('.jpg')[0]
        path = FRAME_DIR+img_name+'.jpg'
        files = {'img': open(path, 'rb')}
        data = {'img_name': img_name}
        response = requests.post(URL, data = data, files=files)
        # print(response)
        
        i += 1
        if i % 200 == 0:
            print("%d uploaded" % (i / len(frames)))
            time.sleep(5) 
        
def main():
    print('processing frames...')
    frames = get_frames_from_mov(VIDEO_PATH)
    print('%d frames extracted', len(frames))
    print('uploading images...')
    print(len(FRAMES))
    upload_images(FRAMES)
    
main()