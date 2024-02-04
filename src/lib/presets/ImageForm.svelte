<script>
    export let handleSubmit;
</script>

<form method="post" on:submit|preventDefault={handleSubmit}>
    <input type="file" name="image" placeholder="Choose image to predict" accept="image/*" />
    <button type="submit">Predict</button>
</form>
