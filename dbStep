class dbStep():
  def attach(self, compute):
    return DatabricksStep(**self.step, **compute)   
  def test(self):        
    with open(self.step['python_script_name'], 'r') as myfile:
      preprocess=myfile.read()
    return preprocess
