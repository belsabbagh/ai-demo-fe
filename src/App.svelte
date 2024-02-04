<script>
    import { resultsStore } from "./stores/result";
    import { errorStore } from "./stores/error";
    import NlpForm from "./lib/NLPForm.svelte";
    import ImageForm from "./lib/ImageForm.svelte";

    const TITLE = "Model Prediction";
    const AI_API_URL = "http://localhost:5000/predict";

    function extractResult(data) {
      //TODO: Change this to return the result that you want to display
        return JSON.stringify(data);
    }

    function buildRequest(formData) {
      //TODO: Change this to return the request object that will be sent to the server.
      return {
            body: "",
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
        };
    }

    async function predict(event) {
        const formData = new FormData(event.target);
        const request = buildRequest(formData);
        const response = await fetch(AI_API_URL, request);
        const data = await response.json();
        if (!response.ok) {
            errorStore.set(data.error);
            resultsStore.set("");
            return;
        }
        resultsStore.set(extractResult(data));
        errorStore.set("");
    }
</script>

<main>
    <h1>{TITLE}</h1>
    <div class="error">{$errorStore}</div>
    <form method="post" on:submit|preventDefault={handleSubmit}>
        TODO: Write the input form here.
    </form>
    <div class="results">
        <h2>Result: {$resultsStore}</h2>
    </div>
</main>
