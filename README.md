# Video Summarization using Deep Multi-modal Networks
This repository contains code for video summarization using Neural Network.

# Overview
All of the prior works in the area of video summarization is done either by exploring different heuristically designed criteria in an unsupervised learning method or by using fully supervised algorithms by leveraging human-labeled training datasets. However, It is observed that unsupervised methods fail to produce meaningful summaries because they are blind to video categories. In supervised approaches, getting a large amount of training data is a challenging task and it may lead to a biased model. Different from all the existing methods, we develop a semi-supervised learning approach that takes frame-level annotations. We propose a summarization system which is a combination of both CNN and RNN. The central idea is to use datasets with only frame-level annotations to generate a static summary in the form of significant frames and a dynamic summary in the form of a short snippet. We use two benchmark datasets, TVSum and SumMe to train and test our model.

# How to get the data:
Please download the dataset directly from http://people.csail.mit.edu/yalesong/tvsum.

# Software prerequisite:
requirements.txt file shows all the required software packages needed to run the project

# Steps to run the project
1. Run /preprocess/preprocess.py file to extract frames from a test video. Frame extraction process is now one frame per second and it can be changed as per requirements.
2. Run /video_segmentation/segment_video.py to run segmentation code. For segmentation, exsisting segmentation framework BubbleNet has been used.
