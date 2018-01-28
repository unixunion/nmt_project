import pickle
import argparse

from data import Utterance

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Show the contents of a pickle jar')
    parser.add_argument('--file', help='the pickle file to open', required=True)

    args = parser.parse_args()

    with open(args.file, 'rb') as f:
        count = 0
        while True:
            try:
                utterance = pickle.load(f)
                if count % 1000 == 0:
                    print()
                    print("speaker: {}".format(utterance.speaker))
                    print("shakespeare: {}".format(utterance.shakespeare))
                    print("modern: {}".format(utterance.modern))
                count += 1
            except EOFError as e:
                print("End of file, samples: {}".format(count))
                break
