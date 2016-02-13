# Machine Learning with the Enron Corpus

This repository is for use with the Massey University *158.739 Introduction to Analytics* course. It uses the Enron email corpus to learn data analysis by doing data anaylsis.

## Supported features

## Getting the dataset

Try:

```bash
git clone https://github.com/stiege/enron_corpus_analysis.git
cd enron_corpus_analysis
rake get_enron_data
```
And hope that it works.

## Parsing emails

The repository contains a passing unit test which shows an example of parsing a single email. This implementation will be tested against the test fixture dataset in order to prepare for it to be launched against the entire dataset.

# Discussion

[![Gitter](https://badges.gitter.im/stiege/enron_corpus_analysis.svg)](https://gitter.im/stiege/enron_corpus_analysis?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

# Testing

This repository tests with both python2 and python3. You must have `python2` and `python3` symlinked correctly or these values set as environmental variables on windows.

```bash
rake test
```
