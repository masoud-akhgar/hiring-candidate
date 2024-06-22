import BankClassifier
import requests

url = "https://imgv2-1-f.scribdassets.com/img/document/659172856/original/b30b97cd92/1716130594?v=1"
print(BankClassifier.BankDocPredictor().predict(url))