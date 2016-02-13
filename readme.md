# Machine Learning with the Enron Corpus

This repository is for use with the Massey University *158.739 Introduction to Analytics* course. It uses the Enron email corpus to learn data analysis by doing data anaylsis.

## Supported features

None. At the moment the only thing this repository does is help you to get and extract the corpus:

Try:

```bash
git clone https://github.com/stiege/enron_corpus_analysis.git
cd enron_corpus_analysis
rake get_enron_data
```
And hope that it works.

# Discussion

[![Gitter](https://badges.gitter.im/stiege/enron_corpus_analysis.svg)](https://gitter.im/stiege/enron_corpus_analysis?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

# Testing

This repository tests with both python2 and python3. You must have `python2` and `python3` symlinked correctly or these values set as environmental variables on windows.

```bash
rake test
```
