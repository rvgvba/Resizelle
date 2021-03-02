from resizelle import Resizelle

try:
    print('{:^88}'.format('Welcome to the Resizelle App'))
    phone_w = input('Please insert phone wallpaper width:\n')
    phone_h = input('Please insert phone wallpaper height:\n')
    pic_path = input('Please copy-paste the path of the directory containg the pics:\n')

    if not phone_w.isdigit() or phone_w is None:
        raise IOError

    if not phone_h.isdigit() or phone_h is None:
        raise IOError

    if pic_path is None:
        raise IOError

    redz = Resizelle()
    redz.read_phone_size(int(phone_w), int(phone_h))
    redz.read_pic_folder_path(pic_path)
    redz.set_output_dir()
    redz.read_imgs_paths()
    redz.parse_images()

except IOError:
    print("Please make sure you compelted the WIDTH & HEIGHT of the wallpaper!")

except Exception as e:
    print(e.__doc__)

finally:
    print("Process done and closed.")


