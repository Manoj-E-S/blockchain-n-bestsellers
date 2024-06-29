import { useEffect, useState } from "react"
import getBooks from "../functions/getBooks"
import { useNavigate } from "react-router-dom"

const BookSection = ({placeholder, url}: {placeholder: string, url: string}) => {
    const navigate = useNavigate();
    const [Books, setBooks] = useState([])
    useEffect(() => {
      async function populateBooks(fetchUrl: string) {
        const books = await getBooks(fetchUrl);
        console.log(books);
        if(books.data) {
          setBooks(books.data);
        } else {
            console.log(`Error fetching books for\n ${fetchUrl}`);
        }
      }
      populateBooks(url);
    }, [])
  return (
    
    <>
        <div className="flex flex-col p-4">
            <h2 className="font-gallient text-3xl font-bold mt-10 pl-10">{placeholder}</h2>
            <div className="grid grid-cols-5 gap-8 py-2">
                {Books?.map((book, index) => {
                    if(index > 4) return null;
                    return (
                        <div onClick={() => navigate(`/book/${book.isbn}`)} key={book.isbn} className="flex flex-col gap-1">
                            <img src={book.imgUrlLarge} alt={book.title} className="h-64  object-contain" />
                            <h3 className="font-gallient text-xl font-bold text-center">{book.title}</h3>
                        </div>
                    )
                })}
            </div>
        </div>
    </>
  )
}

export default BookSection