

import math
import random
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.preprocessing import Normalizer
import numpy as np
from sklearn import tree
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
import time




    #######
print ("DT starts")
#########################################################################################################################
#########################################################################################################################

# This block contains all of the functions and classes

#########################################################################################################################
#########################################################################################################################

# Function to create Corpus 

def Corpus(filelist,root):
    count = len(filelist)
    corpus = [None] * count
    for i in range(count):
        fid = open(root + filelist[i], 'r' ,encoding='utf-8')
        text = fid.read()
        corpus[i] = text.replace('\n','')
        fid.close()
    return corpus

#########################################################################################################################

# Delete stop words

def delStopWords(corpus):

    # List of stop-words from SEO PowerSuite
    
    stopwords_list = ["a","about","above","after","again","against","ain","all","am","an","and","any","are","aren",
                      "aren't","as","at","be","because","been","before","being","below","between","both","but","by",
                      "can","couldn","couldn't","d","did","didn","didn't","do","does","doesn","doesn't","doing","don",
                      "don't","down","during","each","few","for","from","further","had","hadn","hadn't","has","hasn",
                      "hasn't","have","haven","haven't","having","he","her","here","hers","herself","him","himself",
                      "his","how","i","if","in","into","is","isn","isn't","it","it's","its","itself","just","ll",
                      "m","ma","me","mightn","mightn't","more","most","mustn","mustn't","my","myself","needn","needn't",
                      "no","nor","not","now","o","of","off","on","once","only","or","other","our","ours","ourselves",
                      "out","over","own","re","s","same","shan","shan't","she","she's","should","should've","shouldn",
                      "shouldn't","so","some","such","t","than","that","that'll","the","their","theirs","them",
                      "themselves","then","there","these","they","this","those","through","to","too","under","until",
                      "up","ve","very","was","wasn","wasn't","we","were","weren","weren't","what","when","where",
                      "which","while","who","whom","why","will","with","won","won't","wouldn","wouldn't","y","you",
                      "you'd","you'll","you're","you've","your","yours","yourself","yourselves","could","he'd","he'll",
                      "he's","here's","how's","i'd","i'll","i'm","i've","let's","ought","she'd","she'll","that's",
                      "there's","they'd","they'll","they're","they've","we'd","we'll","we're","we've","what's","when's",
                      "where's","who's","why's","would","able","abst","accordance","according","accordingly","across",
                      "act","actually","added","adj","affected","affecting","affects","afterwards","ah","almost","alone",
                      "along","already","also","although","always","among","amongst","announce","another","anybody",
                      "anyhow","anymore","anyone","anything","anyway","anyways","anywhere","apparently","approximately",
                      "arent","arise","around","aside","ask","asking","auth","available","away","awfully","b","back",
                      "became","become","becomes","becoming","beforehand","begin","beginning","beginnings","begins",
                      "behind","believe","beside","besides","beyond","biol","brief","briefly","c","ca","came","cannot",
                      "can't","cause","causes","certain","certainly","co","com","come","comes","contain","containing",
                      "contains","couldnt","date","different","done","downwards","due","e","ed","edu","effect","eg",
                      "eight","eighty","either","else","elsewhere","end","ending","enough","especially","et","etc",
                      "even","ever","every","everybody","everyone","everything","everywhere","ex","except","f","far",
                      "ff","fifth","first","five","fix","followed","following","follows","former","formerly","forth",
                      "found","four","furthermore","g","gave","get","gets","getting","give","given","gives","giving",
                      "go","goes","gone","got","gotten","h","happens","hardly","hed","hence","hereafter","hereby",
                      "herein","heres","hereupon","hes","hi","hid","hither","home","howbeit","however","hundred","id",
                      "ie","im","immediate","immediately","importance","important","inc","indeed","index","information",
                      "instead","invention","inward","itd","it'll","j","k","keep","keeps","kept","kg","km","know",
                      "known","knows","l","largely","last","lately","later","latter","latterly","least","less","lest",
                      "let","lets","like","liked","likely","line","little","'ll","look","looking","looks","ltd","made",
                      "mainly","make","makes","many","may","maybe","mean","means","meantime","meanwhile","merely","mg",
                      "might","million","miss","ml","moreover","mostly","mr","mrs","much","mug","must","n","na","name",
                      "namely","nay","nd","near","nearly","necessarily","necessary","need","needs","neither","never",
                      "nevertheless","new","next","nine","ninety","nobody","non","none","nonetheless","noone","normally",
                      "nos","noted","nothing","nowhere","obtain","obtained","obviously","often","oh","ok","okay","old",
                      "omitted","one","ones","onto","ord","others","otherwise","outside","overall","owing","p","page",
                      "pages","part","particular","particularly","past","per","perhaps","placed","please","plus","poorly",
                      "possible","possibly","potentially","pp","predominantly","present","previously","primarily",
                      "probably","promptly","proud","provides","put","q","que","quickly","quite","qv","r","ran","rather",
                      "rd","readily","really","recent","recently","ref","refs","regarding","regardless","regards",
                      "related","relatively","research","respectively","resulted","resulting","results","right","run",
                      "said","saw","say","saying","says","sec","section","see","seeing","seem","seemed","seeming","seems",
                      "seen","self","selves","sent","seven","several","shall","shed","shes","show","showed","shown",
                      "showns","shows","significant","significantly","similar","similarly","since","six","slightly",
                      "somebody","somehow","someone","somethan","something","sometime","sometimes","somewhat","somewhere",
                      "soon","sorry","specifically","specified","specify","specifying","still","stop","strongly","sub",
                      "substantially","successfully","sufficiently","suggest","sup","sure","take","taken","taking","tell",
                      "tends","th","thank","thanks","thanx","thats","that've","thence","thereafter","thereby","thered",
                      "therefore","therein","there'll","thereof","therere","theres","thereto","thereupon","there've",
                      "theyd","theyre","think","thou","though","thoughh","thousand","throug","throughout","thru","thus",
                      "til","tip","together","took","toward","towards","tried","tries","truly","try","trying","ts","twice",
                      "two","u","un","unfortunately","unless","unlike","unlikely","unto","upon","ups","us","use","used",
                      "useful","usefully","usefulness","uses","using","usually","v","value","various","'ve","via","viz",
                      "vol","vols","vs","w","want","wants","wasnt","way","wed","welcome","went","werent","whatever",
                      "what'll","whats","whence","whenever","whereafter","whereas","whereby","wherein","wheres",
                      "whereupon","wherever","whether","whim","whither","whod","whoever","whole","who'll","whomever",
                      "whos","whose","widely","willing","wish","within","without","wont","words","world","wouldnt","www",
                      "x","yes","yet","youd","youre","z","zero","a's","ain't","allow","allows","apart","appear",
                      "appreciate","appropriate","associated","best","better","c'mon","c's","cant","changes","clearly",
                      "concerning","consequently","consider","considering","corresponding","course","currently",
                      "definitely","described","despite","entirely","exactly","example","going","greetings","hello",
                      "help","hopefully","ignored","inasmuch","indicate","indicated","indicates","inner","insofar","it'd",
                      "keep","keeps","novel","presumably","reasonably","second","secondly","sensible","serious",
                      "seriously","sure","t's","third","thorough","thoroughly","three","well","wonder"]

    # stop-words
    swcount = len(stopwords_list)
    corpus_length = len(corpus)

    for comment in corpus:
        for sword in stopwords_list:
            if sword in comment:
                comment = comment.replace(sword,'')
