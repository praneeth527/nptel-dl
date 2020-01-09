[![GitHub release](https://img.shields.io/badge/release-v1.0-brightgreen.svg?style=flat-square)](https://github.com/praneeth14/nptel-dl/releases/tag/v1.0)
[![GitHub stars](https://img.shields.io/github/stars/praneeth14/nptel-dl.svg?style=flat-square)](https://github.com/praneeth14/nptel-dl/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/praneeth14/nptel-dl.svg?style=flat-square)](https://github.com/praneeth14/nptel-dl/network)
[![GitHub issues](https://img.shields.io/github/issues/praneeth14/nptel-dl.svg?style=flat-square)](https://github.com/praneeth14/nptel-dl/issues)
[![GitHub license](https://img.shields.io/github/license/praneeth14/nptel-dl.svg?style=flat-square)](https://github.com/praneeth14/nptel-dl/blob/master/LICENSE)

# nptel-dl
**A cross-platform python based utility to download course videos from NPTEL.**

By ***Praneeth Kumar Reddy Ballarapu*** (praneeth14)

[![intro.png](https://i.postimg.cc/ZY9TG0Ps/intro.png)](https://postimg.cc/F145crB0)


### Before creating an issue, please do the following:

1. **Use the GitHub issue search** &mdash; check if the issue is already reported.
2. **Check if the issue is already fixed** &mdash; try to reproduce it using the latest `master` in the repository.
3. Please make **pull requests** to contribute to the repository 


## ***Features***
- Downloads entire course videos in a well organised directory strcuture
- Resume capability for a course video.
<!-- - Save course youtube video ids to a json file (option: `--save`). -->



## ***Requirements***

- Python 3.x
- Python `pip`
- Python module `requests`
- Python module `bs4`
- Python module `lxml`
- Python module `youtube_dl`
- Python module `colorama`
- Python module `argparse`
- Python module `termcolor`

## ***Module Installation***

	pip install -r requirements.txt
	
 
## ***Download nptel-dl***

You can download the latest version of nptel-dl by cloning the GitHub repository.

	git clone https://github.com/praneeth14/nptel-dl.git


## ***Usage***

***Download a course***

    python nptel-dl.py --c=COURSE_ID
  
***Download course videos with specific resolution***

    python nptel-dl.py --c=COURSE_ID --q=VIDEO_QUALITY_CODE
  

## **Steps to download course videos**

1. Make sure that you already installed python 3.x on your machine otherwise download from here <a href="https://www.python.org/downloads/">Python 3.x</a>
2. Now clone or download this repository.
3. Open command prompt and goto the repository downloaded path
4. Run `pip install -r requirements.txt` to install required modules
5. Copy the course id you want to download from NPTEL website. For example https://nptel.ac.in/courses/106105217/ here course id is **106105217**
6. Now run `python nptel-dl.py --c=106105217 --q=18`
7. Default quality code is `18`

## Format codes

| Format Code | Extension | Resolution | Note                    |
|-------------|-----------|------------|-------------------------|
| 140 (worst) | m4a       | audio only | DASH audio , audio@128k |
| 160         | mp4       | 144p       | DASH video, video only  |
| 133         | mp4       | 240p       | DASH video, video only  |
| 134         | mp4       | 360p       | DASH video, video only  |
| 135         | mp4       | 480p       | DASH video, video only  |
| 136         | mp4       | 720p       | DASH video, video only  |
| 17          | 3gp       | 176x144    |                         |
| 36          | 3gp       | 320x240    |                         |
| 5           | flv       | 400x240    |                         |
| 43          | webm      | 640x360    |                         |
| 18          | mp4       | 640x360    |                         |
| 22          | mp4       | 1280x720   | (best quality)          |

**Note:** The above codes may differ based on videos



## **Advanced Usage**

<pre><code>
Author: Praneeth Kumar Reddy Ballarapu (<a href="">praneeth14</a>)

usage: nptel-dl.py [-h] --c C [--q Q]

Nptel Course Downloader

optional arguments:
  -h, --help  show this help message and exit
  --c C       Course ID to download the course
  --q Q       Video quality code (default code '18')

A cross-platform python based utility to download course videos from nptel.

positional arguments:
  --c           NPTEL Course ID.
  --q           Video Quality Code

General:
  -h, --help        Shows the help.
  -v, --version     Shows the version.


Others:
  --save            Saves all youtube video ids to a JSON file
  
Example:
  python nptel-dl.py --c=106106169 --q=18
  python nptel-dl.py --c=106106169

</code></pre>