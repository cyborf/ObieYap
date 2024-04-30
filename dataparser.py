import pandas
import sys

def main():

    #read in the file
    path = sys.argv[1] #file name
    csv = pandas.read_csv(path)
	#open and write file
    f = open("finetuner.jsonl", "w")
    #inputting the text into the file
    for i in range (len(csv)):
        writer = "{{\"input\": \"{}\", \"output\": \"{}\"}}\n".format(csv["product"][i][1:], csv["ad"][i])
        f.write(writer)
        
    

main()
