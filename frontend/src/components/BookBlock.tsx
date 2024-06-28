import React from 'react';

type PropType = {
  imgSrc: string;
  desc: string;
};

const BookBlock: React.FC<PropType> = ({ imgSrc, desc }) => {
  return (
    <div className='bg-[#f2f5f8] h-[27vw] w-[20vw] p-10 flex items-center justify-center'>
      <img 
        src={imgSrc} 
        alt={desc} 
        className='h-full w-full object-cover object-center shadow-customShadow rounded-lg'
      />
    </div>
  );
};

export default BookBlock;
