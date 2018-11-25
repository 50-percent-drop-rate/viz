## Converts each tweet to a format that is pastable to the timeline format
import csv

def initial():
    file = 'scored_scaled.csv'
    process(file)

def process(file):
    with open(file, encoding="utf8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        michaelDict = dict()
        khashoggiDict = dict()
        canadaDict = dict()
        for row in csv_reader:
            story = row['story']
            time = row['timestamp']
            time = time.split(' ')
            time = time[0]
            id = row['url']
            score = row['score']
            retweets = row['retweets']
            likes = row['likes']
            replies = row['replies']

            if story == 'Michael':
                if time not in michaelDict:
                    michaelDict[time] = [(id, score, retweets, likes, replies)]
                else:
                    aList = michaelDict[time]
                    aList.append((id, score, retweets, likes, replies))
            elif story == 'Khashoggi':
                if time not in khashoggiDict:
                    khashoggiDict[time] = [(id, score, retweets, likes, replies)]
                else:
                    aList = khashoggiDict[time]
                    aList.append((id, score, retweets, likes, replies))
            else:
                if time not in canadaDict:
                    canadaDict[time] = [(id, score, retweets, likes, replies)]
                else:
                    aList = canadaDict[time]
                    aList.append((id, score, retweets, likes, replies))

        for time in michaelDict.keys():
            values = michaelDict[time]
            sortedValues = sorted(values, key=lambda tup: tup[1], reverse=True)
            if len(sortedValues) > 3:
                sortedValues = sortedValues[0:2]
            michaelDict[time] = sortedValues

        for time in khashoggiDict.keys():
            values = khashoggiDict[time]
            sortedValues = sorted(values, key=lambda tup: tup[1], reverse=True)
            if len(sortedValues) > 3:
                sortedValues = sortedValues[0:2]
            khashoggiDict[time] = sortedValues

        for time in canadaDict.keys():
            values = canadaDict[time]
            sortedValues = sorted(values, key=lambda tup: tup[1], reverse=True)
            if len(sortedValues) > 3:
                sortedValues = sortedValues[0:2]
            canadaDict[time] = sortedValues
        processDict(michaelDict, 'michaelf.csv')
        processDict(khashoggiDict, 'khashoggif.csv')
        processDict(canadaDict, 'canadaf.csv')

def processDict(dict, name):
    for key in dict.keys():
        values = dict[key]
        for value in values:
            time = key
            time = time.split('/')
            month = time[0]
            day = time[1]
            year = time[2]
            score = value[1]
            retweets = value[2]
            likes = value[3]
            replies = value[4]


            text = 'Score: %s. Likes: %s. Replies %s. Retweets %s.' % (score, likes, replies, retweets)
            media = 'twitter.com' + value[0]
            with open(name, 'a', encoding="utf8", newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                data = [year, month,day, '', year,month,day, '', '', '', text, media]
                csv_writer.writerow(data)


if __name__ == '__main__':
    initial()
