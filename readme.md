# Data Analysis with the Enron Corpus

This repository is for use with the Massey University *158.739 Introduction to Analytics* course. It uses the Enron email corpus to learn data analysis by doing data anaylsis.

## Supported features

### Getting the dataset

```bash
git clone https://github.com/stiege/enron_corpus_analysis.git
cd enron_corpus_analysis
rake get_enron_data
```

### Parsing emails

While still in development, the simple parsing function `_parse_email(file_loc)` is able to parse the entire dataset. While most fields are parsed as strings (for example lists of email addresses); the date of emails being sent is correctly typed in the created database in UTC time.

This can be used to create a database (SQLite/MySQL and others supported):

```bash
rake db:create
# Equivalent to db:create["core/_test_fixtures", "sqlite:///database.db"]
```

`rake db:create[maildir]` (after getting the enron dataset) will take wildly different times depending on your version of python and type of hard drive you're using. Expect this to take up to an hour.

## Discussion

[![Gitter](https://badges.gitter.im/stiege/enron_corpus_analysis.svg)](https://gitter.im/stiege/enron_corpus_analysis?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

## Documentation

This project uses sphinx with autodoc extensions for its documentation.

```bash
rake doc  # equivalent to rake doc:make[help]
rake doc:make[html]
```

You can then find `index.html` at `/doc/build/html/index.html`.

## Testing

[![Build Status](https://secure.travis-ci.org/stiege/enron_corpus_analysis.png?branch=master)](http://travis-ci.org/stiege/enron_corpus_analysis)


```bash
rake test      # Default python, equivalent to rake test:py
rake test:py2  # Python2
rake test:py3  # Python3
rake test:all  # Python2 and Python3
```

## Rakefile

As may be seen, the rakefile is the correct interface to get the majority of tasks done. Available rakefile commands can be viewed at anytime with `rake -T`.
