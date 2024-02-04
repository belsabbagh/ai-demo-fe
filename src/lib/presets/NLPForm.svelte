<script>
  export let handleSubmit;
</script>

<form method="post" on:submit|preventDefault={handleSubmit}>
  <input type="text" name="text" placeholder="Enter text to predict" />
  <button type="submit">Predict</button>
</form>


<style>
  form {
      width: 100%;
      margin: 0 auto;
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
  }
  /* form children */
  :global(form > *:not(:last-child)) {
      margin-bottom: 20px;
  }

  input {
      width: 100%;
      height: 50px;
      font-size: 20px;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 1rem;
  }

  button {
      height: 50px;
      font-size: 20px;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 1rem;
  }
</style>
