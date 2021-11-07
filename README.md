# Analysis of Public High Schools Admitting Students by Examination in Turkey


This repo contains a flexible, easy to understand and modifiable foundation for scraping, cleaning, analyzing and visualizing **publicly available education data of Turkey.**

Code was written in Python 3.8.5

Along with the foundation, different studies can be done about high schools and universities in Turkey. We conducted a study on the efficiency of public high schools in Turkey, as detailed in the following papers:


**[Analysis of Public High Schools Admitting Students by Examination in Turkey](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3939070)**,
*Beyza Arslan, Anıl Şen.*

***This study has received second prize in the Education Category from The Scientific and Technological Research Council of Turkey.***

If you use this code or data in your research, please cite us using this BibTeX entry:

```
@article{arslan2021analysis,
  title={Analysis of Public High Schools Admitting Students by Examination in Turkey},
  author={Arslan, Beyza and {\c{S}}en, An{\i}l},
  journal={Available at SSRN 3939070},
  year={2021}
}
```

## Contact Us

If you're interested in extending this work, have an idea or any questions:
- email us barslan16@ku.edu.tr or asen16@ku.edu.tr

or submit an issue.

## Installation Instructions

To get started, you'll need to have Python 3.8+ installed.


### Installing from Source

1. Clone this repository to your local machine:

  ```
   git clone https://github.com/asen16/high-schools-analysis.git
   ```

2. Change directory to the directory where requirements.txt is located.


  ```pyfunctiontypecomment
   cd [Path]
   ```

3. Run:

 ```pyfunctiontypecomment
   pip install -r requirements.txt
   ```
   in your shell.


Installation of Web Driver: You'll need to install the Web Driver to scrape data. You can follow the necessary installation steps from Selenium's documentation.

Selenium:
- See [Web Driver Installation](https://www.selenium.dev/selenium/docs/api/py/index.html#installing)


## Getting Started

### Paths
You can follow the instructions in these files to work on the analysis or data scraping part. Google colab version of the codes will be uploaded in next days.

- [`analysis`](https://github.com/asen16/high-schools-analysis/tree/main/analysis) : Shows how master data is filtered, analyzed and data visualized.
- [`data_scraping`](https://github.com/asen16/high-schools-analysis/tree/main/data_scraping): Explains how raw data is scraped from its source.

## Structure of the Code

The code repository is organized into the following components:

- The datasets are located in the `analysis/data` folder.
- The graphs are located in the `analysis/graphs` folder.
- The tabels are located in the `analysis/table` folder.
- The visualization and analysis programs are located in the `analysis` folder.
- The raw data are located in the `data_scraping/DATA` folder.
- The data scraping program is located in the `data_scraping` folder.

## Releases and Contributing

- Please let us know if you encounter any bugs by filing a Github issue.
- We appreciate all your contributions. If you plan to contribute a new Method, Data, or anything else, please see our [contribution guidelines](https://www.github.com/asen16/high-schools-analysis/blob/main/CONTRIBUTING.md).

## Changelog

For the complete release history, see [CHANGELOG.md](https://www.github.com/asen16/high-schools-analysis/blob/main/CHANGELOG.md).

## License
Analysis of Public High Schools Admitting Students by Examination in Turkey is released under the [MIT License](https://www.github.com/asen16/high-schools-analysis/blob/main/LICENSE).
