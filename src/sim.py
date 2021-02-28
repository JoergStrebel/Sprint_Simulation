import csv
from datetime import datetime
import random

DURATION = 15 # duration of one sprint  in days
N_US=50
M_WORKER=20
SIG_WORKER=[]

TSHIRTS = {"S": 1, "M": 3, "L": 5, "XL": 9}

class UserStory:
    """
    Class UserStory
    it manages the data for one user story
    """
    def __init__(self, name, effort, prio):
        self.name = name
        self.effort = effort
        self.status = "new"
        self.starttime:int = None
        self.endtime:int = None
        self.assignee:int = None
        self.priority:int = prio


def number_sequence(nint):
    """
    Generator for test data
    my test data has three columns : int, int, date
    """
    num = 0
    while num<nint:
        yield (random.randint(0,1000000), random.randint(0,1000000), datetime.today())
        num += 1

#testdata = {'index': [x for x in range(VOLUME)], 'name': ['Zahl '+str(x) for x in range(VOLUME)]}
#pd.DataFrame(data=testdata).to_csv('/home/jstrebel/devel/pyspark-test/testdata.csv', index=False, header=False, quoting=csv.QUOTE_NONNUMERIC)

#with open('../testdata_buf.csv', 'w', newline='') as csvfile:
#    datawriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
#    datawriter.writerows(numgen)

