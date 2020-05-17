import io
from nltk import word_tokenize

if __name__ == '__main__':


    # def extract_data(path):
    #     try:
    #         writetofile = open(os.path.join(path, "wigglefile"), "a")
    #     except:
    #         print("Write to file failed")
    #         return
    #     else:
    #         for filename in os.listdir(path):
    #             try:
    #                 with open(os.path.join(path, filename), 'r') as f:
    #                     writetofile.write(f.read())
    #             except:
    #                 print("File " + filename + " failed to open")
    #                 print("Check " + os.path.join(path, filename) + " for errors")
    #
    #         f.close()
    #         writetofile.close()
    #
    # extract_data("/home/rcoper/Desktop/PythonReadFolder/")

    def analyze():
        pass

    string = "This is a long string of crap that i want to not be so crappy; ThE IntEEENT is to tokenize and analyze"


    word_tokens = []
    for s in string:
        print(word_tokenize(string))
        word_tokens.append(word_tokenize(string))



