from sqlwrapper import gensql,dbget
import json

def MergeProfile(request):
    p_merge = request.json['profile_to_merge']
    o_merge = request.json['original_profile']
    print(p_merge,o_merge,type(p_merge))
    merge_p = {}
    for k,v in p_merge.items():
        for a,b in o_merge.items():
            if k == a:
              if v != '':  
                #b = v   
                merge_p[""+a+""] = v
                #print(merge_p)
              else:
                merge_p[""+a+""] = b
    #if merge_p['pf_type'] == 'individual':
    #    print(merge_p['pf_type'])
    #    a = { k : v for k,v in merge_p.items() if k != 'pf_type'}
    #    e = { k : v for k,v in merge_p.items() if k == 'pf_type'}
        
    print(merge_p)           
    return (json.dumps({"merge_profile":merge_p},indent=2))
