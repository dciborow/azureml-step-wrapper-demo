
class RecognizeDomainSpecificContentStep(dbStep):  
  def __init__(
    self,
    input,
    output,
    VISION_API_KEY,
    model,   
    region,
    outputCol,
    image_url_col='url',  
    source_directory='.',
    name="Recognize Domain Specific Content", 
    run_name="Recognize Domain Specific Content", 
    allow_reuse=True):
      self.step =  {
        "name":name,
        "notebook_params": {
          "account_name": output.datastore.account_name,
          "input_path": input.path_on_datastore,
          "output_path": output.path_on_datastore,
          "model": model,
          "VISION_API_KEY": VISION_API_KEY,
          "image_url_col": image_url_col,
          "outputCol": outputCol,
          "region": region
        },
        "inputs":[input],
        "python_script_name": "RecognizeDomainSpecificContentStep.py",
        "source_directory":source_directory,
        "run_name": run_name,
        "allow_reuse":allow_reuse    
      }    
      