#     corpus = corpDenoising(corpus)
    return corpus

#########################################################################################################################
    

# Function to write test predictions to .csv file

def csvWriter(prediction, submission_no):
    index = 0
    filename = 'G_24_submission_' + str(submission_no) + '.csv'
    csv = open(filename, "w") 

    columnTitleRow = "Id,Category\n"
    csv.write(columnTitleRow)
    
    for i in prediction:
        csv.write(str(index) + ',' + str(i) + "\n")
        index+=1
    
    csv.close()
    
#########################################################################################################################

# Lemma Tokenizer class for lemmatization

class LemmaTokenizer(object):
    def __init__(self):
        self.wnl = WordNetLemmatizer()
    def __call__(self, doc):
        return [self.wnl.lemmatize(t) for t in word_tokenize(doc)]
    
#########################################################################################################################
        
    
# Data preparation and partitioning

pos_root = 'train/pos/'
neg_root = 'train/neg/'
test_root = 'test/'

All_pos = os.listdir(pos_root)
All_neg = os.listdir(neg_root)
All_test = sorted(os.listdir(test_root),key=lambda x: int(os.path.splitext(x)[0]))

pos_corpus = Corpus(All_pos, pos_root)
neg_corpus = Corpus(All_neg, neg_root)

Np = len(pos_corpus)
Nt = 2 * Np
portion = 0.85
N_train = int(portion * Nt)
N_valid = int((1-portion) * Nt)
train_corpus = [None] * Nt
Y_train = [None] * Nt

