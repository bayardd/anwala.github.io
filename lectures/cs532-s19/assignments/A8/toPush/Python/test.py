import docclass
from subprocess import check_output
# from docclass import getwords

cl=docclass.naivebayes(docclass.getwords)

docclass.spamTrain(cl)
docclass.testClassifier(cl)
