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

While still in development, the simple parsing function `_parse_email(file_loc)` is shown by unit tests to parse just over 56% of the test fixtures without loss of information, and can correctly identify when it has done a poor job.

## Discussion

[![Gitter](https://badges.gitter.im/stiege/enron_corpus_analysis.svg)](https://gitter.im/stiege/enron_corpus_analysis?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

## Documentation

This project uses sphinx with autodoc extensions for its documentation.

```
rake doc:make[html]
```

You can then find `index.html` at `/doc/build/html/index.html`.

## Testing

[![Build Status](https://secure.travis-ci.org/stiege/enron_corpus_analysis.png?branch=master)](http://travis-ci.org/stiege/enron_corpus_analysis)


```bash
rake test      # Default python
rake test2     # Python2
rake test3     # Python3
rake test_all  # Python2 and Python3
```
