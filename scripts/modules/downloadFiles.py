def get_PAE_dict(uniprotid, requests, json):
    # Downloading the PAE matrix. The url is always the same but changing the Uniprotid
    url='https://alphafold.ebi.ac.uk/files/AF-'+uniprotid+'-F1-predicted_aligned_error_v2.json'
    r = requests.get(url, allow_redirects=True)

    # Saving the url contents into a file
    open(uniprotid+'.json', 'wb').write(r.content)

    # Transforming the json file into a python dicctionary
    mat=open(uniprotid+'.json')
    data=json.load(mat)

    return data[0]

def get_PDB(uniprotid, requests):
    url='https://alphafold.ebi.ac.uk/files/AF-'+uniprotid+'-F1-model_v2.pdb'
    r = requests.get(url, allow_redirects=True)
    open(uniprotid+'.pdb', 'wb').write(r.content)
