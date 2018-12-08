class RecognizeTextStep(dbStep):  
  def __init__(
    self,
    input,
    output,
    TEXT_API_KEY,
    region,
    image_url_col='url',  
    output_col_rec_text='text',  
    concurrency=10,
    source_directory='.',
    name="Recognize Text", 
    run_name="Recognize Text", 
    allow_reuse=True):
      self.step = {
        "name":name,
        "notebook_params": {
          "account_name": output.datastore.account_name,
          "input_path": input.path_on_datastore,
          "output_path": output.path_on_datastore,
          "TEXT_API_KEY": TEXT_API_KEY,
          "image_url_col": image_url_col,
          "output_col_rec_text": output_col_rec_text,
          "region": region,
          "concurrency": concurrency
        },
        "inputs":[input],
        "python_script_name": "RecognizeTextStep.py",
        "source_directory":source_directory,
        "run_name": run_name,
        "allow_reuse":allow_reuse    
      }
