import React from 'react'
import BookTray from '../BookTray'

const BookDetails : React.FC = () => {
  return (
    <section className='min-h-[100vh] w-full p-20 flex flex-col gap-20 mb-20'>
      <BookTray heading="- Popular up For Exchange" apiUrl="http://localhost:3000/newBooks" />
      <BookTray heading="- Bestselling Books up For Exchange" apiUrl="http://localhost:3000/newBooks" />
      <BookTray heading="- New Books up For Exchange" apiUrl="http://localhost:3000/newBooks" />
    </section>
  )
}

export default BookDetails
