# E-commerce! <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="30px">




## Product and sales data analysis  

## Table of Contents

1. [Introduction](#Introduction)
2. [Data Extracting](#Data-Extracting)
3. [Data Cleaning](#Data-Cleaning)
4. [Data Storing](#Data-Storing)
5. [End Note](#End-Note)

<p align="center">
  <img width="500" height="300" src="https://de.melchers-china.com/wp-content/uploads/2020/07/1-1.jpg">
</p>

## Introduction: 

This project has two core part. One is to extract data from an E-commerce website (we used Amazon USA) and then store the extracted data into a database. From which data can be extracted very efficiently and insights can be formed. 

We worked on two segment Extracting data using python and storing and analysing the extractrd data using Mysql. 

Definition of the both segment can be seen with drop down below-

<details>
<summary>Web Scraping</summary>
<br>
Web scraping is data scraping used for extracting data from websites. The web scraping software may directly access the World Wide Web using the Hypertext Transfer Protocol or a web browser. 

</details>


<details>
<summary>Database Management</summary>
<br>
Database Management, allows  to organize, store and retrieve data from a computer. Database Management can also describe, the data storage, operations and security practices of a Database Administrator (DBA), throughout the life cycle of the data. Managing a database involves designing, implementing and supporting stored data, to maximize its value.
</details>

<span style="color:red"> **THIS REPOSITORY IS  UNDER WORK, Please have a look at the finished work** </span>


<p align="left">
<a href="https://www.animatedimages.org/cat-wine-706.htm"><img src="https://www.animatedimages.org/data/media/706/animated-wine-image-0005.gif" border="0" alt="animated-wine-image-0005" /></a><br></pre>
</details>

## Used tools:

![](https://img.shields.io/badge/Extracting-Scraping-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)

![](https://img.shields.io/badge/Cleaning-Python-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)

![](https://img.shields.io/badge/DBMS-MySQL-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)

![](https://img.shields.io/badge/Visualization-Plotly-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)


## Legal Issues:
As the data extracted here was for solely academic purpose and no business intention was not behiind it this scraping is until this point completely legal. 

## Data Extracting:

We used python libraries for extracting the data. The libraries used for scraping are below - 

---
**Libraries**

import fake_useragent

from selectorlib import Extractor

import requests

from fake_useragent import UserAgent

import json
from time import sleep

---

The process is quite simple. First ran the python script <span style="color:yellow">create_search_url.py</span> where we mentioned the website that will be scraped including how many pages we want to scrape. Which will automatically create the <span style="color:yellow">search_urls.text</span> file. In the next step we created the  <span style="color:yellow">product.py</span> python script which contains the exact direction of what information should be collected from the search url. All the data came as .json format and than used for further analysis. 





## Data Cleaning:

Processing the scraped data took the longest time almost 70% of all the project time. The main reason behind is that scraped data comes with lots of noise in it. We worked with 8 different products including 




## Data Storing:

Structural Query Language or SQL is used in this project for storing the cleaned data. 







## End Note:

Please follow the social media links of the author_

<!-- Please don't remove this: Grab your social icons from https://github.com/carlsednaoui/gitsocial -->

<!-- display the social media buttons in your README -->


[![alt text][1.1]][1]
[![alt text][2.1]][2]


<!-- links to social media icons -->
<!-- no need to change these -->

<!-- icons with padding -->


[1.1]: http://i.imgur.com/yCsTjba.png (google plus icon with padding)
[2.1]: http://i.imgur.com/0o48UoR.png (github icon with padding)

<!-- icons without padding -->


[1.2]: http://i.imgur.com/VlgBKQ9.png (google plus icon without padding)
[2.2]: http://i.imgur.com/9I6NRUm.png (github icon without padding)


<!-- links to your social media accounts -->
<!-- update these accordingly -->


[1]: https://myaccount.google.com/profile
[2]: https://github.com/Sheikh-Nabil

<!-- Please don't remove this: Grab your social icons from https://github.com/carlsednaoui/gitsocial -->

<a href="#top">Back to top</a>
