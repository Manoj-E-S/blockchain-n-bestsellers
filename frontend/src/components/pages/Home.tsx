import React from 'react'
import Hero from '../sections/Hero'
import BookDetails from '../sections/BookDetails'
import Newsletter from '../sections/Newsletter'
import Testimonials from '../sections/Testimonials'

const Home : React.FC = () => {
  return (
    <main className='h-fit w-full bg-cream'>
      <Hero />
      <BookDetails />
      <Testimonials />
      <Newsletter />
    </main>
  )
}

export default Home
