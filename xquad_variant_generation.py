import json
import argparse
import copy

# Create variants of form Question-Snippet in multilingual form from xquad datasets.

supported_languages = ['ar', 'de', 'el', 'en', 'es', 'hi', 'ru', 'th', 'tr', 'vi', 'zh']
input_file_format = './xquad.{}.json'
output_file_format = 'crosslingual_variants/xquad.q_{}_s_{}.json'


def create_multilingual_variant(q_type, s_type):
    with open(input_file_format.format(q_type), 'r', encoding='utf-8') as fp:
        q_dataset = json.load(fp)
    with open(input_file_format.format(s_type), 'r', encoding='utf-8') as fp:
        s_dataset = json.load(fp)
    for q_data, s_data in zip(q_dataset['data'], s_dataset['data']):
        for q_par, s_par in zip(q_data['paragraphs'], s_data['paragraphs']):
            for q_qa, s_qa in zip(q_par['qas'], s_par['qas']):
                s_qa['question'] = q_qa['question']
    with open(output_file_format.format(q_type, s_type), 'w', encoding='utf-8') as fp:
        json.dump(s_dataset, fp)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate multilingual variants of XQuaD datasets.')
    parser.add_argument('-q', choices=supported_languages, default='en',
                        help='Language of the question- should be from any of the languages for which '
                             'xquad datasets are present')
    parser.add_argument('-s', choices=supported_languages, default='en',
                        help='Language of the snippet- should be from any of the languages for '
                             'which xquad datasets are present')
    args = parser.parse_args()
    create_multilingual_variant(args.q, args.s)
