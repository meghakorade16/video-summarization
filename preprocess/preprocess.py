import csv

import cv2 as cv


##
# Function to extract frames
# @param capture, VideoCapture object
# @param duration, duration for frame extraction (unit: seconds)
#
def extract_frames(capture, duration):
    success, image = capture.read()
    fps = round(capture.get(cv.CAP_PROP_FPS))
    frames = (fps * duration)
    indexes = []
    count = 1
    while success:
        frame_id = int(round(capture.get(1)))
        success, image = capture.read()
        if frame_id % frames == 1:
            cv.imwrite("./dataset/frames_test_video/frame%d.jpg" % count, image)  # save frame as JPEG file
            count += 1
            indexes.append(frame_id)
    capture.release()
    print("Frames division for {} complete.".format(instance_name))
    print("Total frames in {} is {}".format(instance_name, count - 1))
    return indexes


##
# Function to extract frames
# @param capture, VideoCapture object
# @param indexes, mapping indexes of frame number
#
def process_annotation(capture, indexes):
    # fps = round(capture.get(cv.CAP_PROP_FPS))
    # total_frames = int(capture.get(cv.CAP_PROP_FRAME_COUNT))
    annotations = []
    with open('../dataset/annotations/tvsum-anno.tsv') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
            important_score = []
            temp = row[2].split(',')
            for index in indexes:
                important_score.append(temp[index - 1])
            annotations.append({'video_id': row[0], 'category_code': row[1], 'importance_score': important_score})
        return annotations


if __name__ == '__main__':
    instance_name = './dataset/test_videos/_xMr-HKMfVA.mp4'
    video_capture = cv.VideoCapture(instance_name)
    indexes = extract_frames(video_capture, 1)
    # indexes = [1, 31, 61, 91, 121, 151, 181, 211, 241, 271, 301, 331, 361, 391, 421, 451, 481, 511, 541, 571, 601,
    # 631, 661, 691, 721, 751, 781, 811, 841, 871, 901, 931, 961, 991, 1021, 1051, 1081, 1111, 1141, 1171, 1201,
    # 1231, 1261, 1291, 1321, 1351, 1381, 1411, 1441, 1471, 1501, 1531, 1561, 1591, 1621, 1651, 1681, 1711, 1741,
    # 1771, 1801, 1831, 1861, 1891, 1921, 1951, 1981, 2011, 2041, 2071, 2101, 2131, 2161, 2191, 2221, 2251, 2281,
    # 2311, 2341, 2371, 2401, 2431, 2461, 2491, 2521, 2551, 2581, 2611, 2641, 2671, 2701, 2731, 2761, 2791, 2821,
    # 2851, 2881, 2911, 2941, 2971, 3001, 3031, 3061, 3091, 3121, 3151, 3181, 3211, 3241, 3271, 3301, 3331, 3361,
    # 3391, 3421, 3451, 3481, 3511, 3541, 3571, 3601, 3631, 3661, 3691, 3721, 3751, 3781, 3811, 3841, 3871, 3901,
    # 3931, 3961, 3991, 4021, 4051, 4081, 4111, 4141, 4171, 4201, 4231, 4261, 4291, 4321, 4351, 4381, 4411, 4441]
    process_annotation(video_capture, indexes)
