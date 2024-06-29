export default async function completeSignup(location: string, contact_no: string) {
    const response = await fetch("http://localhost:3000/auth/completeSignup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        'Authorization': `${localStorage.getItem('token')}`,
      },
      body: JSON.stringify({ location, contact_no, bio: `My Name is ${JSON.parse(atob(localStorage.getItem('token').split(".")[1])).user.name}` }),
    });
    const data = await response.json();
    return { data, ok: response.ok }
}