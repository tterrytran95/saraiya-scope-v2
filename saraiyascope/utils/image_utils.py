import requests, cv2, os, time, sys
# import os
# import cv2

VIDEO = sys.argv[1].split("=")[1] 

URL = 'http://127.0.0.1:8889/post_cur_image'
FRAME_RATE = 10
# assume to run this from saraiya-scope-v2 dir
FRAME_DIR = os.path.abspath('saraiyascope/frames/')
VIDEO_PATH = os.path.abspath('saraiyascope/samples/'+VIDEO)

print('FRAME_DIR', FRAME_DIR)
print('VIDEO_PATH', VIDEO_PATH)



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
            frame_path = FRAME_DIR + '/frame{}.jpg'.format(count)
            out = cv2.imwrite(frame_path, image)
            outframes.append("frame%d.jpg" % count) # just save the name of the image 
            # print('saved {}'.format(frame_path))
        count += 1
    return outframes

def upload_images(frames):
    i = 0
    for f in frames:
    # while i < len(frames):
        img_name = f.split('.jpg')[0]
        # path = FRAME_DIR+"/"+img_name+'.jpg'
        path = FRAME_DIR + "/" + f
        files = {'img': open(path, 'rb')}
        data = {'img_name': img_name+'.jpg'}
        response = requests.post(URL, data = data, files=files)
        # print(response)
        
        i += 1
        if i % 200 == 0:
            print("{} uploaded".format((i/len(frames)*100)))
            time.sleep(5) 
        
def main():
    print('processing frames...')
    frames = get_frames_from_mov(VIDEO_PATH)
    print('%d frames extracted' % len(frames))
    print('uploading images...')
    FRAMES = os.listdir(FRAME_DIR)
    print(len(FRAMES))
    upload_images(FRAMES)
    
main()
