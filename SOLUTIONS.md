The directory `/lab/analysis-cesar/` contains several notebooks with the exploratory data analysis (EDA) and two versions of the ETL and modeling process. One for a regression approach and another one for a classification task. Each of these files is well organized in sections and includes comments to help the reader understand the results and the decisions made.

We have limited the raw dataset to a subset that only takes into account the variables related to the fields included in the input example for the API.

The final model that we trained in this project can be found in `/models/catboost-model-depth12-iter200-l2reg1_5-lr0_1`.

In order to build an API that makes use of the trained model to define the price category for a new listing we have used Flask and Swagger design and document. The code is included in the directory `/api/`. The file `main.py` launches the API and `/controllers/price_controller.py` receives the requests, handles the preprocessing and calls the model to generate the predicted price category.

The directory `/controllers/tests/` contains unit tests that are run every time we make a push to the `develop` branch of this project. It is part of the CI workflow implemented on GitHub and evaluates the correct functioning of the process in charge of receiving the request body and generate a response.

Finally, the API can be deployed on a Docker container. The `Dockerfile` can be fould in the directory `/api/`, as well as the requirements needed to build the image.

The reader can test the API by running `python main.py` from `/api/` or by building an image based on the Dockerfile. These are the commands that executed from the `/api/` directory launch the API in a Docker container.
- `docker build --no-cache -t the-mle-challenge:latest .`
- `docker run -p 8080:8080 the-mle-challenge:latest`

In both cases, to test this solution we just have to make a POST request to `0.0.0.0:8080/data_input` with a valid input in a JSON format.