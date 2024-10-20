# RJ Tardoni
# UWYO COSC 1010
# Submission Date (10/20/24)
# Lab 06
# Lab Section: 14
# Sources, people worked with, help given to: 
# The python crash course textbook on while loops and dictionaries
# comments
# here


random_string = """
jppamiqxegokaizvkyawwurhewtcxohryzptznyuedhhmawpic
pkzwuiorngdfcsgqnlyifzyaivehpiyszykqprbcsobygzhadd
yfddbulxmcnyvqhesmnybyuhxjqqmhdxwhcselasiayqhctnlw
hakethjahqnvjdowhlyzosemxkbenestxgvgncmffkcxldcmkl
itclmqdhrbdgzwtvdxwedcknbyaecvttjphtxubvhwvcvjqayy
almxuxjbcmznnzekptfzbldsjwpvringlmalwufvlppeiendur
dyophftqjkghhncwxoksqaqnpueudpygiytqgpcgjqsjbtbpzi
vaeczmyicnednjjoxkpnjmpfbgyjnbfjlweqqppodfxfzzwkuf
rldgryyhceuikimoavosuzuozthmatcgxcmkxnaxmsevkcumby
spiajlbycvrluxdkfavxidzalxuixqkxiybhfuqhcvmrhzbzse
idjwgwdwgfkyreozkyoxdvhixfejxjfgkkgobescboyfshiovu
fxdyvfsnmjzsphgmtldlaoehofcspzujghcdcxzggvunpbtglr
topplmkviuewwpoaplmbpgejmymxbyzzwbnujrlysszmxkjerb
zpiewqvgopvhmmcgwcyvxvwhdvfgsrybcozhdtwujhdbxzznkc
ergcqbetpgwrejuluqfxchlihunzbcdwboysjqenjxzbgqbycx
dybxpyztjyxpkqfvxullzkedpkjjobhymfinpvprxejktyrpai
ehjgwahpquzcmvclatdfcmattavoehnhnzveoxwnmnptxbvxto
gpcobgzdhsjevhcohkltftmrqkosknkxeylhqxkkctbnusijgr
uvecpbqmylqdaohkfaqbgeokyyipumjuaaayikdzyxfrpaieyo
uxiosjwioebsjtslblfurgcodtyaggzovzfnnyjngawiwbbtqi
kqqhnkwheolpqzasmsmbxqkeiqvogquobphewznfsnlkkizhca
cbiyvxpmjxywqvzqtshfvnfbusphggexfqzepsrduvtovdsknl
ztyuwugprkhbmktfvrenbmqgdjwnkeugtojrpqfmjhtrlcqcpq
pwsguedzgvktpwbqkhkueymjtxbvzmdfjopzkygujrjdtogssg
cxczryuqhhgjlpultkoffescpzyjrfqqabnhkfdnhkylpjamxk
uxidjkqdrkxqjqjtflebvwhcvqjciykzhrvppvxhvpedgznwty
kujglixooczrhxziasjxddfcghzlwrqcyiilpruhdfvitewxzg
dzcvmvnoskchscgoqfsojfvahlwkrslzeirlblseplcmpmbmum
ibrdamvqfstydtjopdkdcbnnmpifxckozyxzluhcqbqtpismog
ulufaajxvuizvdzioxfvypxovptkibcrjvfidomejknuggfrtp
kptwffersvqjknemkejsgspckwqisdcliuezhbeqpwgrjcqajl
huobykkbujmyuuinbwdklqfhvakyozzsxghfyownjjwqtkxgkf
ipdbjzxfogozstfsektujsvklrvecditiectuvtfibohmxxzna
cpqzeoburtquuizhypugnkvuwbdxnraareqkofhfjobrpcsuxq
nbafxlkuafbfsiuyrxdusqyasqyrwhdjrukgxdackumvairlgn
fjhenwbrdghbevgqbybpwncclolgqyuhallbqtzdywbvlzwtil
jctmsxjortnxvlbhuhkblppewjhqjzxrwgftlturxjuwfoaqpp
sgfnxwxolkbrpdmpniitoljzaxabgtnelrmryetxqypwrjdyjc
zipwbdpbazxpesmrcfuikeamtlsrgxrhzfytecenyydeemrhxj
gmdruhillntvpadzbroyygydpmonwuakruvxbdrqhtrjvoqsin
gjbarzvuqplmsmbwtqfghteoknbxmaokwlqqfoblmzsxczjzfj
mzmawtarjdtgongqqufhhdjwcinhlxcsgoltjycxrkloqozxoi
crlfmgflzzxgiiliqlksxyaydsohhahzxtsufzppftvgbpsdlx
ertfmbothijzrrdvfrnsohnwulcxvcvxngvmznhazxrgdsugij
fracotpirvqemsiuualpkpvtmtgchmowkmvoolrjfblrtwkmtr
xhawucytgwlahddkhxxfublukkdldpovqokntydhzzrxiisdwu
ujrkoewqoflyebogbwgdhriwkkoiofwtjlhxxtmzkklzbcmxhv
lrslowamkcwolbcgfkfciegdwqskuazxnycqkkggzsowcmafay
ibmkdwkqmdkjesqnjiqpijixbwjhenmsrrlpcseliiajlvcaac
zkdenxczyooloczcaahnkehbwimvieedpdlqfafbqvxvfmvabd
"""
random_string = random_string.replace("\n","") #remove all newline characters
print(len(random_string)) # Print out the size for reference 

