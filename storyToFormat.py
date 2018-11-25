## Converts each story .csv to a format that is pastable to the timeline format

import csv
#'story1.csv', 'story2.csv', 'story3.csv'
filenames = ['story1', 'story2', 'story3']


def initial():

    for file in filenames:
        process(file)

def process(file):
    stories = dict()
    allStories = []
    name1 = file  +'.csv'
    name2 = file + 'f.csv'
    with open(name1, encoding="utf8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            allStories.append(row)
            time = row["publishedAt"]
            score = row["score"]
            time = time.split('T')
            time = time[0]
            if time not in stories:
                stories[time] = [score]
            else:
                curList = stories[time]
                curList.append(score)
                stories[time] = curList
    for key in stories.keys():
        aList = stories[key]
        if len(aList) > 3:
            aList = aList[0:2]
        stories[key] = aList
    for key in stories.keys():
        values = stories[key]
        for value in values:
            time = key.split("-")
            year = time[0]
            month = time[1]
            day = time[2]
            aStory = allStories[int(value)]
            headline = aStory['title']
            media = aStory['urlToImage']
            mediaCaption = aStory['url']
            rank = int(value) + 1
            text = "Story Rank: " + str(rank) + ". " + aStory['description']
            with open(name2, 'a', encoding="utf8", newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                data = [year, month,day, '', year,month,day, '', '', headline, text, media, '', mediaCaption]
                csv_writer.writerow(data)


if __name__ == '__main__':
    initial()
