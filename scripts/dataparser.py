import pandas as pd
import sys
import random
import csv
import json

def split_data(data_set, seed, train_percentage, training_csv, validation_csv):
    shuffled = data_set.sample(frac=1, random_state=seed)
    breakpt = int(train_percentage*(shuffled.shape[0]))
    training = shuffled.iloc[:breakpt, :]
    validation = shuffled.iloc[breakpt:, :]

    training.to_csv(training_csv, index=False)
    validation.to_csv(validation_csv, index=False)

def create_dataset(csv_file, jsonl_file):
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        data = []
        for row in reader:
            input_text = row[0].strip()
            output_text = row[1].strip()
            data.append({"input": input_text, "output": output_text})

    with open(jsonl_file, 'w', encoding='utf-8') as f:
        for item in data:
            json.dump(item, f, ensure_ascii=False)
            f.write('\n')

def remove_attributes(path, attributes_to_remove, output_file):
    df = pd.read_csv(path)
    df.drop(columns=attributes_to_remove, inplace=True, errors='ignore')
    df.to_csv(output_file, index=False)

def main():

    #read in the file
    path = sys.argv[1] #file name
    perc = float(sys.argv[2]) #training percentage
    seed = int(sys.argv[3])

    # remove attributes
    dataset_name = path[:path.index('.')]
    output_file = dataset_name + '_removed_attributes.csv'
    remove_attributes(path, ['description'], output_file)
    dataset = pd.read_csv(output_file)

    # writes datasets into jsonl
    training_csv = dataset_name + '_removed_attributes_training.csv'
    validation_csv = dataset_name + '_removed_attributes_validation.csv'
    split_data(dataset, seed, perc, training_csv, validation_csv)

    # create final training and validation datasets
    csv_files = [
        {'csv_file': training_csv,
         'output_file': 'advertisement_training.jsonl'
         }, 

         {'csv_file': validation_csv,
          'output_file': 'advertisement_validation.jsonl'}
    ]
    
    for i in csv_files:
        csv_file = i['csv_file']
        output_file = i['output_file'] 
        create_dataset(csv_file, output_file)
main()
