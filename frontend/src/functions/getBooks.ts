export default async function getBooks(url: string, n: number = 10) {
    const finalUrl = url + '/' + n;
    console.log(finalUrl);
    const response = await fetch(finalUrl, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    const data = await response.json();
    return { data, ok: response.ok }
  }