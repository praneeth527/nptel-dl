import requests
import argparse
import os
from bs4 import BeautifulSoup
import youtube_dl
from termcolor import colored
from banner import banner

def downloader(courseTitle, dl, qualityCode="18"):
    if not os.path.exists(courseTitle):
        os.mkdir(courseTitle)
    for mod, lecs in dl.items():
        mod = courseTitle + "/" + mod.strip().replace("/", " - ")
        if not os.path.exists(mod):
            os.mkdir(mod)
        print(colored("\nDownloading "+mod+" ...\n", 'green'))
        for lecname, videoid in lecs.items():
            lecname = lecname.strip()
            print(colored("\nDownloading "+lecname+" ...\n", 'green'))
            videoUrl = "https://www.youtube.com/watch?v="+videoid
            filepath = mod+"/"+lecname+".mp4"
            ydl_opts = {
                'outtmpl': filepath,
                'format': str(qualityCode)
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                try:
                    ydl.download([videoUrl])
                except:
                    print(colored("Some error occured or user interrupted", 'red'))
                    exit()


def createJSON(courseId, outputDict):
    with open(str(courseId)+".json", 'w') as f:
        f.write(str(outputDict).replace("'", "\""))


def getCourseData(courseId):
    outputDict = {}
    url = "https://nptel.ac.in/courses/"+str(courseId)
    resonse = requests.get(url)
    soup = BeautifulSoup(resonse.content, 'lxml')
    courseTitle = soup.select_one('title').text.split(
        'NOC:')[-1].replace('/', '-')
    print(colored("\n"+courseTitle+"\n", 'green'))
    mainHeads = soup.select("#div_lm>ul>li")
    # print(len(mainHeads))
    i = 0
    j = 0
    for mainTitle in mainHeads:
        i += 1
        try:
            head = mainTitle.select("li>a[href='#']")[0].text
            outputDict[str(i)+"-"+head.replace(":", "-")] = {}
            subs = mainTitle.select("li>a[href='']")

            for sub in subs:
                j += 1
                outputDict[str(i)+"-"+head.replace(":", "-")][str(j)+"-"+sub.text.replace(
                    ":", "-").replace("/", "-")] = sub.get('onclick').split(',')[1].replace("'", "").replace(")", "")
        except:
            print(colored("the course with id: "+str(courseId) +
                          " does not have any videos...", 'red'))
    return outputDict, courseTitle


argsParser = argparse.ArgumentParser(description='Nptel Course Downloader')
argsParser.add_argument("--c", default='', required=True,
                        help="Course ID to download the course")
argsParser.add_argument("--q", default='18', help="Video quality code")
args = argsParser.parse_args()

courseID = args.c
videoQuality = args.q


print(banner())


(courseDict, courseTitle) = getCourseData(int(courseID))


# createJSON(int(courseID), courseDict)


downloader(courseTitle, courseDict, int(videoQuality))

# 106106169
