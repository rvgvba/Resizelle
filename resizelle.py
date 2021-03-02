import os
from PIL import Image
from threading import Thread


class Resizelle(object):
    def __init__(self):
        self.__res_x = None
        self.__res_y = None
        self.__input_dir = None
        self.__output_dir = None
        self.__img_urls = []

    def read_phone_size(self, x_size, y_size):
        """
        reading phone wallpaper size
        """
        self.__res_x = x_size
        self.__res_y = y_size

    def read_pic_folder_path(self, selected_input_path):
        """
        reading the folder containg the images to be resized
        """
        try:
            if os.path.isdir(selected_input_path.replace('"', "")):
                self.__input_dir = selected_input_path.replace('"', "")
            else:
                raise NotADirectoryError
        except NotADirectoryError:
            print('No valid directory selected.')

    def set_output_dir(self):
        """
        creating the folder where the resized images will be sent
        """
        new_folder_path = self.__input_dir.split()[0] + os.path.sep + 'resized_imgs'
        if not os.path.exists(new_folder_path):
            os.mkdir(new_folder_path)

        self.__output_dir = new_folder_path

    def read_imgs_paths(self):
        """
        appending each image path to the paths list
        """
        for img in os.listdir(self.__input_dir):
            if img.split('.')[-1] in ['jpg', 'png', 'bmp']:
                self.__img_urls.append(img)

    def resize_image(self, img_url):
        """
        resizeing the each image
        """
        img_path = self.__input_dir + os.path.sep + img_url
        temp_img = Image.open(img_path)
        fixed_height = self.__res_y

        height_percent = (fixed_height / float(temp_img.size[1]))
        width_size = int((float(temp_img.size[0]) * float(height_percent)))

        temp_img_final = temp_img.resize((width_size, fixed_height), Image.NEAREST)
        new_img_path = self.__output_dir + os.path.sep + img_url.split('.')[0] + '_resized.' + img_url.split('.')[-1]
        if not os.path.exists(new_img_path):
            temp_img_final.save(new_img_path)

    def parse_images(self):
        """
        processing each image using threading
        """

        # creating a thread for each image processing and append it to the list of threads
        list_threads = []
        for img_path in self.__img_urls:
            resize_thread = Thread(target=self.resize_image, args=(img_path,))
            list_threads.append(resize_thread)

        # schedule each thread in the list to start
        for th in list_threads:
            th.start()

        # wait until each thread is done
        for th in list_threads:
            th.join()

        print("Image conversion fully done.")

