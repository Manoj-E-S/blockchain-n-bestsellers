import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import getBook from "../../functions/getBook";

// Function to generate star rating
const renderStars = (rating: number) => {
  const fullStars = Math.floor(rating);
  const halfStar = rating % 1 >= 0.5 ? 1 : 0;
  const emptyStars = 5 - fullStars - halfStar;

  const stars = [];

  for (let i = 0; i < fullStars; i++) {
    stars.push(<span key={`full-${i}`}>&#9733;</span>); // full star
  }
  if (halfStar) {
    stars.push(<span key="half">&#9734;</span>); // half star
  }
  for (let i = 0; i < emptyStars; i++) {
    stars.push(<span key={`empty-${i}`}>&#9734;</span>); // empty star
  }

  return stars;
};

const DetailedView: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const params = useParams();
  const isbn = params.id;
  const [Book, setBook] = useState(null);


  useEffect(() => {
    const getBookFromDB = async () => {
      const book = await getBook('http://localhost:3000/books', isbn);
      if(book.ok) {
        console.log(book.data);
        setBook(book.data);
      } else {
        console.log('Error fetching book');
      }

    };

    getBookFromDB();
  }, [id]);

  return (
    <div className="bg-[#c2b19c] w-full h-[100vh] flex items-center justify-center text-darkBrown">
      <div className="left h-full w-1/2 flex items-center justify-center">
        <img className="h-full p-5" src={Book?.imgUrlLarge} alt="Book Cover" />
      </div>
      <div className="right h-full w-1/2 flex flex-col gap-5 p-20 font-raleway">
        <h1 className="text-4xl font-gallient font-bold tracking-wide">{Book?.title}</h1>
        <p className="text-lg">
          By <span className="font-bold">{Book?.author}</span>
        </p>
        <p className="text-lg">
          Average Rating: {renderStars(Book?.avg_rating)}
        </p>
        <p className="text-md text-brown">
          {Book?.description}
        </p>
        <hr />
        <div className="book-detailed-text grid grid-cols-2 gap-x-10 gap-y-4">
          <div className="flex gap-2">
            <h4 className="font-bold">ISBN</h4>
            <p className="text-brown">{Book?.isbn}</p>
          </div>
          <div className="flex gap-2">
            <h4 className="font-bold">Genre</h4>
            <p className="text-brown">{Book?.genres?.join(" | ")}</p>
          </div>
          <div className="flex gap-2">
            <h4 className="font-bold">Publisher</h4>
            <p className="text-brown">{Book?.publisher}</p>
          </div>
          <div className="flex gap-2">
            <h4 className="font-bold">Year Of Publication</h4>
            <p className="text-brown">{Book?.year_of_publication}</p>
          </div>
        </div>
        <div className="person-posted mt-5">
          <div className="flex items-center gap-4">
            <img
              className="w-10 h-10 rounded-full"
              src="/docs/images/people/profile-picture-5.jpg"
              alt="Profile"
            />
            <div className="font-medium text-darkBrown">
              <div className="font-bold">Shared By</div>
              <div className="text-sm text-brown">John Smith</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DetailedView;
