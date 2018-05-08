import tabulate

def get_instances_table(instances=[], headers=None):
  if headers:
    labelled_instances = [{key: i[headers[key]] for key in headers.keys()} for i in instances]
  else:
    labelled_instances = instances
  return tabulate.tabulate(labelled_instances, headers="keys")

def get_display_message(instances_categories):
  message = ""
  for ic in instances_categories:
      headers = ic['headers']
      instances = ic['instances']
      category_name = ic['category_name']
  
      message += f'Instances {category_name} ({len(instances)}) :\n'
      message += get_instances_table(instances, headers)
      message += "\n\n"
      
  return message


      
