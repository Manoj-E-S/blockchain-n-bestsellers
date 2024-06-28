import React from "react";
import BookBlock from "../BookBlock";

const Hero: React.FC = () => {
  return (
    <section className="w-full h-[150vh] relative text-darkBrown py-10 px-5 text-center font-gallient tracking-widest">
      <div className="headings absolute top-[15%] left-[15%] z-[10]">
        <h1 className="text-5xl md:text-7xl font-bold">
          Discover Your Next Favorite Book
        </h1>
        <h2 className="text-2xl md:text-2xl mt-4 font-semibold">
          Exchange, Recommend, and Dive into a World of Stories
        </h2>
      </div>

      <div className="absolute top-[50%] left-[5%] z-[10]">
        <BookBlock imgSrc="assets/ikigai-cover.jpg" desc="ikigai cover" />
        <h2 className="mt-5 text-xl text-white font-bold text-left">Ikigai</h2>
        <h3 className="text-sm text-gray-300 font-semibold text-left">Bestseller of 2016</h3>
      </div>
      <div className="absolute top-[40%] left-[28%] z-[10]">
        <BookBlock
          imgSrc="assets/atomic-habits-cover.jpeg"
          desc="atomic habits cover"
        />
        <h2 className="mt-5 text-xl text-white font-bold text-left">
          Atomic Habits
        </h2>
        <h3 className="text-sm text-gray-300 font-semibold text-left">Published in 2018</h3>
      </div>
      <div className="absolute top-[50%] left-[51%] z-[10]">
        <BookBlock
          imgSrc="assets/comfort-book-cover.jpg"
          desc="comfort book cover"
        />
        <h2 className="mt-5 text-xl text-white font-bold text-left">
          The Comfort Book
        </h2>
        <h3 className="text-sm text-gray-300 font-semibold text-left">Bestseller of 2021</h3>
      </div>
      <div className="absolute top-[40%] left-[74%] z-[10]">
        <BookBlock imgSrc="assets/alchemist-cover.jpg" desc="alchemist cover" />
        <h2 className="mt-5 text-xl text-white font-bold text-left">
          The Alchemist
        </h2>
        <h3 className="text-sm text-gray-300 font-semibold text-left">Published in 1988</h3>
      </div>

      <div className="w-full h-[25vw] bg-darkBrown absolute bottom-0 left-0"></div>
    </section>
  );
};

export default Hero;
