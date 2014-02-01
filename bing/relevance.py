import sys
import pprint
from decimal import Decimal
from collections import Counter
from client import BingClient
from __init__ import *

class Relevance(object):
    STOP_WORDS = ["it", "and", "the", "of", "by", "in", "on"]
    SPECIAL_CHARS = ["-", "_", "&", ";", "@", "~", "#", "$", ","]

    @classmethod
    def validate_input(cls, query, target_precision):
        if query == "":
            raise Exception("Query can not be blank.")

        if (float(target_precision) <= 0) or (float(target_precision) > 1):
            raise Exception("Precision must be between 0 and 1")

        return True

    def __init__(self, query, target_precision):
        if Relevance.validate_input(query, target_precision):
            self.query = query
            self.target_precision = target_precision
            self.current_precision = float(0)
            self.relevant_words = []

    def analyze(self, result, is_revelvant):
        if is_revelvant.upper() == "Y":
            self.relevant_words.append(self.exclude_repeat_and_stop_words(result['Title']))

    def exclude_repeat_and_stop_words(self, result_string):
        sanitized_words_list = []
        for elem in result_string.split():
            lower_elem = elem.lower()
            if (lower_elem not in self.STOP_WORDS) and (lower_elem not in self.SPECIAL_CHARS) and (lower_elem not in sanitized_words_list):
                sanitized_words_list.append(lower_elem)

        return " ".join(sanitized_words_list)

    def process(self, account_key = ACCOUNT_KEY):
        for index, result in enumerate (BingClient(account_key).search(self.query)):
            print "\n result %s \n" % index
            pprint.pprint(result)
            is_revelvant = raw_input("Is the result revelant? (Y/N)")
            self.analyze(result, is_revelvant)

        self.current_precision = float(len(self.relevant_words))/float(10)

        if float(self.current_precision) >= float(self.target_precision):
            print "Search is good enough, my job is done! \n"
            print "Query %s \n" % self.query
            print SEARCH_ENDS
            sys.exit(0)
        elif float(self.current_precision) <= 0:
            print "Errr.. Looks like my search is really bad. \n"
            print "I am afraid that there is nothing I can help! \n"
            print SEARCH_ENDS
            sys.exit(0)
        else:
            print "\n Looks like my results are not good enough, let me give it another shot...\n"
            print SEARCH_CONTINUES
            self.reprocess()

    def reprocess(self):
        relevant_words = []
        for words in self.relevant_words:
            relevant_words += words.split()

        # append 2 more words on top of query
        most_relevant_words = [ite for ite, it in Counter(relevant_words).most_common(5)]
        new_query = ' '.join(most_relevant_words)
        new_relevance = Relevance(new_query, self.target_precision)
        new_relevance.process()

def main():
    account_key = sys.argv[1]
    target_precision = sys.argv[2]
    query =  " ".join(sys.argv[3:])

    relevance = Relevance(query, target_precision)
    print SEARCH_STARTS
    if account_key == "DEFAULT_KEY":
        relevance.process()
    else:
        relevance.process(account_key)

if __name__ == "__main__":
    main()
