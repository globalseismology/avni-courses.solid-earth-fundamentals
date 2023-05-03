import os
import sys

toolName = 'solidearth'
notebookName = 'welcome.ipynb'

try:
   toolParametersPath = os.environ['TOOL_PARAMETERS']
except:
   pass
else:
   if os.path.exists(toolParametersPath):
      try:
         with open(toolParametersPath, 'r') as fp:
            toolParameters = fp.readlines()
      except IOError as e:
         sys.stderr.write("%s: %s\n" % (e.strerror,e.filename))
      else:
         for record in toolParameters:
            label,notebookPath = record.split(':')
            if label == 'file(notebook)':
               if notebookPath.startswith(os.path.join(os.sep,'apps',toolName)):
                  notebookPath = notebookPath.strip()
                  if notebookPath.endswith('.ipynb'):
                     notebookName = notebookPath[len(os.path.join(os.sep,'apps',toolName)):].lstrip(os.sep)
                     break

if notebookName:
   print(notebookName)


