import os, random
import gc
import BankClassifier
import pytest

@pytest.fixture
def objClassifier():
    return BankClassifier.BankDocPredictor()

def test_Instance(objClassifier):
    # test the existence of bank_label_ids file
    assert type(objClassifier.__str__()) == str

def test_bankTestFolder_is_full():
    assert (("cTDaR_t00648.jpg" in os.listdir("./testdata/bank_doc")) and 
    ("cTDaR_t00114.jpg" in os.listdir("./testdata/bank_doc"))) == True

def test_NotValidImage(objClassifier):
    os.system("touch ./testdata/bank_doc/notValideImage.txt")
    assert objClassifier.predict("./testdata/bank_doc/cTDaR_t00114.txt") =="Error: Not a Valid Image"
    os.system("rm ./testdata/bank_doc/notValideImage.txt")

def test_NoTableDetected(objClassifier):
    assert objClassifier.predict("./testdata/bank_doc/cTDaR_t00114.jpg") =="Error: No Table Invoice Was Detected"

def test_performanceTime_prediction(objClassifier, benchmark):
    def run():
        temp = objClassifier.predict("./testdata/bank_doc/cTDaR_t00648.jpg")
    benchmark(run)
    assert benchmark.stats['min'] >= 1
    assert benchmark.stats['max'] < 120

def test_successfullyDetected(objClassifier):
    retrievedList=objClassifier.predict("./testdata/bank_doc/cTDaR_t00648.jpg")
    assert "Detected book with confidence 0.994 at location [74.98, 324.43, 2446.26, 2782.7]"==retrievedList[0]
    assert len(retrievedList)>0

def test_completelyDetected(objClassifier):
    retrievedList=objClassifier.predict("./testdata/bank_doc/3.jpg")
    assert len(retrievedList)>=2
