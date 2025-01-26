from pset3 import *

def test_ps3():
    """
    Unit test for the method apply shift
    """
    failure=False
    testcases = {
        ("zjnzhyyv") : "jnz",
        ("tazrhfroeoerdi") : "az",
        ("qelhomoy") : "moy",
        ("rfcpthlbdgpostxwp") : "bdgp",
        ("miytvsissj") : "iss",
        ("winnbnnk") : "inn",
        ("rmyqhcslvrordnsnneqlwd") : "dns",
        ("abcdefghijklmnopqrstuvwxyz") : "abcdefghijklmnopqrstuvwxyz",
        ("zefanhbvhuuiajtre") : "huu",
        ("fvtvnxfpomrmllflnx") : "flnx",
        ("gqscbthnnxlujliejrcxfppo") : "hnnx",
        ("zyxwvutsrqponmlkjihgfedcba") : "z",
        ("hhwlayvrazcprkgodflpxv") : "dflpx",
        ("tcswmlcs") : "csw",
        ("ocznvzicqpamauqrsmt") : "nvz",
        ("omwnegbibnhkngbofgf") : "hkn",
        ("wfzpvdmgfubkqqecfeebhye") : "bkqq",
        ("nvastcphu") : "ast",
        ("olvyrhjgqf") : "lvy",
        ("vetaylfyqyycemz") : "cemz",
    }
    for testcase in testcases.keys():
        test_result = get_longest_alpha_substr(testcase)
        if test_result != testcases[testcase]:
            print("FAILURE:")
            print("\tExpected", testcases[testcase], " but got '" + test_result + "' for string '" + testcase + "'")
            failure=True
        else:
            print("\tPASS the test '" + testcase + "'; expected ouput: '" + testcases[testcase] + "'")
    
    if not failure:
        print("SUCCESS")

print("----------------------------------------------------------------------")
print("Testing pset 3 week 1: get longest alphabetical substring...")
test_ps3()

