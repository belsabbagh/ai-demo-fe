# AI Model Demo Frontend

This is a template for a frontend application that can be used to demonstrate an AI model. It is based on [Create Vite App](https://vitejs.dev/guide/#scaffolding-your-first-vite-project).

## Getting Started

Clone this repository and install the dependencies:

```bash
npm install
```

## Running the App

To run the app, run:

```bash
npm run dev
```

## Structure
### Backend
The `server.py` file is a simple Flask server that creates a simple `/predict` endpoint that can be used to make predictions. 

In that file, there is a `mk_predict` function that should return a reference to the prediction function of the model that you will be demonstrating. The function takes a path to the file or directory that contains the data that will be used to load the model and build the prediction function.

Then, there are functions to validate input data and make error messages just in case you need more than the default error messages.

There is also a `preprocess_request` function that can be used to preprocess the request data before it is passed to the prediction function. This is useful if you need to do some preprocessing before making a prediction.

Finally, there is a `format_prediction` function that takes the prediction and builds the response dict that will be returned to the frontend.

After these, the endpoint is defined to make use of all these functions to handle prediction requests.

### Frontend
The `src/App.svelte` file contains the frontend code that makes a request to the `/predict`.

The `predict` function is the function that makes the request to the `/predict` endpoint. It takes the data that will be used to make the prediction and returns a promise that resolves to the prediction.
