import pickle
import re

from data import Utterance

# python regex builder https://pythex.org
# creation of the Utterance class


def clean(data : str):
    result = "{}".format(data)
    result = result.replace('\xa0', ' ')
    result = result.replace('\u2003', ' ')
    result = re.sub('\[.*\]', ' ', result)
    result = re.sub('\(.*\)', ' ', result)
    result = re.sub(' +', ' ', result)
    return result.strip()


if __name__ == "__main__":
    with open('utterances-clean.pickle', 'a+b') as o:
        with open('utterances.pickle', 'rb') as f:
            count = 0
            while True:
                try:
                    utterance = Utterance.build(pickle.load(f))

                    cleaned_speaker = utterance.speaker[0]
                    cleaned_shakespeare = clean(utterance.shakespeare)
                    cleaned_modern = clean(utterance.modern)

                    utterance.speaker = cleaned_speaker
                    utterance.shakespeare = cleaned_shakespeare
                    utterance.modern = cleaned_modern

                    pickle.dump(utterance, o)

                    if count % 1000 == 0:
                        print()
                        print(utterance)

                    count += 1
                except EOFError as e:
                    print("End of file, samples: {}".format(count))
                    break
