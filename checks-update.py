#!/usr/bin/python
import requests
import json
import sys
import pprint
import urllib2, urllib
pp = pprint.PrettyPrinter(indent=4)
#############################3
# SUBS
def post(payload, headers, url):
    data=urllib.urlencode(payload)
    print url + "/" + data
    r = requests.post(url, data=data, headers=headers)
    print r.text
def payload(s_name, f_name, url, string_to_check):
    payload = {
        'url': url,
        'groupname':s_name,
        'pollinterval':5,
        'timeout':40,
        'maxfailurechecks':1,
        'method':'G',
        'monitortype':'URL',
        'displayname':f_name,
        'primarylocation':'New Jersey',
        'secondarylocation':'California, London'
    }
    if string_to_check is None:
        return payload
    else:
        payload['availablestringcheck']=string_to_check
        return payload

def delete_all():
    for device in r.json():
        print device['device_id']
        requests.delete(devices_url + "/" + device['device_id'], headers=headers)
def find_device(devices, group_name, device_name):
    exists=0
    device_id=''
    for all in devices.json():
        for all_k,all_v in all.iteritems():
            if all_k == 'groups':
                for groups in all_v:
                    if groups['groupname'] == group_name:
                        for group_list in groups['group']:
                            if group_list['displayname'] == device_name:
                                #print group_list
                                print ("FOUND IT! {0}  -- {1}".format(group_list['displayname'], device_name))
                                exists=1
    return exists,device_id
##########################################################################
# MAIN
#
headers = {'Content-Type' : 'application/x-www-form-urlencoded'}
base_url='http://www.site24x7.com/api/json'
apikey='apikey=nil_key'
add_endpoint='addMonitor'
edit_endpoint='editMonitor'
add_url =  base_url + "/" + add_endpoint + "?" + apikey
edit_url = base_url + "/" + edit_endpoint
get_url = 'http://www.site24x7.com/api/json/listmonitors?apikey=8a6c4b4f1e9521647e2ad770fb556ffe'
devices = requests.get(get_url)

# Had to truncate the cp conver url, site247 did not like it
checks={
       'creative': {
           'ports':['HTTP', 'HTTPS'],
           'need_to_check': [
                {'name':'html::creative', 'url':'/creative?tagID=sd86ec3566cfb4b57b4ca6658b9e25dc6&type=s&impunique=[RANDOM]', 'str_check':'GIF'},
                {'name':'js::creative', 'url':'/creative?type=i&format=3&tagID=s7a3cecd7a7b44e4f842958b2f860f1eb&impunique=%5BRANDOM%5D&env=inapp&lenv=uuuu0uu1u1&r=671175&userID=2438713bae0a4711aecba8af913f5b80&payload=.Oa44iFBBNlY5Du4UXuKrnZ2CI9XkPrwXjm_3xRUdFUFTc4s.Nzl998tp7ppfAaZ6m1CdC5MQjGejuTDRNziCvTDfWmHqvB0cRnHypZHgfLMC7AeLd7FmrpwoNN5uQ4s5uQ1szHVyVxFAk.rpwoNJ9z4oYYLzZKyJcbfYx92u2p.j.26y8GGEDd5ihORoVyFGh8cmvSuCKzIlnY6xljQlpRDHLrOVC2aPMqgXK_Pmtd0UbUV8afXvIdVuxISg0QrpwoNSUC56MnGWpwoNN5uQ32SCVeTrN.29J54MPy.pk6Hb9LazgzH_y3EjNpmW1lqWNiJiPWrjqNI1kcA0YilmX.UHzB_y4EjNpp0iJ7LDoA237lhQwMAj9htsfHOrf8M2Lz4mvmfTT9oaSz_Abqxjgh5BNv_vMfs.0bI', 'str_check':'MedialetsUserID'},
                {'name':'vast', 'url':'/vast?tagID=302f507ef1794640217975584ab00403','str_check':'In-Stream Video'}
                
            ]
        },
        'tag': {
           'ports':['HTTP', 'HTTPS'],
           'need_to_check': [
                {'name':'js::tag', 'url':'/tag?format=3&tagID=s7a3cecd7a7b44e4f842958b2f860f1eb&impunique=%5BRANDOM%5D', 'str_check':'MEDIALETS_AD_TAG'},
            ]
        },
        'pixel': {
           'ports':['HTTP', 'HTTPS'],
           'need_to_check': [
                {'name':'html::pixel', 'url':'/pixel?0.type=i&0.key=MMAdClickthrough&impID=3b6a923daed3b0f5e66fdcaa5d7b7fe6&r=1637088910', 'str_check':None }
            ]
        },
        'cp': {
           'ports':['HTTP', 'HTTPS'],
           'need_to_check': [
                {'name': 'html::conv', 'url': '/conv?spid=health_check&userID=health_check&0.key=action&0.value=check&1.key=value&1.value=1&2.key=conversionID&2.value=', 'str_check':'health_check'}
            ]
        },
        'clk': {
           'ports':['HTTP', 'HTTPS'],
           'need_to_check': [
                {'name': 'js::href', 'url': '/href?0.type=i&0.key=MMAdClickthrough&tagID=s0739f732376d43868019cc847e93c61b&impunique=[RANDOM]', 'str_check': 'advertisers@medialets.com'},
            ]
        },
        'call': {
           'ports':['HTTP', 'HTTPS'],
           'need_to_check': [
                {'name': 'html::text', 'url': 'oncall.html', 'str_check': 'Anthony'},
            ]
        }
}
vips=[
    {'type':'creative', 'servers':['c.site4.medialytics.com', 'c.medialytics.com', 'c.site3.medialytics.com']},
    {'type':'tag', 'servers':['tag.site4.medialytics.com', 'tag.medialytics.com', 'tag.site3.medialytics.com']},
    {'type':'pixel', 'servers':['p.site4.medialytics.com', 'p.medialytics.com', 'p.site3.medialytics.com']},
    {'type':'clk', 'servers':['clk.site4.medialytics.com', 'clk.medialytics.com', 'clk.site3.medialytics.com']},
    {'type':'cp', 'servers':['cp.site4.medialytics.com', 'cp.medialytics.com', 'cp.site3.medialytics.com']},
    {'type':'call', 'servers':['creative.medialytics.com']},
    
]


#delete_all()
for vip in vips:
    #print ("Checking checks for type: {0}".format(vip['type']))
    for server in vip['servers']:
        #print ("Checking on {0}".format(server))
        for alert in checks:
         if vip['type'] == alert:
            for port in checks[alert]['ports']:
             for conf in checks[alert]['need_to_check']:
                my_lname=server + "::" + port + "::" + conf['name']
                my_sname=server.split(".")
                #def payload(s_name, f_name,  url, string_to_check):
                pload=payload(my_sname[0] + "." + my_sname[1] , my_lname, port.lower() + "://" + server + conf['url'], conf['str_check'])
                exists, device_id=find_device(devices, my_sname[0] + "." + my_sname[1], my_lname)
                if exists == 1:
                    print "Updating this device: " + my_lname + " With this id: " + my_lname
                    post(pload, headers, edit_url + "/" + my_lname + "?" + apikey)
                else:
                    print "Creating this device: " + my_lname
                    post(pload, headers, add_url)
                    
                  

