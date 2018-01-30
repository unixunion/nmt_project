import pickle

if __name__ == "__main__":
    with open('utterances.pickle', 'rb') as f:
        count = 0
        while True:
            try:
                utterance = pickle.load(f)
                if count % 100 == 0:
                    print()
                    print(utterance)
                count += 1
            except EOFError as e:
                print("End of file")
                break
