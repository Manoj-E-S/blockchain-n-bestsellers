import React from "react";

type BookTrayProps = {
  heading: string;
  apiUrl: string;
};

const BookTray: React.FC<BookTrayProps> = ({ heading, apiUrl }) => {
  return (
    <div className="book-tray">
      <h2 className="heading text-2xl font-gallient font-semibold tracking-wide">
        {heading}
      </h2>
      <div className="mt-5 w-full h-fit p-10 flex items-center gap-20">
        <div className="w-fit book-detailed-info flex flex-col gap-2">
          <img
            className="h-72 shadow-customShadow"
            src="/assets/pride-and-prejudice-cover.jpg"
            alt="Pride and Prejudice"
          />
          <div className="book-text mt-5">
            <h3 className="text-xl font-gallient font-semibold tracking-wide">
              Pride and Prejudice
            </h3>
            <h4 className="text-md font-gallient text-gold font-semibold tracking-wider">
                Jane Austen
            </h4>
            <h4 className="text-md font-gallient text-gold font-semibold tracking-widest">
                1813
            </h4>
          </div>
        </div>

        {/* BookDetailedInfo Repeating */}
        <div className="w-fit book-detailed-info flex flex-col gap-2">
          <img
            className="h-72 shadow-customShadow"
            src="/assets/robinson-crusoe-cover.jpg"
            alt="Robinson Crusoe"
          />
          <div className="book-text mt-5">
            <h3 className="text-xl font-gallient font-semibold tracking-wide">
                Robinson Crusoe
            </h3>
            <h4 className="text-md font-gallient text-gold font-semibold tracking-wider">
                Daniel Defoe
            </h4>
            <h4 className="text-md font-gallient text-gold font-semibold tracking-widest">
                1719
            </h4>
          </div>
        </div>


        <div className="w-fit book-detailed-info flex flex-col gap-2">
          <img
            className="h-72 shadow-customShadow"
            src="/assets/david-copperfield-cover.jpg"
            alt="David Copperfield"
          />
          <div className="book-text mt-5">
            <h3 className="text-xl font-gallient font-semibold tracking-wide">
                David Copperfield
            </h3>
            <h4 className="text-md font-gallient text-gold font-semibold tracking-wider">
                Charles Dickens
            </h4>
            <h4 className="text-md font-gallient text-gold font-semibold tracking-widest">
                1849
            </h4>
          </div>
        </div>

        <div className="w-fit book-detailed-info flex flex-col gap-2">
          <img
            className="h-72 shadow-customShadow"
            src="/assets/black-beauty-cover.jpg"
            alt="Black Beauty"
          />
          <div className="book-text mt-5">
            <h3 className="text-xl font-gallient font-semibold tracking-wide">
                Black Beauty
            </h3>
            <h4 className="text-md font-gallient text-gold font-semibold tracking-wider">
                Anna Sewell
            </h4>
            <h4 className="text-md font-gallient text-gold font-semibold tracking-widest">
                1877
            </h4>
          </div>
        </div>

        <div className="w-fit book-detailed-info flex flex-col gap-2">
          <img
            className="h-72 shadow-customShadow"
            src="/assets/to-kill-a-mockingbird-cover.jpg"
            alt="To Kill a MockingBird"
          />
          <div className="book-text mt-5">
            <h3 className="text-xl font-gallient font-semibold tracking-wide">
                To Kill a MockingBird
            </h3>
            <h4 className="text-md font-gallient text-gold font-semibold tracking-wider">
                Harper Lee
            </h4>
            <h4 className="text-md font-gallient text-gold font-semibold tracking-widest">
                1960
            </h4>
          </div>
        </div>
        {/* Till Here */}
      </div>
    </div>
  );
};

export default BookTray;
