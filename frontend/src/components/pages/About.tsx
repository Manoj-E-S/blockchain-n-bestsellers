import React from "react";

const About: React.FC = () => {
  return (
    <div className="bg-[#c2b19c]">
      {/* About Us Section */}
      <div className="w-full min-h-[50vh] flex items-center justify-center p-20">
        <div className="w-[60%] p-6">
          <h2 className="text-4xl font-bold mb-4 font-gallient tracking-wider">
            About Us
          </h2>
          <p className="text-lg w-[80%] font-raleway">
            Bookworms and Bestsellers is a platform dedicated to book lovers.
            Our mission is to connect readers and help them discover new
            favorites while facilitating book exchanges within a vibrant
            community. <br />
            <br />
            Join us in celebrating the joy of reading and become part of a
            community that treasures the written word, promotes lifelong
            learning, and fosters a love for books in every corner of the world!
          </p>
        </div>
        <div className="w-[40%] p-6">
          <img
            src="/assets/about-us.jpg"
            alt="About Us"
            className="h-[40vw] w-full rounded-lg shadow-lg object-cover object-center"
          />
        </div>
      </div>
      {/* Our Mission Section */}
      <div className="w-full min-h-[50vh] flex items-center justify-center p-20">
        <div className="w-[40%] p-6 mr-10">
          <img
            src="/assets/our-mission.jpg"
            alt="Our Mission"
            className="h-[40vw] w-full rounded-lg shadow-lg object-cover object-center"
          />
        </div>
        <div className="w-[60%] p-6">
          <h2 className="text-4xl font-bold mb-4 font-gallient tracking-wider">
            Our Mission
          </h2>
          <p className="text-lg w-[85%] font-raleway">
            Our mission is to create a seamless experience for book enthusiasts
            to find and exchange books. We aim to foster a sense of community
            and encourage the sharing of knowledge and stories. <br/><br/>At Bookworms and
            Bestsellers, we believe that books are more than just words on a
            page—they are gateways to different worlds, perspectives, and
            emotions. We strive to make discovering and sharing these worlds as
            easy and enjoyable as possible, ensuring that every reader finds
            their next great adventure.
          </p>
        </div>
      </div>
    </div>
  );
};

export default About;
