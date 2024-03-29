import datetime
import os
import sys

from Codebase.video_segmentation.osvos_marshal_seg import osvos_segment

sys.path.insert(0, os.path.join(os.getcwd(), 'video_segmentation'))


##
# Method that segments video objects
#
#
def main():
    print("Calling main function..")
    main_dir = os.getcwd()
    data_dir = os.path.join(main_dir, 'dataset')
    # raw_data_dir = os.path.join(data_dir, 'rawData')

    # Get list of video directories.
    video_list = sorted(next(os.walk(data_dir))[1])

    # Cycle through each video.
    for i, video_name in enumerate(video_list):
        # Misc. setup.
        video_dir = os.path.join(data_dir, video_name)
        annotation_dir = os.path.join(video_dir, 'annotations')
        if os.path.isdir(os.path.join(video_dir, 'src')):
            image_dir = os.path.join(video_dir, 'src')
        else:
            image_dir = os.path.join(video_dir, 'src')
        # Get results file location from parameter file.
        path_unique = datetime.datetime.now().strftime("%y-%m-%d")
        # If OS-based error for directory, consider using os.path.join()
        result_dir = os.path.join(main_dir, 'results', 'results_' +
                                  path_unique, 'fgbgSeg')
        # Get OSVOS result for each video.
        osvos_segment(image_dir, annotation_dir, result_dir, video_name, data_dir, iters=500)
        print('Finished with ' + video_name + ' segmenation.\n\n')

    # Placeholder for post-processing (e.g., n-object hypothesis, n-pixel mask padding).
    print('\n\nFinished with all segmentations!\n\n')


if __name__ == "__main__":
    main()
