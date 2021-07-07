import os
import shutil

shutil.rmtree('./outputDocs')

if not os.path.exists("./outputDocs"):
     os.makedirs("./outputDocs")
