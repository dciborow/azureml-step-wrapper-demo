class BingImageSearchStep(dbStep):
  
  def __init__(self, output, BING_IMAGE_SEARCH_KEY, input_query,  source_directory='.', name="Bing Image Search", run_name="Bing Image Search", allow_reuse=True):
    self.step = {
      "name":name,
      "notebook_params": {
        "account_name": output.datastore.account_name,
        "output_path": output.path_on_datastore,
        "input_query": input_query,
        "BING_IMAGE_SEARCH_KEY": BING_IMAGE_SEARCH_KEY
      },
      "inputs":[input],
      "python_script_name": "BingSearchStep.py",
      "source_directory":source_directory,
      "run_name": run_name,
      "allow_reuse":allow_reuse    
    }           
    