for i in range(len(pos_corpus) * 2):
    if i % 2 == 0:
        train_corpus[i] = pos_corpus[int(i/2)]
        Y_train[i] = 1
    else:
        train_corpus[i] = neg_corpus[int(math.floor(i/2))]
        Y_train[i] = 0

test_corpus = Corpus(All_test, test_root)

# Removing stop-words from Training set (comment if you don't want to delete stopwords)

train_corpus = delStopWords(train_corpus)
   
# Before splitting training set and validation set, we perform random shuffle

mixed_train = list(zip(train_corpus, Y_train))

random.shuffle(mixed_train)

train_corpus, Y_train = zip(*mixed_train)

X_training = train_corpus[:N_train]
Y_training = Y_train[:N_train]
X_validation = train_corpus[N_train:]
Y_validation = Y_train[N_train:]



# This block is for counting number of features 

cw = CountVectorizer(ngram_range=(1,2),tokenizer=word_tokenize)

X_1 = cw.fit_transform(X_training)
print(X_1.shape[1])




# Decision Tree pipeline

# 1) using binary features

#DT_clf = Pipeline([('vect', CountVectorizer(ngram_range=(1,2),tokenizer=LemmaTokenizer(), binary=True)),
#                    ('clf', tree.DecisionTreeClassifier())])
#
#print("Decision Tree pipeline created!")
#
#DT_clf.fit(X_training, Y_training)
#
#print("Decision Tree Model fitted!")
#
#Y_pred_DT = DT_clf.predict(X_validation)
#
#DT_Accuracy = np.sum(np.logical_not(np.logical_xor(Y_validation,Y_pred_DT)))/N_valid
#print('Validation Accuracy for Decision Tree with binary features is: '+ str(DT_Accuracy))
#

# 2) using TfIDF 

DT_clf = Pipeline([('tfidf', TfidfVectorizer(ngram_range=(1,2),tokenizer=LemmaTokenizer(),sublinear_tf=True)),
                    ('norm', Normalizer()),
                    ('clf', tree.DecisionTreeClassifier())])

print("Decision Tree pipeline created!")

DT_clf.fit(X_training, Y_training)

print("Decision Tree Model fitted!")

Y_pred_DT = DT_clf.predict(X_validation)

DT_Accuracy = np.sum(np.logical_not(np.logical_xor(Y_validation,Y_pred_DT)))/N_valid
print('Validation Accuracy for Decision Tree with TfIDF is: '+ str(DT_Accuracy))


 
param_grid = {'tfidf__ngram_range': [(1, 1), (1, 2)],
              'clf__min_samples_split': range(10,100,10), 'clf__max_depth': range(1,10,1)}
grid_search_cv = GridSearchCV(DT_clf, param_grid, verbose=1,  cv=3, n_jobs=-1)

gs = grid_search_cv.fit(X_training[:1000], Y_training[:1000])
print("Best parameter (CV score=%0.3f):" % grid_search_cv.best_score_)
print(grid_search_cv.best_params_)

    

start = time.time()
DT_clf = Pipeline([('tfidf', TfidfVectorizer(ngram_range=(1,1),tokenizer=LemmaTokenizer(),sublinear_tf=True)),
                    ('norm', Normalizer()),
                    ('clf', tree.DecisionTreeClassifier(min_samples_split=60, max_depth=7))])

print("Decision Tree pipeline created!")

DT_clf.fit(X_training, Y_training)

print("Decision Tree Model fitted!")

Y_pred_DT = DT_clf.predict(X_validation)
stop = time.time()
DT_Accuracy = np.sum(np.logical_not(np.logical_xor(Y_validation,Y_pred_DT)))/N_valid
print('Validation Accuracy for Decision Tree with TfIDF is: '+ str(DT_Accuracy))
print ('Execution time is '+str(stop - start))
print ("DT Ends")
