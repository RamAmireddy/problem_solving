

import heapq
import time

class Pair():

    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __lt__(self, other):
        return (Solution.arr[self.p] / Solution.arr[self.q]) < (Solution.arr[other.p] / Solution.arr[other.q])



class Solution:
    arr = None

    def kthSmallestPrimeFraction(self, A, K):
        Solution.arr = A
        fractions = []
        st = time.time()
        for i in range(0, len(A) - 1):
            fractions.append(Pair(i, len(A) - 1))

        heapq.heapify(fractions)
        # print(fractions)
        ans = None
        while K:
            K = K - 1
            x = heapq.heappop(fractions)
            ans = [A[x.p], A[x.q]]
            if x.q - 1 > x.p:
                heapq.heappush(fractions, Pair(x.p, x.q - 1))
        et = time.time()
        print(et-st)
        return ans

ls =[1,2,3,7,13,17,19,29,53,59,67,71,73,79,97,101,107,127,131,137,139,149,157,167,173,181,193,223,227,229,233,239,251,257,263,269,271,293,307,311,313,317,331,337,347,349,353,359,367,373,383,401,421,431,433,457,461,491,499,521,523,541,557,563,577,593,599,601,613,643,647,659,673,677,683,701,709,719,733,743,757,761,773,787,797,809,811,823,827,829,839,853,857,859,877,881,883,887,907,919,929,941,947,953,967,977,983,997,1009,1019,1021,1031,1039,1049,1051,1061,1069,1087,1091,1097,1103,1117,1123,1151,1171,1187,1193,1201,1213,1231,1237,1249,1259,1289,1291,1301,1307,1327,1361,1373,1381,1409,1423,1429,1433,1439,1451,1453,1471,1483,1487,1489,1493,1511,1523,1531,1543,1549,1553,1571,1579,1583,1601,1609,1613,1621,1657,1663,1667,1669,1693,1709,1721,1733,1741,1747,1753,1759,1777,1783,1787,1789,1823,1831,1861,1871,1879,1889,1913,1933,1949,1973,1997,2017,2027,2029,2039,2053,2063,2069,2081,2099,2111,2113,2131,2141,2153,2161,2179,2207,2213,2221,2237,2239,2243,2267,2269,2281,2297,2311,2333,2351,2371,2381,2383,2393,2417,2423,2437,2441,2459,2467,2473,2477,2503,2521,2531,2549,2551,2557,2579,2609,2617,2633,2647,2659,2663,2671,2683,2689,2693,2707,2711,2719,2729,2731,2767,2777,2789,2791,2803,2819,2833,2837,2843,2879,2887,2903,2909,2917,2927,2953,2957,2963,2971,2999,3019,3023,3037,3041,3079,3083,3109,3121,3137,3163,3167,3169,3187,3203,3253,3257,3307,3313,3319,3323,3331,3343,3361,3373,3389,3413,3433,3449,3457,3463,3467,3469,3491,3517,3527,3539,3547,3557,3571,3581,3613,3617,3623,3631,3637,3643,3671,3673,3677,3691,3697,3701,3709,3727,3767,3779,3793,3797,3803,3823,3833,3847,3851,3853,3877,3881,3889,3907,3923,3929,3931,3943,3989,4003,4007,4019,4049,4051,4073,4079,4091,4093,4099,4127,4133,4139,4177,4201,4211,4217,4219,4231,4243,4259,4261,4271,4273,4289,4337,4339,4363,4391,4409,4423,4441,4447,4463,4483,4493,4513,4517,4519,4547,4583,4603,4621,4639,4703,4721,4733,4751,4787,4789,4813,4817,4889,4909,4933,4937,4943,4951,4967,4969,4973,4987,5009,5011,5021,5023,5059,5077,5081,5087,5099,5101,5107,5153,5167,5179,5189,5209,5231,5237,5261,5273,5279,5281,5303,5309,5323,5333,5347,5381,5387,5399,5417,5419,5431,5443,5471,5477,5479,5483,5501,5503,5507,5519,5521,5527,5531,5557,5563,5569,5573,5581,5639,5641,5651,5657,5683,5689,5701,5783,5791,5851,5861,5869,5879,5897,5923,5927,5953,5981,5987,6029,6037,6047,6053,6067,6073,6089,6091,6101,6113,6121,6143,6163,6203,6211,6263,6277,6287,6299,6311,6317,6323,6343,6359,6361,6373,6397,6421,6427,6449,6451,6473,6481,6491,6521,6529,6547,6553,6563,6571,6577,6581,6607,6619,6653,6659,6661,6673,6689,6691,6701,6703,6709,6719,6733,6761,6763,6779,6791,6827,6829,6833,6863,6869,6871,6899,6907,6911,6917,6947,6959,6961,6967,6971,6977,6997,7001,7013,7039,7043,7057,7069,7079,7103,7109,7121,7129,7151,7159,7187,7207,7213,7229,7237,7243,7253,7297,7307,7321,7331,7349,7351,7369,7393,7411,7417,7433,7459,7477,7499,7507,7517,7523,7529,7541,7547,7559,7561,7577,7589,7591,7603,7607,7639,7643,7649,7673,7681,7691,7699,7723,7727,7741,7753,7757,7759,7789,7793,7817,7829,7841,7867,7873,7877,7879,7883,7901,7919,7927,7963,7993,8009,8011,8017,8053,8069,8081,8093,8101,8111,8123,8161,8167,8171,8179,8191,8209,8237,8243,8263,8269,8293,8311,8317,8329,8363,8369,8377,8387,8389,8419,8423,8429,8431,8443,8461,8467,8501,8527,8539,8563,8597,8599,8609,8623,8629,8641,8647,8663,8669,8677,8689,8693,8699,8707,8713,8719,8737,8741,8747,8819,8821,8831,8839,8849,8861,8863,8867,8929,8933,8941,8951,8963,8969,8971,9007,9011,9029,9049,9059,9067,9091,9109,9127,9133,9137,9151,9157,9173,9181,9187,9199,9203,9209,9221,9227,9239,9241,9257,9277,9281,9283,9319,9323,9341,9349,9377,9413,9419,9421,9433,9437,9439,9461,9463,9467,9473,9479,9491,9497,9521,9533,9539,9547,9587,9601,9629,9631,9643,9649,9661,9677,9679,9719,9721,9733,9739,9743,9749,9767,9769,9787,9803,9811,9829,9833,9839,9857,9871,9887,9929,9931,9973,10007,10009,10037,10061,10067,10069,10079,10091,10093,10103,10111,10133,10139,10141,10151,10159,10163,10169,10177,10181,10193,10211,10223,10253,10259,10273,10303,10321,10331,10333,10337,10343,10357,10399,10457,10459,10463,10477,10487,10501,10513,10529,10567,10597,10601,10607,10613,10627,10631,10639,10651,10667,10687,10691,10709,10711,10723,10729,10733,10739,10753,10771,10789,10889,10891,10937,10949,10957,10973,10979,10993,11003,11027,11059,11069,11083,11087,11113,11119,11149,11161,11197,11239,11243,11257,11299,11311,11351,11383,11393,11399,11411,11437,11443,11447,11467,11471,11483,11489,11491,11503,11519,11549,11551,11587,11593,11633,11657,11677,11681,11689,11719,11731,11743,11777,11779,11783,11789,11801,11807,11813,11821,11833,11863,11867,11887,11903,11909,11927,11941,11953,11971,11981,12007,12011,12037,12041,12043,12049,12071,12073,12097,12101,12109,12113,12149,12197,12211,12227,12239,12253,12281,12289,12329,12373,12377,12379,12391,12409,12421,12451,12457,12473,12487,12497,12511,12539,12547,12553,12569,12583,12601,12619,12641,12647,12653,12671,12697,12721,12739,12763,12809,12823,12889,12899,12911,12923,12941,12973,12983,13001,13003,13007,13037,13043,13049,13063,13093,13103,13109,13147,13159,13163,13171,13177,13183,13187,13217,13219,13229,13241,13249,13267,13291,13297,13309,13313,13331,13337,13339,13381,13397,13411,13417,13421,13441,13451,13457,13469,13477,13487,13513,13537,13553,13591,13597,13613,13633,13649,13681,13687,13693,13709,13751,13759,13781,13789,13799,13807,13841,13859,13873,13877,13879,13883,13901,13933,13997,14011,14029,14033,14051,14071,14081,14083,14087,14107,14153,14159,14177,14197,14221,14249,14251,14281,14321,14323,14341,14347,14387,14401,14423,14431,14437,14449,14461,14503,14533,14543,14549,14551,14561,14563,14621,14629,14633,14639,14657,14669,14713,14731,14737,14753,14767,14771,14779,14797,14813,14827,14867,14869,14879,14887,14891,14929,14939,14947,14969,14983,15013,15031,15053,15061,15073,15083,15091,15121,15131,15139,15187,15193,15241,15263,15271,15277,15287,15289,15313,15319,15329,15349,15359,15361,15373,15377,15383,15401,15413,15427,15439,15443,15451,15461,15467,15497,15511,15527,15541,15551,15559,15569,15581,15583,15601,15619,15629,15641,15647,15649,15667,15679,15683,15733,15739,15749,15761,15767,15787,15797,15817,15859,15881,15889,15901,15907,15913,15919,15923,15937,15971,15973,15991,16001,16007,16033,16057,16061,16073,16103,16111,16127,16141,16189,16217,16223,16229,16231,16249,16301,16333,16339,16349,16361,16363,16369,16381,16417,16421,16427,16433,16447,16451,16481,16529,16547,16553,16561,16607,16619,16631,16657,16673,16693,16699,16741,16759,16763,16787,16823,16831,16843,16879,16889,16901,16927,16931,16937,16943,16963,16981,16987,17011,17021,17033,17099,17117,17159,17183,17189,17191,17207,17209,17231,17239,17257,17293,17299,17321,17327,17333,17341,17351,17359,17387,17389,17393,17417,17419,17449,17467,17477,17483,17489,17497,17509,17551,17579,17581,17597,17599,17609,17623,17627,17657,17659,17669,17681,17713,17761,17791,17807,17827,17837,17839,17863,17891,17903,17909,17911,17923,17959,17971,17981,17987,18013,18041,18047,18049,18059,18061,18077,18097,18119,18127,18131,18149,18169,18181,18211,18217,18229,18251,18257,18287,18307,18311,18313,18341,18353,18367,18397,18401,18413,18427,18439,18481,18521,18523,18539,18541,18553,18583,18587,18593,18713,18731,18743,18749,18757,18773,18793,18803,18839,18899,18911,18913,18973,18979,19001,19009,19031,19051,19069,19073,19079,19081,19121,19141,19157,19163,19181,19183,19211,19213,19259,19273,19289,19301,19309,19333,19373,19381,19391,19403,19421,19423,19427,19429,19433,19447,19463,19483,19489,19501,19507,19531,19541,19543,19559,19597,19603,19609,19661,19699,19739,19751,19759,19793,19801,19841,19853,19861,19867,19889,19891,19927,19937,19949,19973,19979,20011,20021,20029,20047,20051,20063,20071,20089,20101,20123,20129,20143,20147,20149,20161,20173,20183,20231,20233,20249,20287,20297,20333,20347,20353,20357,20369,20389,20393,20399,20411,20431,20441,20443,20477,20507,20533,20551,20563,20593,20611,20627,20681,20707,20731,20743,20747,20749,20759,20771,20773,20807,20809,20849,20857,20879,20887,20897,20899,20903,20921,20929,20959,20981,21011,21013,21017,21059,21061,21089,21101,21121,21139,21143,21179,21187,21193,21221,21227,21269,21277,21283,21313,21317,21319,21347,21377,21379,21407,21419,21467,21481,21487,21491,21503,21517,21529,21557,21559,21563,21569,21577,21587,21589,21599,21611,21613,21647,21649,21673,21683,21701,21713,21727,21737,21751,21757,21767,21787,21799,21803,21851,21859,21863,21871,21911,21929,21943,21977,21997,22003,22027,22031,22037,22063,22067,22073,22079,22091,22123,22129,22157,22171,22189,22193,22247,22259,22271,22273,22283,22307,22343,22369,22381,22391,22447,22481,22501,22511,22549,22567,22571,22573,22613,22643,22651,22709,22717,22727,22751,22777,22783,22807,22811,22859,22861,22871,22877,22901,22907,22921,22943,22973,23011,23039,23053,23057,23059,23063,23071,23081,23087,23117,23131,23143,23159,23173,23201,23209,23251,23269,23293,23297,23311,23321,23333,23339,23357,23399,23417,23447,23459,23497,23509,23531,23557,23561,23563,23567,23581,23593,23599,23627,23669,23671,23687,23689,23719,23747,23753,23761,23789,23801,23813,23833,23869,23899,23911,23993,24019,24023,24049,24077,24091,24097,24103,24107,24109,24113,24137,24169,24181,24223,24251,24281,24329,24371,24379,24391,24407,24419,24439,24469,24481,24499,24517,24527,24533,24547,24571,24611,24631,24671,24683,24691,24697,24709,24749,24781,24793,24799,24821,24841,24847,24851,24859,24877,24889,24919,24923,24943,24953,24967,24977,24979,24989,25031,25057,25087,25097,25111,25117,25121,25127,25147,25163,25171,25183,25189,25237,25243,25247,25253,25261,25309,25321,25343,25349,25373,25391,25409,25411,25439,25447,25453,25463,25471,25541,25561,25583,25603,25621,25633,25639,25667,25673,25693,25717,25733,25747,25763,25771,25799,25801,25819,25849,25889,25903,25913,25919,25933,25939,25969,25981,25999,26017,26021,26029,26041,26107,26111,26119,26153,26177,26183,26249,26263,26293,26321,26339,26347,26371,26387,26399,26407,26417,26423,26431,26449,26459,26489,26497,26557,26591,26597,26633,26681,26687,26699,26701,26711,26723,26731,26737,26759,26777,26783,26813,26879,26881,26893,26903,26921,26927,26947,26951,26953,26993,27017,27059,27061,27067,27077,27091,27107,27109,27127,27143,27179,27191,27197,27259,27271,27277,27299,27329,27337,27397,27407,27431,27437,27449,27457,27479,27529,27539,27541,27581,27611,27617,27631,27647,27653,27673,27691,27701,27733,27739,27743,27749,27751,27763,27767,27773,27779,27793,27809,27823,27847,27851,27917,27919,27941,27943,27947,27953,27961,27967,27983,27997,28019,28027,28051,28057,28069,28081,28087,28163,28181,28183,28211,28219,28229,28283,28289,28307,28309,28349,28351,28387,28393,28403,28409,28433,28447,28463,28477,28513,28517,28547,28559,28571,28573,28579,28591,28597,28621,28627,28631,28657,28661,28663,28669,28687,28703,28711,28753,28759,28789,28793,28807,28813,28817,28837,28843,28859,28871,28879,28909,28921,28927,28933,28949,28979,29023,29027,29033,29063,29077,29101,29129,29147,29153,29167,29179,29201,29207,29221,29251,29269,29287,29297,29327,29333,29339,29347,29383,29387,29399,29423,29443,29453,29473,29483,29501,29527,29537,29573,29581,29599,29611,29629,29633,29641,29741,29759,29803,29837,29863,29867,29879,29881,29921,29927,29947,29959,29983]
k = 1144765
print(len(ls))
# s = Solution()
# print(s.kthSmallestPrimeFraction(ls,k))