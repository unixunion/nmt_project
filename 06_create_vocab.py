import pickle
import argparse
import nltk

from data import Utterance

modern = ["<unk>", "<s>", "</s>"]
shakespeare = ["<unk>", "<s>", "</s>"]

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Show the contents of a pickle jar')
    parser.add_argument('--file', help='the pickle file to open', required=True)

    args = parser.parse_args()

    with open(args.file, 'rb') as f:
        count = 0
        while True:
            try:
                utterance = pickle.load(f)  # type: Utterance

                for word in nltk.word_tokenize(utterance.shakespeare):
                    if not word in shakespeare:
                        shakespeare.append(word)

                for word in nltk.word_tokenize(utterance.modern):
                    if not word in modern:
                        modern.append(word)

                if count % 1000 == 0:
                    print()
                    print("speaker: {}".format(utterance.speaker))
                    print("shakespeare: {}".format(utterance.shakespeare))
                    print("modern: {}".format(utterance.modern))

                    with open("tst.en", "at") as test_en:
                        test_en.write(utterance.modern + "\n")

                    with open("tst.sh", "at") as test_sh:
                        test_sh.write(utterance.shakespeare + "\n")

                elif count % 1002 == 0:
                    with open("dev.en", "at") as test_en:
                        test_en.write(utterance.modern + "\n")

                    with open("dev.sh", "at") as test_sh:
                        test_sh.write(utterance.shakespeare + "\n")

                else:
                    with open("train.sh", "at") as tt:
                        tt.write(utterance.shakespeare + "\n")

                    with open("train.en", "at") as tf:
                        tf.write(utterance.modern + "\n")

                count += 1
            except EOFError as e:
                print("End of file, samples: {}".format(count))

                with open("vocab.en", 'wt') as m:
                    for w in modern:
                        m.write(w + '\n')
                m.close()

                with open("vocab.sh", 'wt') as s:
                    for w in shakespeare:
                        s.write(w + '\n')
                s.close()

                break
