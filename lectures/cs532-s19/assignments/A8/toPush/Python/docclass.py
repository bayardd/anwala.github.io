#from pysqlite2 import dbapi2 as sqlite
import sqlite3 as sqlite
import re
import math

tab = '\t'
newline = '\n'


def getwords(doc):
  splitter=re.compile('\\W*')
  # Split the words by non-alpha characters
  words=[s.lower() for s in splitter.split(doc) 
          if len(s)>2 and len(s)<20]
  
  # Return the unique set of words only
  toreturn = dict([(w,1) for w in words])
  return toreturn

class classifier:
  def __init__(self,getfeatures,filename=None):
    # Counts of feature/category combinations
    self.fc={}
    # Counts of documents in each category
    self.cc={}
    self.getfeatures=getfeatures
    
    # Increase the count of a feature/category pair
  def incf(self,f,cat):
    self.fc.setdefault(f,{})
    self.fc[f].setdefault(cat,0)
    self.fc[f][cat]+=1


   # Increase the count of a category
  def incc(self,cat):
    self.cc.setdefault(cat,0)
    self.cc[cat]+=1

  # The number of times a feature has appeared in a category
  def fcount(self,f,cat):
    if f in self.fc and cat in self.fc[f]:
      return float(self.fc[f][cat])
    return 0.0

 # The number of items in a category
  def catcount(self,cat):
    if cat in self.cc:
      return float(self.cc[cat])
    return 0

 # The total number of items
  def totalcount(self):
   return sum(self.cc.values( ))

  # The list of all categories
  def categories(self):
    return self.cc.keys( )


  def train(self,item,cat):
    features=self.getfeatures(item)
    # Increment the count for every feature with this category
    for f in features:
      self.incf(f,cat)

    # Increment the count for this category
    self.incc(cat)

  def fprob(self,f,cat):
    if self.catcount(cat)==0: return 0

    # The total number of times this feature appeared in this 
    # category divided by the total number of items in this category
    return self.fcount(f,cat)/self.catcount(cat)

  def weightedprob(self,f,cat,prf,weight=1.0,ap=0.5):
    # Calculate current probability
    basicprob=prf(f,cat)

    # Count the number of times this feature has appeared in
    # all categories
    totals=sum([self.fcount(f,c) for c in self.categories()])

    # Calculate the weighted average
    bp=((weight*ap)+(totals*basicprob))/(weight+totals)
    return bp




class naivebayes(classifier):
  
  def __init__(self,getfeatures):
    classifier.__init__(self,getfeatures)
    self.thresholds={}
  
  def docprob(self,item,cat):
    features=self.getfeatures(item)   

    # Multiply the probabilities of all the features together
    p=1
    for f in features: p*=self.weightedprob(f,cat,self.fprob)
    return p

  def prob(self,item,cat):
    catprob=self.catcount(cat)/self.totalcount()
    docprob=self.docprob(item,cat)
    return docprob*catprob
  
  def setthreshold(self,cat,t):
    self.thresholds[cat]=t
    
  def getthreshold(self,cat):
    if cat not in self.thresholds: return 1.0
    return self.thresholds[cat]
  
  def classify(self,item,default=None):
    probs={}
    # Find the category with the highest probability
    max=0.0
    for cat in self.categories():
      probs[cat]=self.prob(item,cat)
      if probs[cat]>max: 
        max=probs[cat]
        best=cat

    # Make sure the probability exceeds threshold*next best
    for cat in probs:
      if cat==best: continue
      if probs[cat]*self.getthreshold(best)>probs[best]: return default
    return best

