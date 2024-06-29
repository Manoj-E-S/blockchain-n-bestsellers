export default async function signup(name: string, email: string, password: string) {
    const response = await fetch("http://localhost:3000/auth/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name, email, password }),
    });
    const data = await response.json();
    localStorage.setItem("token", data.token);
    return { data, ok: response.ok }
  }