import pandas
import sys

def main():

    #read in the file
    path = sys.argv[1] #file name
    csv = pandas.read_csv(path)

    f = open("finetuner.jsonl", "w")
    writer = ""

    print(len(csv))
    for i in range (len(csv)):
        writer += "{{\"input\": \"{}\", \"output\": \"{}\"}}\n".format(csv["product"][i][1:], csv["ad"][i])
        f.write(writer)
        
    

main()
