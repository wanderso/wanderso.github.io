from os import listdir
from os.path import isfile, join, getmtime
import time, datetime

onlyfiles = [f for f in listdir("./queue") if isfile(join("./queue", f))]

for file_data in onlyfiles:
    file_name = "./queue/" + file_data
    file_time = getmtime(file_name) 
    print "%s last modified: %s" % (file_data, time.ctime(file_time))
    title_text = file_data
    
    with open(file_name) as f:
        content = f.readlines()

    file_datetime = datetime.datetime.fromtimestamp(file_time)

    post_name = file_datetime.strftime("%Y-%m-%d-") + file_data + ".md"

    post_name = post_name.replace(" ","-")
    
    with open("./_posts/" + post_name,"w") as f:
        f.write("---\n")
        f.write("layout: post\n")
        f.write("title: \"%s\"\n" % file_data)
        f.write("date: %s\n" % file_datetime.strftime("%Y-%m-%d %H:%M:%S"))
        f.write("---\n")
        for entry in content:
            f.write(entry)

#---
#layout: post
#title: "Multi-post test"
#date: 2016-06-09 14:40:45
#---