# Above is a string with 2500 characters.
# Create a program that goes through and counts the occurrence of each character, excluding \n using a  dictionary
# Output each letter and its corresponding occurrence in alphabetical order
# Output which letter occurred the most 
# Output which letter occurred the least 
# Output what the percentage of the string each character is, again in alphabetical

#Tips and trick:
# You can iterate through strings like you would a list
# All characters are lowercase 
# Each letter will be PAIRED with its corresponding value 
# That is to say, this is a great use of dictionaries
    # You will  need to add the letter to the dictionary on first occurrence 
    # Then increment its corresponding count 


#Load all the elements into a dictionary
#Will need to first declare a dictionary 

# Output: each letter and its corresponding occurrence in alphabetical order


letter_occurance={}

for index in random_string:
    if index in letter_occurance:
        letter_occurance[index] += 1
    else:
        letter_occurance[index] = 1


print(sorted(letter_occurance.items()))


# Output which letter occurred the most 


max_occurance= max(letter_occurance['a'],letter_occurance['b'], letter_occurance['c'], letter_occurance['d'], 
                    letter_occurance['e'], letter_occurance['f'], letter_occurance['g'], letter_occurance['h'], 
letter_occurance['i'], letter_occurance['j'],  letter_occurance['k'], letter_occurance['l'], letter_occurance['m'], 
letter_occurance['n'], letter_occurance['o'], letter_occurance['p'], letter_occurance['q'], letter_occurance['r'], 
letter_occurance['s'], letter_occurance['t'], letter_occurance['u'], letter_occurance['v'], letter_occurance['w'], 
letter_occurance['x'], letter_occurance['y'], letter_occurance['z'])


min_occurance= min(letter_occurance['a'],letter_occurance['b'], letter_occurance['c'], letter_occurance['d'], 
                    letter_occurance['e'], letter_occurance['f'], letter_occurance['g'], letter_occurance['h'], 
letter_occurance['i'], letter_occurance['j'],  letter_occurance['k'], letter_occurance['l'], letter_occurance['m'], 
letter_occurance['n'], letter_occurance['o'], letter_occurance['p'], letter_occurance['q'], letter_occurance['r'], 
letter_occurance['s'], letter_occurance['t'], letter_occurance['u'], letter_occurance['v'], letter_occurance['w'], 
letter_occurance['x'], letter_occurance['y'], letter_occurance['z'])
 
print(max_occurance)
print(min_occurance)


most_occurred = "k"
least_occurred = "n"

print(f"The letter that occurred the most is {most_occurred}")


# Output which letter occurred the least 
print(f"The letter that occurred the least is {least_occurred}")


# Output what the percentage of the string each character is, again in alphabetical

Total= (letter_occurance['a']+letter_occurance['b'] + letter_occurance['c'] + letter_occurance['d'] +
                    letter_occurance['e'] + letter_occurance['f'] + letter_occurance['g'] + letter_occurance['h']+ 
letter_occurance['i'] + letter_occurance['j'] +  letter_occurance['k'] + letter_occurance['l'] + letter_occurance['m'] + 
letter_occurance['n'] + letter_occurance['o'] + letter_occurance['p'] + letter_occurance['q'] + letter_occurance['r'] + 
letter_occurance['s'] + letter_occurance['t'] + letter_occurance['u'] + letter_occurance['v'] + letter_occurance['w'] + 
letter_occurance['x'] + letter_occurance['y'] + letter_occurance['z'])

print(Total)

for index in sorted(letter_occurance):
    print(f"The percentage of letter {index} is {letter_occurance[index]/Total*100}")
