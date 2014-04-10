# open coordinate file
f1=open('ch1_ca_cb.cor','rb') # Open coordinate file 
array =[row.strip().split('\t') for row in f1] # put coordinates in a list

#del array[0:4] #removing 4 first rows of the list (Comment elements of coordinate file)
atom=[]; matrix=[]; count = 0;i=0

while (count<len(array)):
    atom.append(array[count][0].split())
    matrix.append(atom[count][:])
    count = count +1

count=4

while (count<len(matrix)):
   matrix[count][2]='P%d' %int(matrix[count][1])
   count=count+1

#print matrix


#print >> reportfile,'\n\nRead atoms of type',type, ':',i, 'Out of', len(array), '\n'
reportfile=open('./report.txt','w+')
f2=open('./ch1_2bead.cor2','w+')
template="{0:10} {1:10} {2:10} {3:10} {4:11} {5:10} {6:5} {7:10}"

for row in matrix:
 print row.format("{0:10} {1:10} {2:10} {3:10} {4:11} {5:10} {6:5} {7:10}") 
# print >>f2, template.format(' '.join(row) + '\n') # Print a copy of extracted matrix into the report file
#print "Coordinations of", type, "atoms opened successfully!"
#return matrix

