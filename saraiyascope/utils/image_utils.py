import requests, os, cv2, time
# import os
# import cv2

URL = 'http://127.0.0.1:8000/post_cur_image'
FRAME_DIR = '/Users/tuethutran/saraiya-scope-venv/scope/saraiyascope/frames/'
FRAMES = os.listdir(FRAME_DIR)
FRAME_RATE = 5 
VIDEO_PATH = './samples/mochu_ks.mp4'

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
            cv2.imwrite("frames/frame%d.jpg" % count, image)
            outframes.append("frames/frame%d.jpg" % count) # just save the name of the image 
        count += 1
        print(count)
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
        print(response)
        
        i += 1
        if i % 200 == 0:
            print('%2d/% uploaded', int(i / len(frames)))
            time.sleep(5) 
        
def main():
    print('processing frames...')
    # frames = get_frames_from_mov(VIDEO_PATH)
    # print('%d frames extracted', len(frames))
    print('uploading images...')
    upload_images(FRAMES)
    
main()