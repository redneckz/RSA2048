import sys
import math
import sympy

target = 2519590847565789349402718324004839857142928212620403202777713783604366202070_7595556264018525880784406918290641249515082189298559149176184502808489120072_8449926873928072877767359714183472702618963750149718246911650776133798590957_0009733045974880842840179742910064245869181719511874612151517265463228221686_9987549182422433637259085141865462043576798423387184774447920739934236584823_8242811981638150106748104516603773060562016196762561338441436038339044149526_3443219011465754445417842402092461651572335077870774981712577246796292638635_6373289912154831438167899885040445364023527381951378636564391212010397122822_120720357

primes_from =  int(sys.argv[1]) if len(sys.argv) > 1 else 2
primes_to = int(sys.argv[2]) if len(sys.argv) > 2 else math.isqrt(target)

prime = sympy.randprime(primes_from, primes_to)

print(prime)
