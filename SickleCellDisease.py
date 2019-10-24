#Task 25: Consolidation, DNA
#Tarisai Munodawafa Friday 12 April 2019
#A function that will simulate the effects of the Single Nucleotide Polymorphism that leads to this gentic disease, it will read a DNA sequence and then search and replace a codon,
#while printing and showing what a normal and mutated DNA sequence is supposed to look like as a result of variations of that specific codon. The program uses 3 function, one to identify
#mutation, and the other two to translate the DNA sequences in into SLC codon Keys
def mutate(a):
    normal_dna=open("normalDNA.txt", "w")
    normal_dna.write(open('dna.txt', 'r').read().replace(a, 'A'))        
    mutated_dna= open("mutatedDNA.txt", "w") 
    mutated_dna.write(open('dna.txt', 'r').read().replace(a, 'T'))    
    mutated_dna.close()
    normal_dna.close()  
    return print("\'mutatedDNA.txt\' and \'normalDNA.txt\' were created and edited successfully ")
print(mutate('a'))
def txt_translate(TextFile): 
    text=translate(open(TextFile, 'r').read())
    return text
def translate(dNA): 
    length_of_sequence=len(dNA)
    slc_codon_dictionary={"ATT":"I","ATC":"I","ATA":"I","CTT":"L","CTC":"L","CTA":"L","CTG":"L","TTA":"L","TTG":"L","GTT":"V","GTC":"V","GTA":"V","GTG":"V","TTT":"F","TTC":"F","ATG":"M"}
    triplets_list=[]
    for i in range (0,length_of_sequence, 3):
        #taking a slice from each set of 3 characters 
        codon=dNA[i : i+3]
        triplets_list.append(codon)   
    keylist=[]
    #this loop seaches the key that matches each set of three dNA characters
    for a_key in triplets_list:
        #this is to specify that only the first 5 keys are to be searched
        if a_key in slc_codon_dictionary: 
            keylist.append(slc_codon_dictionary[a_key])
        else:
            keylist.append("X")
    #extracting the key values from the list and printing them combined as a plain string of SLC keys
    final_output=''.join(keylist)          
    return final_output
print("The Amino acid sequence found in DNA.txt is; \n"+txt_translate("DNA.txt")+"\n")
print("The Amino acid sequence found in normalDNA.txt is; \n"+txt_translate("normalDNA.txt")+"\n")
print("And the Amino acid sequence found in mutatedDNA.txt is; \n"+txt_translate("mutatedDNA.txt"))
