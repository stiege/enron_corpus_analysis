# Data Analysis with the Enron Corpus

This repository is for use with the Massey University *158.739 Introduction to Analytics* course. It uses the Enron email corpus to learn data analysis by doing data anaylsis.

## Supported features

### Getting the dataset

Try:

```bash
git clone https://github.com/stiege/enron_corpus_analysis.git
cd enron_corpus_analysis
rake get_enron_data
```
And hope that it works.

### Parsing emails

While still in development, the simple parsing function `_parse_email(file_loc)` is shown by unit tests to parse just over 56% of the test fixtures without loss of information.

## Discussion

[![Gitter](https://badges.gitter.im/stiege/enron_corpus_analysis.svg)](https://gitter.im/stiege/enron_corpus_analysis?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

## Testing

[![Build Status](https://secure.travis-ci.org/stiege/enron_corpus_analysis.png)](http://travis-ci.org/stiege/enron_corpus_analysis)


```bash
rake test      # Default python
rake test2     # Python2
rake test3     # Python3
rake test_all  # Python2 and Python3
```
