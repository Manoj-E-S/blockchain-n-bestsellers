import BookSection from "../BookSection"

const Books = ({FavGenres}) => {
  return (
    <div className="py-10 bg-[#c2b19c]">
        <h1 className="font-gallient tracking-wide text-5xl font-bold text-center">Books</h1>
        <BookSection placeholder='Popular Books' url="http://localhost:3000/books/nPopularBooks" />
        <BookSection placeholder='Random Books' url="http://localhost:3000/books/nRandomBooks" />
        {FavGenres.map(genre => {
            return <BookSection key={genre} placeholder={genre} url={`http://localhost:3000/books/nPopularGenreBooks/${genre}`} />
        })}
    </div>
  )
}

export default Books