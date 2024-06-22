# BackEnd Project - Python Developer
This python program uses the pre-trained model (detr-doc-table-detection) in the context of object detection to detect tables related to bank documents and invoices.

In total, there are three python files in this project:
- **BankClassifier** : a class developed using the Detr pretrained model to detect invoice and bank documents data in this particular case.
- **BankClassifier_test** : an automated test coded as an unit test for the main class
- **sampleUsage** : a sample use case which show simply how the class can be used after importing into the project
- I also prepared an image **Scenarios.JPG** which we can explore the different scenarios which the model can end up, coinciding with the associated error.

Of course to deploy the model, the simpleUsage and test-related files were neglected to be mentioned on dockerfile.

you can find the main class, named **BankDocPredictor**, on **BankClassifier.py** file. A few pictures of the dataset of Detr model have been used to test the correctness of the main model on **BankClassifier_test.py** file, while there has been added some pictures from **Financial Document Image Dataset** to test the model even more.

Financial Document Image Dataset :
https://www.kaggle.com/datasets/mehaksingal/personal-financial-dataset-for-india

You can see the different deduced scenarios on **Scenarios.JPG** in the project folder.
the model can be used by calling the predict function of BankDocPredictor class in the main directory.

Dockerize the project:

To run the project, after logging into your server host, use following command to copy the code onto the server:

`scp -R InvoiceDetection/ my-server.host.name:InvoiceDetection/`

after making sure to install docker on server too, by this command...:

`curl -fsSL https://get.docker.com | sudo sh`

then run the code using:

`cd InvoiceDetection/`
`docker compose build`
`docker compose up -d`

in the case of killing the process which now is running in the background, we can use `docker compose down`.
we can also check if the process is running by `docker ps`.

