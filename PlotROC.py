import os
import sys
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
import math
#from scipy import stats
import scipy
import scipy.stats
import IO as io
import myMath as mm


def main(argv):
    tpr =[]
    fpr =[]
    featureVector = io.readFile(argv[1]) #list of pdb files
    #print featureVector
    for i in range(len(featureVector)):
        if featureVector[i].startswith('@') or featureVector[i].startswith('%'):
            continue
        temp = featureVector[i].split(',')
        #print temp
        tpr.append(eval(temp[1]))
        fpr.append(eval(temp[3]))
    x = mm.NormalizedList(fpr)
    y = mm.NormalizedList(tpr)
    #print x, y
    plt.plot(x,y, linewidth=2.5, color='black')
    plt.xlabel('FPR', fontsize = 40, fontweight='bold', )
    plt.ylabel('TPR', fontsize = 40, fontweight='bold')
    plt.xticks((0.0, 0.5, 1.0), fontsize = 34)
    plt.yticks((0.5, 1.0), fontsize = 34)
    plt.savefig('J48_AUC.pdf',bbox_inches='tight', pad_inches=0.1, dpi = 300)
    #plt.show()


if __name__ == '__main__':

    main(sys.argv)

