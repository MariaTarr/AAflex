from Bio.Blast import NCBIWWW, NCBIXML
from Bio.PDB import PDBList
import urllib.parse
import urllib.request

#Read fasta sequence

def get_fasta(fasta_filename):
	fd = open(fasta_filename, "r")
	ident=""
	wholeseq = ""	
	for line in fd:
		line=line.rstrip()
		if line.startswith(">"):
			ident=line.strip(">")
		else:
			wholeseq = wholeseq + line 
	fd.close()
	return [ident, wholeseq]


#https://python.hotexamples.com/examples/Bio.Blast/NCBIWWW/qblast/python-ncbiwww-qblast-method-examples.html
	
#BLAST
def get_blast_id(seq, db):	
	my_blast=NCBIWWW.qblast(program='blastp', database=db, sequence=seq, hitlist_size=1)  #Only get the best sequence.
	rec=NCBIXML.read(my_blast)
	for alignment in rec.alignments:
		for hsp in alignment.hsps:
			access=alignment.accession
			prot_id=alignment.hit_id
			prot_e_val=hsp.expect
	return [prot_id, access, prot_e_val] #Això hauria de funcionar straightforward
			

#Download PDB
def get_pdb_file(ID): #descarrega el pdb al WD
	pdbl = PDBList()
	pdbl.retrieve_pdb_file(ID, pdir=".", file_format='pdb')
	#return obj
	#faltarà read el pdb
	#!!! el fitxer es guarda amb el nom pdbXXXX.ent


#Map identifier from one to other database
def map_identifier(indb, outdb, queryID):
	url = 'https://www.uniprot.org/uploadlists/'

	params = {
	'from': indb,
	'to': outdb,
	'format': 'tab',
	'query': queryID
	}
	
	data = urllib.parse.urlencode(params)
	data = data.encode('ascii')
	req = urllib.request.Request(url, data)
	with urllib.request.urlopen(req) as f:
   		response = f.read()
   		print (response.decode('ascii'))
  
	

if __name__ == "__main__":

	infasta=get_fasta("P38401.fasta")
	query_seq=infasta[1]
	print (query_seq)
	

	
	#query_id=get_blast_id(query_seq, 'pdb')	
	#print (query_id)

	#get_pdb_file('6QNO')
	
	#map_idendifier('ACC', 'PDB_ID', 'P38401' )


#https://www.uniprot.org/help/api_idmapping

#pdb_file = get_pdb_file('4lza', filetype='cif', compression=False)
#print(pdb_file[:400])
#https://github.com/williamgilpin/pypdb/blob/master/demos/demos.ipynb

