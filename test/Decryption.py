import unittest
import sys
sys.path.append(".")

from src.Sampling import Sampling
from src.McmcException import DecryptionException 
from src.Decryption import Decryption

class DecryptionTest(unittest.TestCase):
    def test_run(self):
        decryption = make_decryption()
        sampling = Sampling()
        sampling.set_path("test/words/francais_30000.txt")
        #test erreur path/data and sampling renseigned
        self.assertRaises(DecryptionException, decryption.run) #error because sampling not renseigned
        # self.assertRaises(DecryptionException, decryption.set_sampling, sampling) #error because sampling not runed // now this error is catch from sampling class
        decryption.set_sampling(sampling=sampling) 
        self.assertRaises(DecryptionException, decryption.run) #error because data/path not renseigned
        decryption.set_path("test/words/chiffrer.txt")
        # decryption.set_data("a word")
        decryption.run()

    def test_accept_plausible_degradation(self):
        decryption = make_decryption()
        self.assertRaises(DecryptionException, decryption.set_acceptable_degration, 1.1)
        self.assertRaises(DecryptionException, decryption.set_acceptable_degration, 2)
        self.assertRaises(DecryptionException, decryption.set_acceptable_degration, -0.0000001)
        decryption.set_acceptable_degration()
        decryption.set_acceptable_degration(0.00005)
        decryption.set_acceptable_degration(1.00000000)
        
        
def make_decryption():
    decryption = Decryption()
    # decryption.set_data(data=get_content())
    return decryption

if __name__ == '__main__':
    unittest.main()