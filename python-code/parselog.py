import sys, getopt
import statistics
import csv

def main(argv):
    inputfile = ''
    outputfile = ''

    ## some variables to parse file
    bench = 'Benchmark'

    headline = ['clients', 'minimum', 'average', 'maximum', 'queriesPerClient', 'stddev']
    results=[]
    output=[]
    output.append(headline)
    avg_tmp=[]
    count = 0

    offset = 3

    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])

    except getopt.GetoptError:
        print ('parselog.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print ('parselog.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
            print ('Input file is ',inputfile)
            print ('Output file is ',outputfile)

    datafile = open(inputfile, 'r')

    while True:
        line = datafile.readline()
        if not line:
            break

        if bench in line:
            # Average
            #line = datafile.readline()
            average = float(pythonIsRidiculous(datafile.readline(), 2))
            minimum = float(pythonIsRidiculous(datafile.readline(), 2))
            maximum = float(pythonIsRidiculous(datafile.readline(), 2))
            clients = int(pythonIsRidiculous(datafile.readline(), 0))
            queries = int(pythonIsRidiculous(datafile.readline(), 0))

            result = [clients, minimum, average, maximum, queries, 0]
            results.append(result)

    datafile.close()

    ##calculate values
    for dataset in results:
        index = dataset[0]-offset

        try:
            if not output[index][0]:
                print('\n')
        except:                
            output.append(dataset)
            avg_tmp.append([dataset[2],0,0,0,0])            

        if output[index][1] > dataset[1]:
            output[index][1]=dataset[1]
        
        if output[index][3] < dataset[3]:
            output[index][3]=dataset[3]

        print(dataset)
        avg_tmp[index-1][count] = dataset[2]            
        
        if dataset[0] == 20:
            count += 1
            
    count = 1

    while (count <= len(output)):
        if count >= len(output):
            break

        output[count][2] = statistics.mean(avg_tmp[count-1])
        output[count][5] = statistics.stdev(avg_tmp[count-1])

        count += 1

    csvFile = open(outputfile, 'w', newline ='')
    with csvFile:
        write = csv.writer(csvFile)
        write.writerows(output)

    print("Finished")


def pythonIsRidiculous(line, fromRight):
    tmp = line.split(' ')
    try:
        return tmp[len(tmp)-fromRight]
    except:
        return tmp[-1].strip()

if __name__ == "__main__":
    main(sys.argv[1:])