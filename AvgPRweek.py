from pprint import pprint
from github import Github
import datetime,time,calendar

# token=config.git_token


g=Github('1e303c2fb9056453aecd6ff128957eb5e928eaf6')

cal = calendar.Calendar()

ll=[]
n=7

for day in cal.itermonthdates(2020, 10):
    ll.append(day)

dl=[ll[i:i+n]for i in range(0,len(ll),n)]

#pprint(dl)


def avgtime():
    clo1=[]
    cre1=[]
    crm1=[]
    repo=g.get_repo("testsyren/fullstackpython.com")
    pulls=repo.get_pulls(state='closed',sort='created',base='master')
    for pr in pulls:
        cre=pr.created_at
        cre1.append(cre)
        clo=pr.closed_at
        clo1.append(clo)
        crm=datetime.datetime.date(cre)
        crm1.append(crm)
    
    diff=[]
    for i in dl:
        ss=[]
        for j in i:
            for k in range(len(clo1)):
                if crm1[k] == j:
                    createdsec=time.mktime(cre1[k].timetuple())
                    closedsec=time.mktime(clo1[k].timetuple())
                    output_diff=closedsec-createdsec
                    ss.append(output_diff)

        diff.append(ss)
       
    temp_avg=[]
    for i in diff:
        length=len(i)
        if(length>0):
            sum=0
            for j in  i:
                sum=sum+j
            avg=(sum/length)
            convert=str(datetime.timedelta(seconds=avg))
            temp_avg.append(convert)
            
        else:
            temp_avg.append(0)


    for i in temp_avg:
            print('The avg PR time for week '+str(temp_avg.index(i)+1)+' of the  month is '+str(i))     
        
    # print(diff)
    # print(temp_avg)      

             
avgtime()    
