from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import cv2
from scipy import misc
import tensorflow as tf
import numpy as np
import os
import facenet
import align.detect_face


# 计算数据库后台所有的embadding
def computing_compare_emb():
    with tf.Graph().as_default():
        with tf.Session() as sess:
            # 加载facenet参数
            model = '../20170512-110547/'
            facenet.load_model(model)
            images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
            embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
            phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
            image = []
            emb_dir = '../emb_img'
            global all_obj_name
            all_obj_name = []
            for i in os.listdir(emb_dir):
                all_obj_name.append(i)
                img = misc.imread(os.path.join(emb_dir, i), mode='RGB')
                print('img.shape:', img.shape)
                prewhitened = facenet.prewhiten(img)  # 预白化去除冗余信息
                image.append(prewhitened)
                nrof_images = nrof_images + 1
            images = np.stack(image)  # 沿着新轴连接数组的序列。
            feed_dict = {images_placeholder: images, phase_train_placeholder: False}
            # 计算对比图片embadding，embdadding是一个128维的张量
            compare_emb = sess.run(embeddings, feed_dict=feed_dict)
            # print('compare_emb:', compare_emb)
            print('compare_emb_shape:', compare_emb.shape)
            compare_num = len(compare_emb)
        return compare_num, compare_emb


def main():
    with tf.Graph().as_default():
        with tf.Session() as sess:
            # 加载facenet参数
            model = '../20170512-110547/'
            facenet.load_model(model)
            images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
            embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
            phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")

            image = []
            nrof_images = 0
            emb_dir = '../emb_img'
            all_obj_name = []
            for i in os.listdir(emb_dir):
                all_obj_name.append(i)
                img = misc.imread(os.path.join(emb_dir, i), mode='RGB')
                print('img.shape:', img.shape)
                prewhitened = facenet.prewhiten(img)  # 预白化去除冗余信息
                image.append(prewhitened)
                nrof_images = nrof_images + 1

            images = np.stack(image)  # 沿着新轴连接数组的序列。
            feed_dict = {images_placeholder: images, phase_train_placeholder: False}
            # 计算对比图片embadding，embdadding是一个128维的张量
            compare_emb = sess.run(embeddings, feed_dict=feed_dict)
            # print('compare_emb:', compare_emb)
            print('compare_emb_shape:', compare_emb.shape)
            compare_num = len(compare_emb)

            # compare_num, compare_emb = computing_compare_emb()
            capture = cv2.VideoCapture(0)
            cv2.namedWindow("camera", 1)
            while True:
                ret, frame = capture.read()
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # 获取 判断标识 bounding_box crop_image
                mark, bounding_box, crop_image = load_and_align_data(rgb_frame, 160, 44)
                if (1):
                    if (mark):
                        # 计算视频帧的embadding
                        feed_dict = {images_placeholder: crop_image, phase_train_placeholder: False}
                        emb = sess.run(embeddings, feed_dict=feed_dict)
                        print("emb shape:", emb.shape)
                        pre_person_num = len(emb)  # 存在多个人脸，embadding.shape为[n,128]，（n:人数）

                        find_obj = []
                        print('识别到的人数:', pre_person_num)
                        print('数据库名字：:', all_obj_name)
                        # 为bounding_box 匹配标签
                        for i in range(pre_person_num):
                            dist_list = []  # 距离列表
                            for j in range(compare_num):
                                # 求误差(欧氏距离)，存储每个embadding-compare_embadding对应的distance
                                dist = np.sqrt(np.sum(np.square(np.subtract(emb[i, :], compare_emb[j, :]))))
                                dist_list.append(dist)
                            min_value = min(dist_list)  # 求视频帧和对比图直接最小的差值，即表示为最相似的图片
                            if (min_value > 0.65):  # margin==0.65
                                find_obj.append('Unknow')
                            else:
                                # 从dist.list里面选择最接近的index并在obj_name里面查找对应的name
                                find_obj.append(all_obj_name[dist_list.index(min_value)])
                                # 在frame上绘制边框和文字
                        for rec_position in range(pre_person_num):
                            # 利用回归边框给input image画框
                            cv2.rectangle(frame,
                                          (bounding_box[rec_position, 0], bounding_box[rec_position, 1]),
                                          (bounding_box[rec_position, 2], bounding_box[rec_position, 3]),
                                          (0, 255, 0),
                                          1, 8, 0)

                            cv2.putText(
                                frame,
                                find_obj[rec_position],
                                (bounding_box[rec_position, 0], bounding_box[rec_position, 1]),
                                cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                1,
                                (0, 0, 255),
                                thickness=2,
                                lineType=2)
                # return frame
                        cv2.imshow('camera', frame)
                key = cv2.waitKey(3)
                if key == 27:
                    break
            capture.release()
            cv2.destroyWindow("camera")


with tf.Graph().as_default():
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=1.0)
    sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))
    with sess.as_default():
        pnet, rnet, onet = align.detect_face.create_mtcnn(sess, None)


def load_and_align_data(img, image_size, margin):
    minsize = 20
    threshold = [0.6, 0.7, 0.7]
    factor = 0.709
    # bounding_boxes shape:(1,5)  type:np.ndarray
    bounding_boxes, _ = align.detect_face.detect_face(img, minsize, pnet, rnet, onet, threshold, factor)
    # 如果未发现目标 直接返回
    if len(bounding_boxes) < 1:
        return 0, 0, 0
    det = bounding_boxes
    det = det.astype(int)
    crop = []
    for i in range(len(bounding_boxes)):
        temp_crop = img[det[i, 1]:det[i, 3], det[i, 0]:det[i, 2], :]
        aligned = misc.imresize(temp_crop, (image_size, image_size))
        prewhitened = facenet.prewhiten(aligned)
        crop.append(prewhitened)
    # np.stack 将crop由一维list变为二维
    crop_image = np.stack(crop)
    return 1, det, crop_image  # mark标记位置，回归边框，切割图片


if __name__ == '__main__':
    main()
