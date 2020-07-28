import twint
import csv
import time
import asyncio


f = open('test.csv')
c = twint.Config()
c.Lang = "en"
c.Translate = True
c.TranslateDest = "en"

csv_f = csv.reader(f)

c.Username = "defaultkoda"

async def runTwink(item):
    c.Search = item
    twint.run.Search(c)

    return print("- Search Completed. ")


async def main():
    for row in csv_f:
        for i in range(0, len(row)):
            word = row[i]
            i = i + 1
            
            await runTwink(word) 
        
            pass

asyncio.run(main())
# def runTwink(item):

#     c.Search = item

#     twint.run.Search(c)

#     return print("- Search Completed. ")



        
#         pass
# runTwink("testing")


# asyncio.run(runTwink("@apple"))