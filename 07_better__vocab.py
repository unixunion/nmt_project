from tensorflow.contrib import learn
import numpy as np
import pickle

from data import encode

en_text = []
sh_text = []

with open("utterances-clean.pickle", "rb") as f:
    while True:
        try:
            u = pickle.load(f) # type: Utterance
            en_text.append(u.modern)
            sh_text.append(u.shakespeare)
        except Exception as e:
            pass
            break

en_max_document_length = max([len(x.split(" ")) for x in en_text])
sh_max_document_length = max([len(x.split(" ")) for x in sh_text])

## Create the vocabularyprocessor object, setting the max lengh of the documents.
en_vocab_processor = learn.preprocessing.VocabularyProcessor(en_max_document_length)
sh_vocab_processor = learn.preprocessing.VocabularyProcessor(sh_max_document_length)

## Transform the documents using the vocabulary.
en_x = np.array(list(en_vocab_processor.fit_transform(en_text)))
sh_x = np.array(list(sh_vocab_processor.fit_transform(sh_text)))

## Extract word:id mapping from the object.
en_vocab_dict = en_vocab_processor.vocabulary_._mapping
sh_vocab_dict = sh_vocab_processor.vocabulary_._mapping

## Sort the vocabulary dictionary on the basis of values(id).
## Both statements perform same task.
#sorted_vocab = sorted(vocab_dict.items(), key=operator.itemgetter(1))
en_sorted_vocab = sorted(en_vocab_dict.items(), key = lambda x : x[1])
sh_sorted_vocab = sorted(sh_vocab_dict.items(), key = lambda x : x[1])

## Treat the id's as index into list and create a list of words in the ascending order of id's
## word with id i goes at index i of the list.
en_vocabulary = list(list(zip(*en_sorted_vocab))[0])
sh_vocabulary = list(list(zip(*sh_sorted_vocab))[0])


print("Vocabulary : ")
print(en_vocabulary)
with open("vocab2.en", 'wt') as o:
    for w in en_vocabulary:
        o.write(encode(w))

print(sh_vocabulary)
print("Transformed documents : ")
print(en_x)
print(sh_x)

