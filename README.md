# ObieYap!
a promotion text generator to help Oberlin student-run organizations with social media presence.

## Abstract
The motivation behind our project ObieYap is the observation that most student organizations at Oberlin do not have active social media presence, and that prevents them from having the best outreach to Oberlin students. It is understandable that this is the case, as a typical Oberlin student organizer is also busy with their classes as well as extracurricular activities. We want to provide them a solution that can help them with making social media presence tasks easier.

## Technology
HuggingFace's Transformer model - Mistral 7-B

## Datasets
All .csv datasets have been parsed using our dataparser (dataparser.py). They are:
1. GPT: Entirely Chat-GPT generated dataset (100+ rows)
2. HF: HuggingFace open source dataset "advertisement_copy.csv" (1000+ rows)
3. IG: Scraped from Oberlin student club Instagram (3000+ rows)
All datasets have been splitted into two portions: one for training and the other for validation. They were downloaded and used to finetune locally, and would not be used to train commercial LLMs.

## Hyperparameters
- max_new_tokens = 200
- repetition_penalty = 1.15
- batch_size = 2
- device_map = "cuda"

## Brief Descriptions of Outcome
1. GPT and base model: best used for generic posts
2. HF: best used for casual Instagram-worthy captions
3. IG: best used for Oberlin-specific posts

## Honor Code Declaration:
We have adhered to the Honor Code in this assignment.
Dan-Ha Le, An Nguyen, Yen Mai

## Thanks to:
Professor Adam Eck and CSCI 373: Applied Machine Learning - Spring 2024