class fisherclassifier(classifier):
  def cprob(self,f,cat):
    # The frequency of this feature in this category    
    clf=self.fprob(f,cat)
    if clf==0: return 0

    # The frequency of this feature in all the categories
    freqsum=sum([self.fprob(f,c) for c in self.categories()])

    # The probability is the frequency in this category divided by
    # the overall frequency
    p=clf/(freqsum)
    
    return p
  def fisherprob(self,item,cat):
    # Multiply all the probabilities together
    p=1
    features=self.getfeatures(item)
    for f in features:
      p*=(self.weightedprob(f,cat,self.cprob))

    # Take the natural log and multiply by -2
    fscore=-2*math.log(p)

    # Use the inverse chi2 function to get a probability
    return self.invchi2(fscore,len(features)*2)
  def invchi2(self,chi, df):
    m = chi / 2.0
    sum = term = math.exp(-m)
    for i in range(1, df//2):
        term *= m / i
        sum += term
    return min(sum, 1.0)
  def __init__(self,getfeatures):
    classifier.__init__(self,getfeatures)
    self.minimums={}

  def setminimum(self,cat,min):
    self.minimums[cat]=min
  
  def getminimum(self,cat):
    if cat not in self.minimums: return 0
    return self.minimums[cat]
  def classify(self,item,default=None):
    # Loop through looking for the best result
    best=default
    max=0.0
    for c in self.categories():
      p=self.fisherprob(item,c)
      # Make sure it exceeds its minimum
      if p>self.getminimum(c) and p>max:
        best=c
        max=p
    return best


# def sampletrain(cl):
  


def spamTrain(cl):

  # document = open("documentation.txt", 'a')

  # spamTitles = ["Enter to win a $100 Amazon gift card", "Buy the more popular, higher rated", "Here are this week's five links", "Master’s Degree Learning Within Reach",
  # "New! Introduction to TensorFlow", "Continue the Johns Hopkins experience", "These are the Skills of T﻿omorrow", "The MSc in Innovation and Entrepreneurship", "Your Learning Experience Just Got Better",
  # "You want better audio right?"]

  # notSpamTitles = ["I write first to invite your participation", "The Norfolk Police Department", "Heart to Heart Career Training Center", "We would like to invite your undergraduate", "Below is the Monarch Crown",
  # "Time tickets were updated March 27", "As part of the Monarch community", "Did you know that the Mane", "I am happy to see that the development", "Here is a tip for registering for a class"]

  # document.write(f"{tab}{tab}{tab}Training files and title subsets listed below.{newline}")
  # document.write(f"----------------------------------------------------------------------------------- {newline}{newline}")
  # document.write(f"{tab}{tab}File Name + Class{tab}{tab}{tab}{tab}{tab}{tab} Headline {newline}")
  # document.write(f"------------------------------------    -------------------------------------------{newline}")
  # count = 0
  for r in range(1,11):
    spamFileName = "spamFile" + str(r)
    notSpamFileName = "notSpam" + str(r)
 
    spamFile = open("./Spam/Train/spam" + str(r) + ".txt", "r")
    notSpamFile = open("./Not_Spam/Train/NotSpam" + str(r) + ".txt", "r")
    text = spamFile.read()
    text2 = notSpamFile.read()

    # document.write(f'File Name: {spamFileName}{tab} Class: Spam {tab}{tab}{spamTitles[count]} {newline}{newline}')
    # document.write(f'File Name: {notSpamFileName}{tab}{tab} Class: NotSpam {tab}{notSpamTitles[count]}{newline}{newline}')


    cl.train(text2, "NotSpam")
    cl.train(text,'spam')

    # count += 1

def testClassifier(cl):

  # document = open("documentation.txt", 'a')

  # notSpamTitles = ["I hope that your semester is going well", "Visionary Integration Professionals (VIP)",  "Monarch diversity and not a study space","Talk to professors and students who currently are doing research",
  # "ODU to offer new Master of Library and Information Studies", "Additional questions to consider can be found on the Registrar’s Office website", "I know the Monarch community joins me in expressing our profound",
  # "I hope your semester is off to a great start", "You have been invited to membership in the Old Dominion University", "Preregistration for Fall 2019 classes is April" ]

  # testSpamTitles = ["Learn from world-class academics", "Get your first month of learning", "Here are this week's five links", "Transform your CV and open the door", "Add a powerful new skill", "Enhance your career", 
  # "Reach your goals with courses", "Black Friday is on", "Worpdress Aliexpress Dropshipping MasterClass", "Create Your Own WordPress Website"]

  # document.write(f"{tab}{tab}{tab}Testing files and title subsets listed below.{newline}")
  # document.write(f"----------------------------------------------------------------------------------- {newline}{newline}")
  # document.write(f"{tab}{tab}File Name + Class{tab}{tab}{tab}{tab}{tab}{tab}{tab} Predicted Class {tab}{tab}{tab}{tab}{tab}{tab}{tab}{tab}{tab} Headline {newline}")
  # document.write(f"--------------------------------------------       ---------------------------    --------------------------------------{newline}")

  # count = 0
  for r in range(11,21):

    spamFileName = "spamFile" + str(r)
    notSpamFileName = "notSpam" + str(r)
  
    spamFile = open("./Spam/Test/spam" + str(r) + ".txt", "r")
    notSpamFile = open("./Not_Spam/Test/NotSpam" + str(r) + ".txt", "r")
    text = spamFile.read()
    text2 = notSpamFile.read()

    predictNotSpam = cl.classify(text2, default='unknown')
    predictSpam = cl.classify(text,default='unknown')
   

    # document.write(f'File Name: {spamFileName}{tab}Expected Class: Spam {tab}{tab} Predicted Class: {predictSpam} {tab}{tab}{tab}{testSpamTitles[count]} {newline}{newline}')
    # document.write(f'File Name: {notSpamFileName}{tab}Expected Class: NotSpam {tab} Predicted Class: {predictNotSpam} {tab}{tab}{notSpamTitles[count]}{newline}{newline}')
    
    # count += 1