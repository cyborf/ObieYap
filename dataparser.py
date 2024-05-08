import pandas
import sys

def main():

    #read in the file
    path = sys.argv[1] #file name
    perc = float(sys.argv[2]) #training percentage
    csv = pandas.read_csv(path)

    point = int(perc * len(csv))

	#open and write file
    f = open("{}_training.jsonl".format(path.split(".")[0]), "w")
    #inputting the text into the file
    for i in range (0, point):
        writer = "{{\"input\": \"{}\", \"output\": \"{}\"}}\n".format(csv["product"][i][1:].replace('\"', ''), csv["ad"][i].replace('\"', ''))
        f.write(writer)
    f.close()

    f = open("{}_validation.jsonl".format(path.split(".")[0]), "w")
    #inputting the text into the file
    for i in range (point, len(csv)):
        writer = "{{\"input\": \"{}\", \"output\": \"{}\"}}\n".format(csv["product"][i][1:].replace('\"', ''), csv["ad"][i].replace('\"', ''))
        f.write(writer)
    f.close()
    


main()
