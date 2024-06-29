export default async function getBook(url: string, isbn: string) {
    const finalUrl = url + '/' + isbn;
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