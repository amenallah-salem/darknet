def _red_config(yaml_dir):
  with open(os.path.join(yaml_dir, "cfg.yaml"), "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)
  return data 

def obj_names(num_classes): #class names 
    with open('./data/custom_obj.names', 'w') as obj_names_file:
      for class_id in range(num_classes):
        obj_names_file.write(class_names[class_id])
        obj_names_file.write('\n')
      obj_names_file.close()

def obj_data(class_names):
  with open('./data/custom_obj.data', 'w')as f :
    f.write('classes = {}'.format(data['num_classes']))
    f.write('\n')
    f.write('train = ./images/train.txt')
    f.write('\n')
    f.write('valid = ./images/train.txt')
    f.write('\n')
    f.write('names =  ./data/custom_obj.names')
    f.write('\n')
    f.write('backup = {}'.format(data['backup']))
    f.write('\n')
    f.close()



if __name__=='__main__':
  import yaml
  import os
  data = _red_config('../')
  class_names=[]
  for key, val in data['names'].items():
    class_names.append(key)
    num_classes = len(class_names)
  print('num_class', num_classes)
  print(class_names)

  obj_names(num_classes)
  print('succesffully creating custom_obj_names file in ./data/ folder')
  obj_data(class_names)
  print('succesffully creating custom_obj_names file in ./data/ folder')

  
