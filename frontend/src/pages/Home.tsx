import Hero from "../components/Hero/Hero.tsx";
import HorizontalNavbar from "../components/HorizontalNavbar/HorizontalNavbar.tsx";
import Sneekpeek from "../components/Sneekpeek/Sneekpeek.tsx";
import Footer from "../components/Footer/Footer.tsx";

const Home = () => {
  return (
    <>
        <HorizontalNavbar />
        <Hero />
        <Sneekpeek />
        <Footer />
    </>
  );
}

export default Home;
