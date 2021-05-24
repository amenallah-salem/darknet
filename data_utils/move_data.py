import shutil
import os

def copy_images(source, destination): 
  print("moving data from the source...")
  print('Listing files and directories Before moving folders:',os.listdir(source))
  # Source path  
  # Move the content of  
  # source to destination  
  dest = shutil.move(source, destination)      
  # Print path of newly  
  # created file  
  print("Listing files and directories in Destination path:{} after moving folders{} ".format(dest, os.listdir(destination)))


if __name__=='__main__':
  
  try:

    list_files = []
    for files in os.listdir(os.getcwd()):
      list_files.append(files)
    if 'images' in list_files:
      pass
    else:
      print("Directory images doen't exist... creating images/ folder ")
      os.mkdir('images')
      print("successfully creating images/ directory .....")

    IMAGES_PATH= './images' #directory to store the images into the repository
    original_images_path = '/content/drive/MyDrive/images'#images are originally storred to drive 

    copy_images(source= os.path.join(original_images_path,'train'),
            destination=IMAGES_PATH)

    copy_images(source=os.path.join(original_images_path,'test'),
            destination=IMAGES_PATH)
    print('Images moved succesfuly to', IMAGES_PATH)
  except Exception as e :
    print("An Exception has occured: ", e )