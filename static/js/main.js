const form = document.querySelector("form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const username = document.querySelector("#username").value;
  const password = document.querySelector("#password").value;

  const data = { username: username, password: password };

  const response = await fetch("/login", {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (response.ok) {
    const result = await response.json();
    console.log(result);
  } else {
    console.error(response.status);
  }
});
