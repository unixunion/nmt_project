import pickle
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Show the contents of a pickle jar')
    parser.add_argument('--file', help='the pickle file to open', required=True)

    args = parser.parse_args()

    with open(args.file, 'rb') as f:
        count = 0
        while True:
            try:
                utterance = pickle.load(f)
                if count % 123 == 0:
                    print()
                    print("speaker: {}".format(utterance.speaker))
                    print("shakespeare: {}".format(utterance.shakespeare))
                    print("modern: {}".format(utterance.modern))
                    print("url: {}".format(utterance.url))
                count += 1
            except EOFError as e:
                print("End of file, samples: {}".format(count))
                break
