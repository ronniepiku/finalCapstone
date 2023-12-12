# finalCapstone
The final capstone project for HyperionDev bootcamp.

# Description
The SpaCy library is used to determine the sentiment on amazon product reviews.

# Table of Contents

1. Getting started
2. Usage
3. Installation
4. Contact Information

# 1. Getting Started
Very easy to get started. Just clone this repo and run the main file. Feel free to make changes to suit your own needs.

# 2. Usage

First of all, data needs to be collected to train the model. In this case, data is downloaded as a .csv file from Kaggle. If you want to adjust the usage of this program, feel free to replace the .csv file with any data you want to determine sentiment on.

The data is then pre-prosessed and the en_core_web_sm model is loaded from the SpaCy library. The pre-processing that occurs includes: dropping NaN values; removing stop words; converting to lower case and stripping whitespace.

Finally, plarity score is caluculated as the data passed through the model and compared to a base score. A value of Positive, Negative or Neautral is returned.

# 3. Installation
The following libraries are required to run this code:

- SpaCy
- SpacyTextBlob
- pandas

# 4. Contact Information
Please direct any questions to any of the following:

- e-mail: ronniepiku1@hotmail.co.uk

- LinkedIn: https://www.linkedin.com/in/ronald-piku/
