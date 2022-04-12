import json
import sys
import requests
sys.path.append('./modules')
from createDict import *
from modifyData import *
from downloadFiles import *
from classes import *
import matplotlib.pyplot as plt
import numpy as np

sequence="MDEEPERTKRWEGGYERTWEILKEDESGSLKATIEDILFKAKRKRVFEHHGQVRLGMMRHLYVVVDGSRTMEDQDLKPNRLTCTLKLLEYFVEEYFDQNPISQIGIIVTKSKRAEKLTELSGNPRKHITSLKKAVDMTCHGEPSLYNSLSIAMQTLKHMPGHTSREVLIIFSSLTTCDPSNIYDLIKTLKAAKIRVSVIGLSAEVRVCTVLARETGGTYHVILDESHYKELLTHHVSPPPASSSSECSLIRMGFPQHTIASLSDQDAKPSFSMAHLDGNTEPGLTLGGYFCPQCRAKYCELPVECKICGLTLVSAPHLARSYHHLFPLDAFQEIPLEEYNGERFCYGCQGELKDQHVYVCAVCQNVFCVDCDVFVHDSLHCCPGCIHKIPAPSGV"
lenseq=len(sequence)
uniprotid="Q13888"
#ERBB4: Q15303
#TF2H2: Q13888

PAE_dict=get_PAE_dict(uniprotid, requests, json)
get_PDB(uniprotid, requests)
pLDDT_dict=pLDDT_dict(uniprotid)

def matrix_iterator(dict, class_name):
    i=0
    j=0
    lenseq=len(sequence)
    while i<lenseq:
        vector=[]
        while j<lenseq:
            vector.append(PAE_dict["distance"][j+i*lenseq])
            j+=1
        yield class_name(i+1, vector, pLDDT_dict[i+1])
        j=0
        i+=1

final_scores=[]
positions_list=[]

for element in matrix_iterator(PAE_dict, Element):
        final_scores.append(element.score_xavi(lenseq))
        #final_scores.append(element.score_xavi2(lenseq))
        positions_list.append(element.get_position())

smoothed_list=smoothing(final_scores, 15, lenseq)
print(smoothed_list)
