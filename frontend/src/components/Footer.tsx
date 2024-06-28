import React from "react";
import { Link } from "react-router-dom";

const Footer: React.FC = () => {
  return (
    <footer className="bg-[#cd8e64] font-raleway">
      <div className="mx-auto w-full max-w-screen-xl p-4 py-6 lg:py-8">
        <div className="md:flex md:justify-between">
          <div className="mb-6 md:mb-0">
            <Link to="/" className="flex items-center bg-cream rounded-md p-2">
              <img
                src="/assets/logoFull_L_nobg.png"
                className="h-40 me-3"
                alt="B&B Logo"
              />
            </Link>
          </div>
          <div className="grid grid-cols-2 gap-8 sm:gap-6 sm:grid-cols-3">
            <div>
              <h2 className="mb-6 text-lg font-semibold text-darkBrown uppercase">
                Our Links
              </h2>
              <ul className="text-brown font-medium">
                <li className="mb-2">
                  <Link to="/" className="hover:text-cream">
                    Home
                  </Link>
                </li>
                <li className="mb-2">
                  <Link
                    to="/about"
                    className="hover:text-cream"
                  >
                    About
                  </Link>
                </li>
                <li className="mb-2">
                  <Link
                    to="/books"
                    className="hover:text-cream"
                  >
                    Books
                  </Link>
                </li>
                <li className="mb-2">
                  <Link
                    to="/contact"
                    className="hover:text-cream"
                  >
                    Contact Us
                  </Link>
                </li>
              </ul>
            </div>
            <div>
              <h2 className="mb-6 text-lg font-semibold text-darkBrown uppercase">
                Socials
              </h2>
              <ul className="text-brown font-medium">
                <li className="mb-2">
                  <a
                    href="#"
                    className="hover:text-cream "
                  >
                    Facebook
                  </a>
                </li>
                <li className="mb-2">
                  <a
                    href="#"
                    className="hover:text-cream"
                  >
                    Instagram
                  </a>
                </li>
                <li className="mb-2">
                  <a
                    href="#"
                    className="hover:text-cream"
                  >
                    LinkedIn
                  </a>
                </li>
                <li className="mb-2">
                  <a
                    href="#"
                    className="hover:text-cream"
                  >
                    Twitter
                  </a>
                </li>
              </ul>
            </div>
            <div>
              <h2 className="mb-6 text-lg font-semibold text-darkBrown uppercase">
                Legal
              </h2>
              <ul className="text-brown font-medium">
                <li className="mb-4">
                  <a href="#" className="hover:text-cream">
                    Privacy Policy
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-cream">
                    Terms &amp; Conditions
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <hr className="my-6 border-darkBrown sm:mx-auto lg:my-8" />
        <div className="sm:flex sm:items-center sm:justify-between">
          <span className="text-md font-semibold text-darkBrown sm:text-center">
            © {new Date().getFullYear()}{" "}
            <a href="https://flowbite.com/" className="hover:underline">
              B&B™
            </a>
            . All Rights Reserved.
          </span>
          <div className="text-darkBrown font-semibold flex mt-4 sm:justify-center sm:mt-0">
           Where Stories Meet New Friends.
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
