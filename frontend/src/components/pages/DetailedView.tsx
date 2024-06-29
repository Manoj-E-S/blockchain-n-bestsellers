import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

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
  const [rating, setRating] = useState<number>(0);

  useEffect(() => {
    // Mock fetch rating from API
    const fetchRating = async () => {
      // Replace this with your API call
      const response = await new Promise<{ rating: number }>((resolve) =>
        setTimeout(() => resolve({ rating: 4.3 }), 1000)
      );
      setRating(response.rating);
    };

    fetchRating();
  }, [id]);

  return (
    <div className="bg-[#c2b19c] w-full h-[100vh] flex items-center justify-center text-darkBrown">
      <div className="left h-full w-1/2 flex items-center justify-center">
        <img className="h-full p-5" src="/assets/black-beauty-cover.jpg" alt="Book Cover" />
      </div>
      <div className="right h-full w-1/2 flex flex-col gap-5 p-20 font-raleway">
        <h1 className="text-4xl font-gallient font-bold tracking-wide">Book Name</h1>
        <p className="text-lg">
          By <span className="font-bold">Author Name</span>
        </p>
        <p className="text-lg">
          Average Rating: {renderStars(rating)}
        </p>
        <p className="text-md text-brown">
          In the heart of an ancient and mystical forest, young Elara discovers
          a hidden world filled with magical creatures, lost secrets, and untold
          adventures. When she stumbles upon an ancient artifact, she
          unknowingly awakens an age-old prophecy that foretells the return of a
          great power. With the help of a mysterious guide, Elara embarks on a
          perilous journey to unravel the secrets of the enchanted forest and
          protect it from dark forces that seek to conquer its magic. Along the
          way, she forms unbreakable bonds with newfound friends, faces her
          deepest fears, and uncovers the true strength within herself.
        </p>
        <hr />
        <div className="book-detailed-text grid grid-cols-2 gap-x-10 gap-y-4">
          <div className="flex gap-2">
            <h4 className="font-bold">ISBN</h4>
            <p className="text-brown">3243334</p>
          </div>
          <div className="flex gap-2">
            <h4 className="font-bold">Genre</h4>
            <p className="text-brown">Action | Adventure | Sci-fi</p>
          </div>
          <div className="flex gap-2">
            <h4 className="font-bold">Publisher</h4>
            <p className="text-brown">Penguin Books</p>
          </div>
          <div className="flex gap-2">
            <h4 className="font-bold">Year Of Publication</h4>
            <p className="text-brown">2003</p>
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
