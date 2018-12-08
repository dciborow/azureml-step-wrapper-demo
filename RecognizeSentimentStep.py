
class RecognizeSentimentStep(dbStep):  
  def __init__(
    self,
    input,
    output,    
    TEXT_API_KEY,
    region,
    text_col='text',  
    outputCol='sentiment',  
    source_directory='.',
    name="Recognize Sentiment", 
    run_name="Recognize Sentiment", 
    allow_reuse=True):
    self.step = {
      "name":name,
      "notebook_params": {
        "account_name": output.datastore.account_name,
        "input_path": input.path_on_datastore,
        "output_path": output.path_on_datastore,
        "TEXT_API_KEY": TEXT_API_KEY,
        "text_col": text_col,
        "output_col_sentiment": outputCol,
        "region": region
      },
      "inputs":[input],
      "python_script_name": "TextSentimentStep.py",
      "source_directory":source_directory,
      "run_name": run_name,
      "allow_reuse":allow_reuse    
    }      
