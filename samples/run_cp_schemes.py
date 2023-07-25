'''
:Date:            4/2022
'''

from charm.toolbox.pairinggroup import PairingGroup, GT
from FABEO.fabeo22cp import FABEO22CPABE

def run_cpabe(abe, attr_list, policy_str, msg):
    (mpk, msk) = abe.setup()
    key = abe.keygen(mpk, msk, attr_list)
    ctxt = abe.encrypt(mpk, msg, policy_str)
    rec_msg = abe.decrypt(mpk, ctxt, key)
    
    if debug:
        if rec_msg == msg:
            print("Successful decryption for {}.".format(abe.name))
        else:
            print("Decryption failed for {}.".format(abe.name))

def main():
    # instantiate a bilinear pairing map
    pairing_group = PairingGroup('MNT224')

    attr_list = ['1', '2', '3']
    policy_str = '((1 and 3) and (2 OR 4))'

    # choose a random message
    msg = pairing_group.random(GT)
   
    fabeo22_cp = FABEO22CPABE(pairing_group)
    run_cpabe(fabeo22_cp, attr_list, policy_str, msg)

if __name__ == "__main__":
    debug = True
    main()
