# -*- coding: UTF-8 -*-
import requests
import json
import pandas as pd
import time


category = []
categoryCode = []
code = []
comSummary = []
fundedYearEnd = []
fundedYearStart = []
funding = []
keywordCh = []
keywordEn = []
leader = []
leaderCode = []
leaderTitle = []
name = []
organization = []
organizationCode = []
outComeAwardNum = []
outComeConferenceNum = []
outComeJournalNum = []
outComePatent = []
outComeWorkNum = []
searchYearEnd = []
summaryCh = []
summaryEn = []
tranceNo = []
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
j = []
k = []
l = []
m = []
n = []
o = []
p = []
q = []
r = []
s = []
t = []
u = []
v = []
w = []
x = []
z = []
zz = []
ISOTIMEFORMAT = '%Y-%m-%d %X'
timenow = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
print("init successful  "+timenow)


def getResponse(resp=None,i=1):
    url = 'http://npd.nsfc.gov.cn/projectSearch!searchAjaxForBut.action'
    headers = {
        'host': 'npd.nsfc.gov.cn',
        'method': 'POST',
        'cookie': '_gscu_1512923953=00785253fwctg711; JSESSIONID=752E885283EAB4F383948C9BB71A334C',
        'origin': 'http://npd.nsfc.gov.cn',
        'referer': 'http://npd.nsfc.gov.cn/projectSearch!search.action?project.applyCode=H',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    }
    data = {
        'project.code': '',
        'sort': '0',
        'pageSize': '21',
        'project.searchYearEnd': '',
        'currentPage': i,
        'project.name': '',
        'project.leader': '',
        'project.organization': '',
        'project.organizationCode': '',
        'project.applyCode': 'H',
        'project.category': '',
        'project.fundedYearStart': '',
        'project.fundedYearEnd': '',
        'checkCode': '请输入验证码',
    }
    resp = requests.post(url, headers=headers, data=data)
    return resp


timenow = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
print("def successful  "+timenow)


for page in range(1, 1508):
    html = json.loads(getResponse(i=page).content)
    for y in range(0, 21):
        applyCode = a.append(html["projectList"][y]["applyCode"])
        category = b.append(html["projectList"][y]["category"])
        categoryCode = c.append(html["projectList"][y]["categoryCode"])
        code = d.append(html["projectList"][y]["code"])
        comSummary = e.append(html["projectList"][y]["comSummary"])
        fundedYearEnd = f.append(html["projectList"][y]["fundedYearEnd"])
        fundedYearStart = g.append(html["projectList"][y]["fundedYearStart"])
        funding = h.append(html["projectList"][y]["funding"])
        keywordCh = j.append(html["projectList"][y]["keywordCh"])
        keywordEn = k.append(html["projectList"][y]["keywordEn"])
        leader = l.append(html["projectList"][y]["leader"])
        leaderCode = m.append(html["projectList"][y]["leaderCode"])
        leaderTitle = n.append(html["projectList"][y]["leaderTitle"])
        name = o.append(html["projectList"][y]["name"])
        organization = p.append(html["projectList"][y]["organization"])
        organizationCode = q.append(html["projectList"][y]["organizationCode"])
        outComeAwardNum = r.append(html["projectList"][y]["outComeAwardNum"])
        outComeConferenceNum = s.append(html["projectList"][y]["outComeConferenceNum"])
        outComeJournalNum = t.append(html["projectList"][y]["outComeJournalNum"])
        outComePatent = u.append(html["projectList"][y]["outComePatent"])
        outComeWorkNum = v.append(html["projectList"][y]["outComeWorkNum"])
        searchYearEnd = w.append(html["projectList"][y]["searchYearEnd"])
        summaryCh = x.append(html["projectList"][y]["summaryCh"])
        summaryEn = z.append(html["projectList"][y]["summaryEn"])
        tranceNo = zz.append(html["projectList"][y]["tranceNo"])

html = json.loads(getResponse(i=1508).content)
for y in range(0, 7):
    applyCode = a.append(html["projectList"][y]["applyCode"])
    category = b.append(html["projectList"][y]["category"])
    categoryCode = c.append(html["projectList"][y]["categoryCode"])
    code = d.append(html["projectList"][y]["code"])
    comSummary = e.append(html["projectList"][y]["comSummary"])
    fundedYearEnd = f.append(html["projectList"][y]["fundedYearEnd"])
    fundedYearStart = g.append(html["projectList"][y]["fundedYearStart"])
    funding = h.append(html["projectList"][y]["funding"])
    keywordCh = j.append(html["projectList"][y]["keywordCh"])
    keywordEn = k.append(html["projectList"][y]["keywordEn"])
    leader = l.append(html["projectList"][y]["leader"])
    leaderCode = m.append(html["projectList"][y]["leaderCode"])
    leaderTitle = n.append(html["projectList"][y]["leaderTitle"])
    name = o.append(html["projectList"][y]["name"])
    organization = p.append(html["projectList"][y]["organization"])
    organizationCode = q.append(html["projectList"][y]["organizationCode"])
    outComeAwardNum = r.append(html["projectList"][y]["outComeAwardNum"])
    outComeConferenceNum = s.append(html["projectList"][y]["outComeConferenceNum"])
    outComeJournalNum = t.append(html["projectList"][y]["outComeJournalNum"])
    outComePatent = u.append(html["projectList"][y]["outComePatent"])
    outComeWorkNum = v.append(html["projectList"][y]["outComeWorkNum"])
    searchYearEnd = w.append(html["projectList"][y]["searchYearEnd"])
    summaryCh = x.append(html["projectList"][y]["summaryCh"])
    summaryEn = z.append(html["projectList"][y]["summaryEn"])
    tranceNo = zz.append(html["projectList"][y]["tranceNo"])
result = {'applyCode': a,
          'category': b,
          'categoryCode': c,
          'code': d,
          'comSummary': e,
          'fundedYearEnd': f,
          'fundedYearStart': g,
          'funding': h,
          'keywordCh': j,
          'keywordEn': k,
          'leader': l,
          'leaderCode': m,
          'leaderTitle': n,
          'name': o,
          'organization': p,
          'organizationCode': q,
          'outComeAwardNum': r,
          'outComeConferenceNum': s,
          'outComeJournalNum': t,
          'outComePatent': u,
          'outComeWorkNum': v,
          'searchYearEnd': w,
          'summaryCh': x,
          'summaryEn': z,
          'tranceNo': zz}
timenow = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
print("data successful  "+timenow)

df = pd.DataFrame.from_dict(result)
timenow = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
print("format successful  "+timenow)
df.to_csv('./NSFCmed.csv', index=False)
timenow = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
print("export successful  "+timenow)

#for i in range(97, 123):
#    print(chr(i)+" = []")
