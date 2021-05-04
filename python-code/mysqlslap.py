import numpy as np
import sys, getopt
import matplotlib.pyplot as plt
import csv

def main(argv):
    inputfile = ''
    outputfile = ''
    qfile = ''

    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv,"h:i:o:q:",["ifile=","ofile=","qfile="])

    except getopt.GetoptError:
        print ('parselog.py -i <inputfile> -o <outputfile> -q <thirdfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print ('parselog.py -i <inputfile> -o <outputfile> -q <thirdfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-q", "--qfile"):
            qfile = arg
            #print ('Input file is ',inputfile)
            #print ('Output file is ',outputfile)
            

    csv1 = np.genfromtxt (inputfile, delimiter=",", names=True, case_sensitive=True)
    csv2 = np.genfromtxt (outputfile, delimiter=",", names=True, case_sensitive=True)
    csv3 = np.genfromtxt (qfile, delimiter=",", names=True, case_sensitive=True)
    #print(repr(csv))

    fig, ax = plt.subplots()

    hdd = ax.errorbar(csv1['clients'], csv1['average'], yerr=[csv1['minimum'], csv1['maximum']], fmt='o')
    hdd.set_label('HDD')

    ssd = ax.errorbar(csv2['clients'], csv2['average'], yerr=[csv2['minimum'], csv2['maximum']], fmt='o')
    ssd.set_label('SSD')

    ceph = ax.errorbar(csv3['clients'], csv3['average'], yerr=[csv3['minimum'], csv3['maximum']], fmt='o')
    ceph.set_label('ceph')

    ax.set_ylim((0,500))
    ax.set_title('Performance of three tested storage technologies')
    ax.legend()

    ax.set_ylabel('t[s]')
    ax.set_xlabel('concurrent users')

    #labels=['HDD', 'SSD', 'ceph']

    plt.grid(linestyle='dotted')
    plt.savefig("mysqlslap.png")
    plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])